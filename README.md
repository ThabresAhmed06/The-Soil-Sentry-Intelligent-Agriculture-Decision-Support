# AgriIntel: Autonomous Hybrid Agriculture Agent
### Multi-Tool Reasoning | RAG | Text-to-SQL | LLM Orchestration

Project Overview
AgriIntel is a sophisticated AI solution designed to handle the dual nature of agricultural data. Modern farming intelligence is often siloed between unstructured knowledge (research papers, advice) and structured data (yield metrics, seasonal statistics).

This project solves the "Data Silo" problem by implementing a Multi-Tool Agentic Framework. The system acts as a digital agronomist that intelligently distinguishes between a request for advice and a request for statistical analysis, executing the appropriate logic in real-time.
## Key Engineering Features
Autonomous Intent Routing: Implemented a "Gatekeeper" logic to solve RAG-Bias, ensuring numeric queries (e.g., "Top 5 crops") are routed to SQL while advisory queries remain in the RAG pipeline.

Dynamic Text-to-SQL: Converts natural language into executable SQLite queries (aggregations, filters, and joins) using the Mahesh2841/Agriculture dataset.

Vector Search Optimization: Uses all-MiniLM-L6-v2 embeddings and ChromaDB to perform semantic search over thousands of agricultural topics.

Synthetic Data Augmentation: Enriched the base HuggingFace dataset with numeric features (yield, water_usage) to demonstrate full analytical capabilities.
## Tech Stack
- **LLM**: GPT-4o-mini 
- **Orchestration**: LangChain 
- **Vector Database**: ChromaDB 
- **Structured Database**: SQLite
- **Interface**: Gradio

## Project Architecture
```text
AgriAI-Project/
├── app.py            # Master file (Agent, Tools, and UI)
├── database/         # SQLite storage (agri.db)
├── docs/             # Knowledge base (agriculture.txt)
├── requirements.txt  # Project dependencies
└── verify_data.py    # Direct SQL verification script
```
## Dataset Attribution
This project utilizes the Mahesh2841/Agriculture dataset for both structured analysis and knowledge retrieval. The system is designed to handle the unique challenge where the input field contains diverse agricultural topics and questions.
