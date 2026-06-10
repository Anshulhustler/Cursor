import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "YOUR_OPENAI_KEY"),
    temperature=0
)

def testing_node(state):
    code = state.get("generated_code", "")

    prompt = f"""
    You are a QA engineer. Review this code and write test cases for it.
    Also, summarize if the code looks robust enough for production.

    Code:
    {code}
    """

    response = llm.invoke(prompt)

    state["test_results"] = response.content

    return state
