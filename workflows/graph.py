from langgraph.graph import StateGraph

from workflows.state import AgentState
from workflows.router import review_router
from agents.supervisor_agent import supervisor_node
from agents.planner_agent import planner_node
from agents.rag_agent import rag_node
from agents.coding_agent import coding_node
from agents.review_agent import review_node
from agents.testing_agent import testing_node
from agents.final_node import final_node

graph = StateGraph(AgentState)

graph.add_node("supervisor", supervisor_node)
graph.add_node("planner", planner_node)
graph.add_node("rag", rag_node)
graph.add_node("coder", coding_node)
graph.add_node("review", review_node)
graph.add_node("tester", testing_node)
graph.add_node("final", final_node)

graph.add_edge("supervisor", "planner")
graph.add_edge("planner", "rag")
graph.add_edge("rag", "coder")
graph.add_edge("coder", "review")

graph.add_conditional_edges(
    "review",
    review_router,
    {
        "coder": "coder",
        "tester": "tester"
    }
)

graph.add_edge("tester", "final")

graph.set_entry_point("supervisor")

app = graph.compile()