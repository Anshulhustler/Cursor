import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "YOUR_OPENAI_KEY"),
    temperature=0
)

def review_node(state):
    code = state.get("generated_code", "")

    prompt = f"""
    Review this code.
    Find:
    - bugs
    - security issues
    - bad practices

    Code:
    {code}
    
    IMPORTANT: The very last line of your response MUST be exactly either "PASS" or "FAIL". 
    Output "FAIL" if there are any bugs, security issues, or bad practices. Otherwise, output "PASS".
    """

    response = llm.invoke(prompt)
    feedback = response.content

    state["review_feedback"] = feedback
    
    lines = feedback.strip().split('\n')
    status = lines[-1].strip() if lines else "FAIL"
    
    if "PASS" in status.upper():
        state["review_status"] = "PASS"
    else:
        state["review_status"] = "FAIL"
        state["retry_count"] = state.get("retry_count", 0) + 1

    return state