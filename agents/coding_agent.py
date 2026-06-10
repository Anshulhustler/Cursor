import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "YOUR_OPENAI_KEY"),
    temperature=0
)

def coding_node(state):
    plan = state.get("plan", [])
    context = state.get("retrieved_context", "")

    prompt = f"""
    You are senior software engineer.
    Use this context:
    {context}

    Follow this plan:
    {plan}

    Generate production-grade Python code.
    """

    response = llm.invoke(prompt)

    state["generated_code"] = response.content

    return state