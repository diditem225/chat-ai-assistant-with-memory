from flask import Flask, render_template, request, jsonify, Response
from langchain_groq import ChatGroq
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

conversations = {}

PERSONAS = {
    "travel": {
        "name": "Travel Assistant",
        "system": "You are a helpful travel assistant who suggests budget-friendly trips. Always ask about budget and preferences. Keep responses short and friendly."
    },
    "grammar": {
        "name": "Grammar Teacher",
        "system": "You are a strict grammar teacher who corrects every mistake. Point out errors politely and explain the correct form. Be encouraging but thorough."
    },
    "tutor": {
        "name": "Math Tutor",
        "system": "You are a patient math tutor. When students ask questions, give a short explanation followed by one clear example. Encourage them to try solving problems."
    },
    "chef": {
        "name": "Chef Assistant",
        "system": "You are a professional chef assistant. Help with recipes, cooking tips, and meal planning. Always consider dietary restrictions and skill level."
    }
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/personas', methods=['GET'])
def get_personas():
    return jsonify({
        "personas": [
            {"id": key, "name": value["name"]}
            for key, value in PERSONAS.items()
        ]
    })


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    persona_id = data.get('persona', 'travel')
    session_id = data.get('session_id', 'default')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    if session_id not in conversations:
        conversations[session_id] = []
    
    persona = PERSONAS.get(persona_id, PERSONAS['travel'])
    
    messages = [{"role": "system", "content": persona["system"]}]
    messages.extend(conversations[session_id])
    messages.append({"role": "user", "content": user_message})
    
    def generate():
        try:
            full_response = ""
            
            for chunk in llm.stream(messages):
                if chunk.content:
                    full_response += chunk.content
                    yield f"data: {json.dumps({'content': chunk.content})}\n\n"
            
            conversations[session_id].append({"role": "user", "content": user_message})
            conversations[session_id].append({"role": "assistant", "content": full_response})
            
            yield f"data: {json.dumps({'done': True})}\n\n"
            
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
    
    return Response(generate(), mimetype='text/event-stream')


@app.route('/clear', methods=['POST'])
def clear_memory():
    data = request.json
    session_id = data.get('session_id', 'default')
    
    if session_id in conversations:
        conversations[session_id] = []
    
    return jsonify({'success': True})


@app.route('/history', methods=['POST'])
def get_history():
    data = request.json
    session_id = data.get('session_id', 'default')
    
    history = conversations.get(session_id, [])
    return jsonify({'history': history})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
