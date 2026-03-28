import sqlite3
import pandas as pd
from datasets import load_dataset
import numpy as np
import os

# Load Data
print("Fetching Data...")
dataset = load_dataset("Mahesh2841/Agriculture")
df = pd.DataFrame(dataset["train"])

# CLEANING: Rename columns so SQL can find them
df = df.rename(columns={"input": "crop_name", "response": "details"})

# DATA SEEDING: Ensure 'yield' is a FLOAT (Number) so we can sort it
df['yield'] = np.random.uniform(10.0, 95.0, size=len(df))
df['water_usage'] = np.random.randint(100, 1000, size=len(df))
df['season'] = np.random.choice(['Kharif', 'Rabi', 'Summer'], size=len(df))

# Save to DB
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "database", "agri.db")
os.makedirs(os.path.dirname(db_path), exist_ok=True)

conn = sqlite3.connect(db_path)
# if_exists="replace" is key to clearing old data!
df.to_sql("agriculture", conn, if_exists="replace", index=True, index_label="id")
conn.close()

print(f"✅ Success! Created {len(df)} rows with numeric 'yield' column.")