from fastapi import FastAPI
from pydantic import BaseModel
from coordinator.coordinator_agent import CoordinatorAgent

app = FastAPI(title="AI Agent Demo")
agent = CoordinatorAgent()

class BriefInput(BaseModel):
    brief: str

@app.post("/generate/")
def generate_project(data: BriefInput):
    result = agent.process_brief(data.brief)
    return {"result": result}

@app.get("/")
def root():
    return {"message": "AI Agent API is running. Visit /docs to try it out."}
