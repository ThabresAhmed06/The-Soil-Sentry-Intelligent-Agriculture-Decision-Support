import gradio as gr
from agent.agent import agent

def chat(user_input, history):
    """
    Simulates the AI Agent workflow: 
    Intent Understanding -> Tool Selection (RAG/SQL) -> Final Response
    """
    # The agent function handles the logic of selecting the appropriate tool [cite: 49]
    response = agent(user_input)

    # Producing final intelligent response based on retrieved knowledge or data [cite: 50]
    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": response})

    return "", history, history

# Setting up the Blocks interface for the Agriculture Intelligence System 
with gr.Blocks() as demo:

    gr.Markdown("""
    # 🌾 AgriAI Intelligence System
    ### AI-powered Agriculture Assistant (RAG + SQL + Agent)
    """)
    
    gr.Markdown("""
    **Capabilities:**
    - **RAG:** Knowledge retrieval for crops, soil, and irrigation[cite: 16].
    - **SQL:** Structured data analysis for yields and water usage[cite: 21].
    """)

    chatbot = gr.Chatbot(height=450)

    with gr.Row():
        user_input = gr.Textbox(
            placeholder="Ask about crops, soil, irrigation, or dataset statistics...",
            scale=4
        )
        send_btn = gr.Button("Send", scale=1)

    clear_btn = gr.Button("Clear Chat")

    # Persistent state to maintain context for RAG or multi-turn reasoning 
    state = gr.State([])

    # Event handlers for Agent execution [cite: 52]
    send_btn.click(
        chat,
        inputs=[user_input, state],
        outputs=[user_input, chatbot, state]
    )

    user_input.submit(
        chat,
        inputs=[user_input, state],
        outputs=[user_input, chatbot, state]
    )

    clear_btn.click(
        lambda: (None, [], []),
        outputs=[user_input, chatbot, state]
    )

if __name__ == "__main__":
    # Launching with the Soft theme as initially configured
    demo.launch(theme=gr.themes.Soft())