from fastapi import FastAPI, Depends
from pydantic import BaseModel
import os
from workflows.graph import app

api = FastAPI(title="Coding Multi-Agent API")

class GenerateRequest(BaseModel):
    user_request: str
    api_key: str | None = None

@api.post("/generate")
def generate_code(request: GenerateRequest):
    if request.api_key:
        os.environ["OPENAI_API_KEY"] = request.api_key

    initial_state = {
        "user_request": request.user_request,
        "plan": [],
        "retrieved_context": "",
        "generated_code": "",
        "review_feedback": "",
        "test_results": "",
        "final_response": "",
        "review_status": "",
        "retry_count": 0,
        "memory_logs": []
    }

    result = app.invoke(initial_state)

    return {
        "final_response": result.get("final_response"),
        "retry_count": result.get("retry_count", 0)
    }