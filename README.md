# 🧠 AI Multi-Agent Project Generator

A minimal demo showing how multiple AI agents can collaborate to turn a high-level project brief into runnable code.
The system routes a text prompt to specialized sub-agents that generate **frontend** and **backend** scaffolds automatically.

---

## 🚀 Features

* 🤖 **Coordinator Agent** – Reads a natural-language brief and decides which sub-agents to activate
* 🎨 **Frontend Agent** – Produces React component stubs
* ⚙️ **Backend Agent** – Generates Express.js API scaffolding
* 🧩 **FastAPI** interface – Clean REST endpoint (`/generate/`) for triggering generation
* 🪄 Auto-redirects `/` → `/docs` for quick testing in Swagger UI

---

## 🏗️ Folder Structure

```
ai_agent_project/
│
├── app.py
├── coordinator/
│   └── coordinator_agent.py
├── agents/
│   ├── frontend_agent.py
│   └── backend_agent.py
├── outputs/
│   ├── frontend_output/
│   └── backend_output/
└── requirements.txt
```

---

## ⚙️ Setup

### 1. Clone or unzip

```bash
cd ai_agent_project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI server

```bash
uvicorn app:app --reload
```

### 4. Open the docs

Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) → auto-redirects to `/docs`.

---

## 💬 Usage

### Endpoint

`POST /generate/`

### Example body

```json
{
  "brief": "Build a task management app with UI and API"
}
```

### Example responses

```json
{
  "result": "✅ React UI component generated at outputs/frontend_output/TaskManager.jsx | ✅ Express API generated at outputs/backend_output/server.js"
}
```

Generated files will appear in the `outputs/` folder.

---

## 🧩 Agent Logic

| Agent                | Responsibility                                                                    | Output                     |
| -------------------- | --------------------------------------------------------------------------------- | -------------------------- |
| **CoordinatorAgent** | Parses the brief, detects keywords (UI, API, database, etc.), and delegates tasks | —                          |
| **FrontendAgent**    | Generates React component (`TaskManager.jsx`)                                     | `outputs/frontend_output/` |
| **BackendAgent**     | Generates Express.js API (`server.js`)                                            | `outputs/backend_output/`  |

If the brief mentions both *UI* and *API*, both sub-agents are triggered.

---

## 🧠 Example Flow

1. User sends: `"Build a task management app with UI and API"`
2. Coordinator detects both keywords
3. Frontend agent creates `TaskManager.jsx`
4. Backend agent creates `server.js`
5. Response confirms both completed

---

## 💡 Optional Enhancements

* Integrate an LLM API to interpret complex project briefs
* Add a **file bundler** that zips outputs automatically
* Include **database model generation** via SQLAlchemy
* Extend frontend agent to support **Next.js / Tailwind** templates

---

## 📜 License

MIT — free for learning and experimentation.

---