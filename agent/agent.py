from langchain_openai import ChatOpenAI
from rag.retriever import rag_query
from sql.query import run_sql_query

def agent(query):
    # USE YOUR REAL KEY HERE
    llm = ChatOpenAI(
        model="gpt-4.1-nano",
        api_key="sk-QK5vbrlNoAVpUMqaeWzMDw", 
        base_url="https://apidev.navigatelabsai.com"
    )
    # 1. Force SQL for these specific "Top/Highest" queries
    sql_keywords = ["top", "highest", "average", "yield", "count", "max"]
    if any(word in query.lower() for word in sql_keywords):
        intent = "SQL"
    else:
        intent = "RAG" # Default to RAG for advice

    if intent == "SQL":
        sql_gen_prompt = f"""
        Table: agriculture
        Columns: id, crop_name, details, yield, water_usage, season
        Note: The 'crop_name' column contains agricultural topics and questions.
        
        Task: Write a SQLite query for: {query}
        Example: SELECT crop_name, yield FROM agriculture ORDER BY yield DESC LIMIT 5;
        Return ONLY raw SQL.
        """
        sql_command = llm.invoke(sql_gen_prompt).content.strip().replace("```sql", "").replace("```", "")
        
        try:
            result = run_sql_query(sql_command)
            
            # THE FIX: Tell the LLM that 'crop_name' is the topic
            interpret_prompt = f"""
            The user asked: {query}
            The database returned these top topics and their yield scores: {result}
            
            Format this as a clean list. Example:
            1. Inter-cropping (Yield: 94.96)
            2. Potassium-based fertilizers (Yield: 94.96)
            ...
            """
            return llm.invoke(interpret_prompt).content
        except:
            return rag_query(query)
    else:
        return rag_query(query)