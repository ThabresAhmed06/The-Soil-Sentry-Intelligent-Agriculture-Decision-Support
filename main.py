from agent.agent import agent

while True:
    query = input("\nAsk: ")
    result = agent(query)
    print("\nAI:", result)