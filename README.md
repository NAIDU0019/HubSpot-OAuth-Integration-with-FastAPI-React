

---

# 🚀 HubSpot OAuth Integration with FastAPI & React

This project is a full-stack OAuth integration system that connects with the **HubSpot API** to fetch CRM contacts using `OAuth 2.0`. It was built as part of a technical assessment for **VectorShift (YC S23)**.

---

## 🌟 Features

* 🔐 HubSpot OAuth 2.0 Authorization Flow
* 🧠 Access token management using Redis (Memurai on Windows)
* 📩 Fetch and display contacts from HubSpot CRM
* ⚡ Built with **FastAPI** (Python) & **React.js** (JavaScript)
* 💡 UI with Material-UI (MUI), clean design and interactive controls
* ✅ Supports connection, data loading, and reset actions

---

## 📦 Tech Stack

| Layer          | Technologies                          |
| -------------- | ------------------------------------- |
| Frontend       | React.js, Material UI, Axios          |
| Backend        | FastAPI, Uvicorn, Redis (via Memurai) |
| Authentication | OAuth 2.0 (HubSpot)                   |
| Storage        | Redis (Token store)                   |
| Languages      | Python, JavaScript                    |

---

## 🖼️ Screenshots

| Video Preview | Loaded CRM Contacts |
|----------------------|---------------------|
| https://www.loom.com/share/04d6dabd03ed44e4a21842afdef7857f?sid=beccf396-5bef-44c1-bf10-c97e1c2eb941 |



---

## 🔧 Local Setup

### 1. 📁 Clone the Repository

```bash
git clone https://github.com/NAIDU0019/HubSpot-OAuth-Integration-with-FastAPI-React.git
cd HubSpot-OAuth-Integration-with-FastAPI-React
```

---

### 2. ⚙️ Backend Setup

```bash
cd backend
python -m venv env

# On macOS/Linux
source env/bin/activate

# On Windows
env\Scripts\activate

pip install -r requirements.txt
```

📄 Create a `.env` file inside `/backend/`:

```env
HUBSPOT_CLIENT_ID=your_client_id
HUBSPOT_CLIENT_SECRET=your_client_secret
HUBSPOT_REDIRECT_URI=http://localhost:8000/integrations/hubspot/oauth2callback
```

✅ Required HubSpot Scopes (during app creation):

```
crm.objects.contacts.read crm.objects.companies.read crm.objects.deals.read oauth
```

---

### 3. 🧠 Start Redis

> Using **Memurai** (Redis for Windows) or any local Redis server.

```bash
memurai
```

---

### 4. 🚀 Start Backend Server

```bash
uvicorn main:app --reload
```

---

### 5. 💻 Frontend Setup

```bash
cd ../frontend
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 🌐 Usage

1. Select **HubSpot** from the integrations dropdown.
2. Click **Connect** – you’ll be redirected to HubSpot’s OAuth page.
3. Authorize the app and return to your UI.
4. Click **Load Data** – CRM contacts will appear.
5. Click **Clear Data** to reset the state.

---

## 🗂️ Project Structure

```
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
```

---

## 🧠 Optional Enhancements

* Extend integration support to **Airtable** and **Notion**
* Add **token refresh** logic for long-lived sessions
* Use **persistent storage** (e.g., PostgreSQL) instead of Redis
* Add **filtering, sorting, and search** to the CRM UI

---

## 🤝 Author

**Rajappa Adabala**
📧 [rajuadabala1199@gmail.com](mailto:rajuadabala1199@gmail.com)

---

## ⚠️ Security Notes

* ❌ **Never push real credentials or `.env` files** to GitHub.
* ✅ Add `.env` to `.gitignore` and use GitHub secrets or CI/CD pipelines in production.
* 🔐 Protect your HubSpot credentials at all times.

---

## 📜 License

This project is licensed under the **MIT License**.
Feel free to fork, use, and extend!

---
