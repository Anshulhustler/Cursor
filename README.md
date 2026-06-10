# Multi-Agent Code Generation Workflow

A production-ready multi-agent workflow built with **LangGraph**, **FastAPI**, and **OpenAI**, designed to generate, review, test, and finalize code through a structured agent pipeline.

## Features

* Multi-agent orchestration using LangGraph
* Automated planning and retrieval workflow
* Code generation with iterative review cycles
* Automatic testing and validation
* FastAPI endpoint for workflow execution
* Dockerized deployment
* Environment-based API key management
* Retry handling with configurable review loops

---

# Architecture

The workflow follows the execution graph below:

```text
Supervisor
    ↓
Planner
    ↓
RAG
    ↓
Coder
    ↓
Review
├── PASS → Tester → Final
└── FAIL → Coder (Max 2 Retries)
```

### Workflow Description

| Agent      | Responsibility                                          |
| ---------- | ------------------------------------------------------- |
| Supervisor | Coordinates workflow execution                          |
| Planner    | Breaks down user requirements into implementation steps |
| RAG        | Retrieves relevant context and reference information    |
| Coder      | Generates code based on the plan and retrieved context  |
| Review     | Evaluates generated code quality and correctness        |
| Tester     | Validates reviewed code before final delivery           |
| Final      | Produces final workflow output                          |

---

# Project Structure

```text
project/
│
├── agents/
│   ├── supervisor_agent.py
│   ├── planner_agent.py
│   ├── rag_agent.py
│   ├── coder_agent.py
│   ├── review_agent.py
│   └── testing_agent.py
│
├── workflows/
│   └── graph.py
│
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# Review & Retry Logic

The Review Agent evaluates generated code and returns one of:

```text
PASS
FAIL
```

### PASS Flow

```text
Review → Tester → Final
```

### FAIL Flow

```text
Review → Coder
```

Additional behavior:

* `retry_count` is incremented after every failed review.
* Failed generations are routed back to the Coder.
* Maximum retry limit: **2 attempts**.
* Workflow exits after successful review or retry exhaustion.

---

# FastAPI API

The workflow is exposed through a FastAPI server.

## Endpoint

### Generate Code

```http
POST /generate
```

### Request Body

```json
{
  "user_request": "Build a Redis caching utility function",
  "api_key": "YOUR_OPENAI_API_KEY"
}
```

### Parameters

| Field        | Type   | Required | Description                                                     |
| ------------ | ------ | -------- | --------------------------------------------------------------- |
| user_request | string | Yes      | User prompt describing the desired implementation               |
| api_key      | string | No       | OpenAI API key (optional if environment variable is configured) |

---

## Example Response

```json
{
  "graph_output": {
    "final_result": "...generated code..."
  },
  "retry_count": 0
}
```

### Response Fields

| Field        | Description                        |
| ------------ | ---------------------------------- |
| graph_output | Complete workflow output           |
| retry_count  | Number of review retries performed |

---

# Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

The workflow automatically reads the API key from:

```text
OPENAI_API_KEY
```

### Dynamic API Key Support

You may also provide the API key directly in the API request payload.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/multi-agent-workflow.git

cd multi-agent-workflow
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Locally

Start the FastAPI server:

```bash
uvicorn main:api --host 0.0.0.0 --port 8000
```

API documentation will be available at:

```text
http://localhost:8000/docs
```

---

# Docker Deployment

## Build and Run

```bash
docker-compose up --build
```

The application will be available at:

```text
http://localhost:8000
```

---

# Dependencies

Core dependencies include:

```text
fastapi
uvicorn
langgraph
openai
```

Additional workflow dependencies are listed in:

```text
requirements.txt
```

---

# Postman Testing

### Request

```http
POST http://localhost:8000/generate
```

### Body

```json
{
  "user_request": "Build a Redis caching utility function",
  "api_key": "YOUR_OPENAI_API_KEY"
}
```

### Notes

* `api_key` is optional if `OPENAI_API_KEY` is configured.
* The request executes the entire LangGraph workflow.
* Response includes generated artifacts and retry statistics.

---

# Deliverables

* ✅ Broken links fixed
* ✅ LangGraph workflow implemented
* ✅ Supervisor → Planner → RAG → Coder → Review → Tester → Final flow
* ✅ Review pass/fail routing
* ✅ Retry handling (maximum 2 retries)
* ✅ Testing Agent implementation
* ✅ FastAPI endpoint exposure
* ✅ Environment-based API key management
* ✅ Docker support
* ✅ Dependency updates
* ✅ Postman testing documentation

---

# Future Enhancements

* Human-in-the-loop approval
* Persistent workflow memory
* Multi-model support
* Agent observability and tracing
* Automated CI/CD integration
* Advanced test coverage reporting

---

# License

MIT License

Feel free to use, modify, and distribute this project.
