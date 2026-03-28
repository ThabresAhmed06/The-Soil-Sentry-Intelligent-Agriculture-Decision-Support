def run_sql_query(query):
    import sqlite3

    try:
        conn = sqlite3.connect("database/agri.db")
        cursor = conn.cursor()

        cursor.execute(query)
        results = cursor.fetchall()

        conn.close()
        return results

    except Exception as e:
        return f"SQL ERROR: {str(e)}"