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
    texto = data.get('texto', '')
    sugestoes = chatbot.sugerir_perguntas(texto)
    return jsonify({"sugestoes": sugestoes})

if __name__ == '__main__':
    app.run(debug=True)
