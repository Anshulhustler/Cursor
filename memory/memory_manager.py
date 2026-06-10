def add_memory(state, message):

    state["memory_logs"].append(message)

    return state