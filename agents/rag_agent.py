import os
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

documents = [
    "Use Redis for fast caching.",
    "FastAPI supports async APIs.",
    "Kafka handles event streaming."
]

vectorstore = Chroma.from_texts(
    texts=documents,
    embedding=OpenAIEmbeddings(
        api_key=os.environ.get("OPENAI_API_KEY", "YOUR_OPENAI_KEY")
    )
)

retriever = vectorstore.as_retriever()

def rag_node(state):
    query = state.get("user_request", "")

    docs = retriever.invoke(query)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    state["retrieved_context"] = context

    return state