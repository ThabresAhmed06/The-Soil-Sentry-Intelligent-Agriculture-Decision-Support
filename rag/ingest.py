import os
from datasets import load_dataset
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# 🔥 STEP 1: Load Knowledge Sources [cite: 13]
documents = []

# Load HuggingFace Dataset 
print("Loading HuggingFace dataset...")
dataset = load_dataset("Mahesh2841/Agriculture")
for row in dataset["train"]:
    content = f"Question: {row['input']}\nAnswer: {row['response']}"
    documents.append(Document(page_content=content))

# Load Local Documents (e.g., agriculture.txt) 
local_file = "docs/agriculture.txt"
if os.path.exists(local_file):
    loader = TextLoader(local_file, encoding='utf-8')
    documents.extend(loader.load())
    print(f"✅ Loaded {local_file}")

# 🔥 STEP 2: Preprocessing & Chunking [cite: 14]
# Recursive splitter is better for farming guidelines/reasoning
splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=70)
docs = splitter.split_documents(documents)

# 🔥 STEP 3: Embeddings & Vector Store 
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma.from_documents(
    docs, 
    embeddings, 
    persist_directory="vectorstore"
)
print(f"🔥 Successfully indexed {len(docs)} chunks into Vector DB.")