from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

persona = "You are a helpful travel assistant who suggests budget-friendly trips."

memory = []


print("AI Travel Assistant - Type 'quit' to exit\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'quit':
        break
    
    messages = [{"role": "system", "content": persona}]
    messages.extend(memory)
    messages.append({"role": "user", "content": user_input})
    
    response = llm.invoke(messages)
    
    print(f"AI: {response.content}\n")
    
    memory.append({"role": "user", "content": user_input})
    memory.append({"role": "assistant", "content": response.content})

print("Goodbye!")
