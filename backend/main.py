from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()  # this should be at the top of hubspot.py or main.py

client_id = os.getenv("HUBSPOT_CLIENT_ID")
client_secret = os.getenv("HUBSPOT_CLIENT_SECRET")
# Integration imports
from integrations.airtable import (
    authorize_airtable,
    get_items_airtable,
    oauth2callback_airtable,
    get_airtable_credentials
)

from integrations.notion import (
    authorize_notion,
    get_items_notion,
    oauth2callback_notion,
    get_notion_credentials
)

from integrations.hubspot import (
    authorize_hubspot,
    get_items_hubspot,
    oauth2callback_hubspot,
    get_hubspot_credentials
)

app = FastAPI()

# Allow CORS from frontend
origins = [
    "http://localhost:3000",  # React frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

# -----------------------
# Airtable Integration
# -----------------------

@app.post('/integrations/airtable/authorize')
async def authorize_airtable_integration(user_id: str = Form(...), org_id: str = Form(...)):
    return await authorize_airtable(user_id, org_id)

@app.get('/integrations/airtable/oauth2callback')
async def oauth2callback_airtable_integration(request: Request):
    return await oauth2callback_airtable(request)

@app.post('/integrations/airtable/credentials')
async def get_airtable_credentials_integration(user_id: str = Form(...), org_id: str = Form(...)):
    return await get_airtable_credentials(user_id, org_id)

@app.post('/integrations/airtable/load')
async def get_airtable_items(credentials: str = Form(...)):
    return await get_items_airtable(credentials)

# -----------------------
# Notion Integration
# -----------------------

@app.post('/integrations/notion/authorize')
async def authorize_notion_integration(user_id: str = Form(...), org_id: str = Form(...)):
    return await authorize_notion(user_id, org_id)

@app.get('/integrations/notion/oauth2callback')
async def oauth2callback_notion_integration(request: Request):
    return await oauth2callback_notion(request)

@app.post('/integrations/notion/credentials')
async def get_notion_credentials_integration(user_id: str = Form(...), org_id: str = Form(...)):
    return await get_notion_credentials(user_id, org_id)

@app.post('/integrations/notion/load')
async def get_notion_items(credentials: str = Form(...)):
    return await get_items_notion(credentials)

# -----------------------
# HubSpot Integration
# -----------------------

@app.post('/integrations/hubspot/authorize')
async def authorize_hubspot_integration(user_id: str = Form(...), org_id: str = Form(...)):
    return await authorize_hubspot(user_id, org_id)

@app.get('/integrations/hubspot/oauth2callback')
async def oauth2callback_hubspot_integration(request: Request):
    return await oauth2callback_hubspot(request)

@app.post('/integrations/hubspot/credentials')
async def get_hubspot_credentials_integration(user_id: str = Form(...), org_id: str = Form(...)):
    return await get_hubspot_credentials(user_id, org_id)

@app.post('/integrations/hubspot/load')
async def get_hubspot_items_integration(credentials: str = Form(...)):
    return await get_items_hubspot(credentials)

@app.post('/integrations/hubspot/get_hubspot_items')
async def load_slack_data_integration(credentials: str = Form(...)):
    return await get_items_hubspot(credentials)

