from fastapi import FastAPI
from pydantic import BaseModel

from backend.kubernetes import (
    get_failed_pod,
    describe_pod
)

app = FastAPI()


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Welcome to Kubernetes AI Troubleshooting Bot 🚀"}


@app.post("/analyze")
def analyze(data: Question):

    pod = get_failed_pod()

    if not pod:
        return {
            "status": "success",
            "message": "No failed pods found."
        }

    details = describe_pod(pod)

    return {
        "question": data.question,
        "failed_pod": pod,
        "details": details
    }
