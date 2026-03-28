import sqlite3
import os

# 1. Connect to the DB
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database", "agri.db")

if not os.path.exists(db_path):
    print("❌ Error: Database file still missing. Run db_setup.py first!")
else:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 2. Check Top 5 Yields directly
    print("--- 🌾 Checking Top 5 Crops by Yield ---")
    try:
        query = "SELECT crop_name, yield FROM agriculture ORDER BY yield DESC LIMIT 5;"
        cursor.execute(query)
        results = cursor.fetchall()
        
        if not results:
            print("⚠️ Table exists but it is EMPTY.")
        for row in results:
            print(f"Crop: {row[0]:<20} | Yield: {row[1]:.2f}")
            
    except Exception as e:
        print(f"❌ SQL Error: {e}")
    
    conn.close()