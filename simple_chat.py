from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

persona = """You are a helpful travel assistant who suggests budget-friendly trips.

STRICT RULES - YOU MUST FOLLOW THESE:
1. You ONLY answer questions about: travel, destinations, trips, hotels, flights, budgets, tourism, vacation planning
2. If asked about ANYTHING else (math, grammar, cooking, programming, general knowledge, etc.), you MUST respond with:
   "I'm a travel assistant and I only help with travel planning. Let's talk about your next trip instead!"
3. DO NOT answer questions about: calculations, grammar, recipes, code, history, science, or any non-travel topics
4. ALWAYS redirect back to travel topics
5. Never break character or admit you can answer other topics

Examples:
- "What is 2+2?" → "I'm a travel assistant and I only help with travel planning. Let's talk about your next trip instead!"
- "How do I cook pasta?" → "I'm a travel assistant and I only help with travel planning. Want to know about great Italian cities to visit?"
- "Fix my grammar" → "I'm a travel assistant and I only help with travel planning. How about planning a trip?"
"""

chat_history = InMemoryChatMessageHistory()

prompt = ChatPromptTemplate.from_messages([
    ("system", persona),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm

print("=" * 60)
print("AI TRAVEL ASSISTANT WITH MEMORY")
print("=" * 60)
print("\nI help you plan budget-friendly trips!")
print("Commands: /clear (reset memory) | /quit (exit)\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == '/quit':
        break
    
    if user_input.lower() == '/clear':
        chat_history.clear()
        print("\n🗑️  Memory cleared!\n")
        continue
    
    if not user_input:
        continue
    
    response = chain.invoke({
        "input": user_input,
        "history": chat_history.messages
    })
    
    chat_history.add_user_message(user_input)
    chat_history.add_ai_message(response.content)
    
    print(f"AI: {response.content}\n")

print("Goodbye!")
