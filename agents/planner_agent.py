import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "YOUR_OPENAI_KEY"),
    temperature=0
)

def planner_node(state):
    user_request = state.get("user_request", "")

    prompt = f"""
    Break this software task into steps:
    {user_request}
    """

    response = llm.invoke(prompt)

    state["plan"] = response.content.split("\n")

    return state