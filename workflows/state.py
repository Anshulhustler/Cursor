from typing import TypedDict
from typing import List

class AgentState(TypedDict):
    user_request: str
    plan: List[str]
    retrieved_context: str
    generated_code: str
    review_feedback: str
    test_results: str
    final_response: str
    review_status: str
    retry_count: int
    memory_logs: List[str]