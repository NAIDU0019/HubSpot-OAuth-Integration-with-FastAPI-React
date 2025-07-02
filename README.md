# 🚀 HubSpot OAuth Integration with FastAPI & React

This project is a full-stack OAuth integration system that connects with the **HubSpot API** to fetch CRM contacts using `OAuth 2.0`. It was built as part of a technical assessment for **VectorShift (YC S23)**.

---

## 🌟 Features

- 🔐 HubSpot OAuth 2.0 Authorization Flow  
- 🧠 Access token management using Redis (Memurai on Windows)  
- 📩 Fetch and display contacts from HubSpot CRM  
- ⚡ Built with **FastAPI** (Python) & **React.js** (JavaScript)  
- 💡 UI with Material-UI (MUI), clean design and interactive controls  
- ✅ Supports connection, load data, and clear actions

---

## 📦 Tech Stack

| Layer        | Technologies                           |
|--------------|----------------------------------------|
| Frontend     | React.js, Material UI, Axios           |
| Backend      | FastAPI, Uvicorn, Redis (via Memurai)  |
| Authentication | OAuth 2.0 (HubSpot)                  |
| Storage      | Redis (Token store)                    |
| Language     | Python, JavaScript                     |

---

## 🖼️ Screenshots

| Connect with HubSpot | Loaded CRM Contacts |
|----------------------|---------------------|
| https://www.loom.com/share/04d6dabd03ed44e4a21842afdef7857f?sid=beccf396-5bef-44c1-bf10-c97e1c2eb941 |

---

## 🔧 Local Setup

### 1. 📁 Clone the Repository

```bash
git clone https://github.com/yourusername/hubspot-oauth-integration.git
cd hubspot-oauth-integration
### 2. ⚙️ Backend Setup
```bash
cd backend
python -m venv env
# On macOS/Linux
source env/bin/activate
# On Windows
env\Scripts\activate

pip install -r requirements.txt

Create a .env file inside /backend/:
```bash
HUBSPOT_CLIENT_ID=your_client_id
HUBSPOT_CLIENT_SECRET=your_client_secret
HUBSPOT_REDIRECT_URI=http://localhost:8000/integrations/hubspot/oauth2callback

✅ Required HubSpot Scopes (during app creation):
```bash
crm.objects.contacts.read crm.objects.companies.read crm.objects.deals.read oauth


3. 🧠 Start Redis (Memurai on Windows)
memurai

4. 🚀 Start Backend
```bash
uvicorn main:app --reload

5. 💻 Frontend Setup
```bash
cd ../frontend
npm install
npm run dev

🌐 Usage
Navigate to http://localhost:3000

Select HubSpot from the integration dropdown

Click Connect → you'll be redirected to HubSpot's OAuth page

Complete authorization and return to your app

Click Load Data → contacts from HubSpot will appear

Click Clear Data to reset the state
```bash
hubspot-oauth-integration/
│
├── backend/
│   ├── integrations/
│   │   ├── hubspot.py
│   │   ├── airtable.py
│   │   └── notion.py
│   ├── main.py
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── integrations/
│   │   │   ├── hubspot.js
│   │   │   ├── notion.js
│   │   │   └── airtable.js
│   │   └── components/
│   │       └── DataForm.js
│   └── package.json
│
└── README.md
🧠 Optional Enhancements
Extend to support Airtable and Notion using same flow

Add token refresh logic for expired tokens

Use persistent storage (e.g., PostgreSQL) instead of Redis

Add sorting/filtering/search to CRM data display

🎥 Demo (Screen Recording)
https://www.loom.com/share/04d6dabd03ed44e4a21842afdef7857f?sid=beccf396-5bef-44c1-bf10-c97e1c2eb941
🤝 Author
Rajappa Adabala
📧 rajuadabala1199@gmail.com

⚠️ Security Notes
❌ Never push real credentials or .env files to GitHub

✅ Add .env to .gitignore and use secrets for CI/CD in production

🔐 Protect your HubSpot Client Secret at all times

📜 License
This project is licensed under the MIT License.
Feel free to fork and extend!







