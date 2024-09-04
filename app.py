from flask import Flask, request, jsonify, render_template
from chatbot import ChatBot

app = Flask(__name__)

chatbot = ChatBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pergunta', methods=['POST'])
def pergunta():
    data = request.get_json()
    question = data.get('question')
    response = chatbot.responder(question)
    return jsonify({"response": response})

@app.route('/sugestoes', methods=['POST'])
def sugestoes():
    data = request.get_json()
    user_input = data.get('user_input')
    suggestions = chatbot.sugerir_perguntas(user_input)
    return jsonify({"suggestions": suggestions})

if __name__ == '__main__':
    app.run(debug=True)
