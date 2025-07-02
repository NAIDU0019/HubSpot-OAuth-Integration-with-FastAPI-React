# slack.py
from fastapi import Request
import os
from urllib.parse import urlencode
import requests
import redis
from fastapi.responses import JSONResponse

async def authorize_hubspot(user_id, org_id):
    client_id = os.getenv("HUBSPOT_CLIENT_ID")
    redirect_uri = os.getenv("HUBSPOT_REDIRECT_URI")
    scope = "crm.objects.contacts.read crm.objects.companies.read crm.objects.deals.read oauth"
  # Add more scopes if needed
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scope,
        "state": f"{user_id}:{org_id}",
        "response_type": "code",
    }
    auth_url = f"https://app.hubspot.com/oauth/authorize?{urlencode(params)}"
    return {"auth_url": auth_url}



async def oauth2callback_hubspot(request: Request):
    try:
        code = request.query_params.get("code")
        state = request.query_params.get("state")

        if not code or not state:
            return JSONResponse(status_code=400, content={"error": "Missing code or state in callback"})

        user_id, org_id = state.split(":")

        token_url = "https://api.hubapi.com/oauth/v1/token"
        redirect_uri = os.getenv("HUBSPOT_REDIRECT_URI")

        data = {
            "grant_type": "authorization_code",
            "client_id": os.getenv("HUBSPOT_CLIENT_ID"),
            "client_secret": os.getenv("HUBSPOT_CLIENT_SECRET"),
            "redirect_uri": redirect_uri,
            "code": code,
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(token_url, data=data, headers=headers)

        if response.status_code != 200:
            return JSONResponse(status_code=500, content={
                "error": "Failed to fetch access token",
                "details": response.text
            })
        tokens = response.json()
        access_token = tokens.get("access_token")
        if not access_token:
            return JSONResponse(status_code=500, content={"error": "No access_token in response"})

        r = redis.Redis()
        r.set(f"hubspot:{user_id}:{org_id}", access_token)

        return {"message": "HubSpot connected successfully!"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
async def get_hubspot_credentials(user_id, org_id):
    r = redis.Redis()
    access_token = r.get(f"hubspot:{user_id}:{org_id}")
    if not access_token:
        raise Exception("No credentials found")
    return access_token.decode()


async def create_integration_item_metadata_object(response_json):
    items = []
    for contact in response_json.get("results", []):
        props = contact.get("properties", {})
        items.append({
            "id": contact.get("id"),
            "type": "contact",
            "name": props.get("firstname", "") + " " + props.get("lastname", ""),
            "email": props.get("email", ""),
            "extra_params": props
        })
    return items


async def get_items_hubspot(credentials):
    url = "https://api.hubapi.com/crm/v3/objects/contacts"
    headers = {
        "Authorization": f"Bearer {credentials}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []

    response_json = response.json()
    return await create_integration_item_metadata_object(response_json)