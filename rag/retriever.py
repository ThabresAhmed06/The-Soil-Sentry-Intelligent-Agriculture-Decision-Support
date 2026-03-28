from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="vectorstore", embedding_function=embeddings)
llm = ChatOpenAI(model="gpt-4.1-nano", api_key="sk-QK5vbrlNoAVpUMqaeWzMDw", base_url="https://apidev.navigatelabsai.com")

def rag_query(query):
    # Increase k=5 to pull more relevant data from documents [cite: 16]
    docs = db.similarity_search(query, k=5)
    context = "\n".join([doc.page_content for doc in docs])

    # Improved prompt for better answer generation [cite: 50]
    prompt = f"""
    Use the following agricultural context to answer the question. 
    If the context doesn't have the exact answer, use it as a guideline to provide a helpful response.

    Context:
    {context}

    Question: {query}
    """
    return llm.invoke(prompt).content