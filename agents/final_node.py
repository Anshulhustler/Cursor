def final_node(state):
    response = {
        "plan": state.get("plan", []),
        "retrieved_context": state.get("retrieved_context", ""),
        "generated_code": state.get("generated_code", ""),
        "review_feedback": state.get("review_feedback", ""),
        "test_results": state.get("test_results", ""),
        "review_status": state.get("review_status", ""),
        "retry_count": state.get("retry_count", 0)
    }

    state["final_response"] = response

    return state