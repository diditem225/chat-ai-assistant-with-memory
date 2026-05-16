# AI Assistant with Persistent Memory and Persona Switching

A simple chatbot that remembers conversation history and can switch between different personas/roles.

## 🎯 Features

- **4 Different Personas:**
  - 🌍 Travel Assistant - Budget-friendly trip suggestions
  - 📝 Grammar Teacher - Corrects mistakes and explains
  - 🧮 Math Tutor - Patient explanations with examples
  - 👨‍🍳 Chef Assistant - Recipes and cooking tips

- **Persistent Memory:** Remembers entire conversation history
- **Persona Switching:** Change assistant role anytime
- **Clear Memory:** Reset conversation when needed
- **Streaming Responses:** See answers appear in real-time

## 🚀 Quick Start

```bash
cd 6
pip install -r requirements.txt
python app.py
```

Open: http://localhost:5000

## 📖 How It Works

### Step 1: System Message (Persona)
Each persona has a clear system message that defines its role:

```python
"travel": "You are a helpful travel assistant who suggests budget-friendly trips..."
"grammar": "You are a strict grammar teacher who corrects every mistake..."
```

### Step 2: Conversation Memory
The app stores all messages in a dictionary:

```python
conversations[session_id] = [
    {"role": "user", "content": "I want to visit Spain"},
    {"role": "assistant", "content": "Great! What's your budget?"},
    {"role": "user", "content": "800 euros"},
    ...
]
```

### Step 3: Context Awareness
When you send a new message, the assistant sees:
1. System message (persona)
2. All previous messages
3. Your new message

This allows it to remember and reference earlier parts of the conversation.

## 🧪 Test the Memory

Try this conversation with the Travel Assistant:

```
You: I want to visit Spain
Assistant: Great! Do you have a budget in mind?

You: Yes, around 800 euros
Assistant: [suggests trips within 800 euros]

You: What about something else in that budget?
Assistant: [remembers 800 euros and suggests alternatives]
```

## 📝 Demo Dialogue Examples

### Travel Assistant
```
User: I want to plan a trip to Europe
Assistant: Wonderful! What's your budget for this trip?

User: Around $1500
Assistant: Great! With $1500, you could visit Portugal or Poland for a week...

User: Tell me more about Portugal
Assistant: Portugal is perfect for your $1500 budget! Lisbon and Porto are affordable...

User: What about food costs there?
Assistant: In Portugal, you can eat well for $20-30 per day...
```

### Grammar Teacher
```
User: I goed to the store yesterday
Assistant: I notice an error! "Goed" should be "went". The past tense of "go" is irregular...

User: Oh right! I went to the store. Is that correct now?
Assistant: Perfect! Yes, "I went to the store" is correct...
```

## 🔧 Code Structure

### Backend (`app.py`)
- `PERSONAS` - Dictionary of all available personas
- `conversations` - Stores chat history per session
- `/chat` - Handles messages and streaming
- `/clear` - Resets memory
- `/personas` - Returns available personas

### Frontend (`index.html`)
- Persona selector buttons
- Chat interface with message history
- Streaming message display
- Clear memory button

## 💡 Key Concepts

1. **System Message** = Defines the assistant's role
2. **Conversation Buffer** = Stores all past messages
3. **Context Window** = All messages sent to LLM each time
4. **Session ID** = Unique identifier for each user's conversation

## 🎓 Learning Points

- How system messages control AI behavior
- How conversation memory works
- How to maintain context across multiple turns
- How to implement persona switching
- How streaming responses improve UX

## 🔄 What Happens When You Clear Memory?

- All previous messages are deleted
- Assistant starts fresh (no context)
- Persona stays the same
- Like starting a new conversation

## 📊 Memory Test Questions

1. **Did the assistant stay in its role?**
   - Yes, system message enforces consistent behavior

2. **Did it remember past details?**
   - Yes, all messages are in the conversation buffer

3. **What happens if memory is cleared?**
   - Assistant forgets everything, starts fresh

## 🚀 Try It Yourself!

1. Start with Travel Assistant
2. Ask about a trip
3. Mention your budget
4. Ask follow-up questions referencing your budget
5. Switch to Grammar Teacher
6. Make intentional grammar mistakes
7. See how it corrects and remembers context

Enjoy your AI assistant! 🎉
