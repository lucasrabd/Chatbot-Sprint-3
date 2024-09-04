import json

class ChatBot:
    def __init__(self):
        # Carregar as perguntas frequentes do arquivo JSON
        with open('faq.json', 'r') as f:
            self.faq_data = json.load(f)

    def responder(self, pergunta):
        # Procurar a pergunta na lista de FAQs
        for faq in self.faq_data['faq']:
            if pergunta.lower() in faq['question'].lower():
                return faq['answer']
        # Resposta padrão se a pergunta não for encontrada
        return "Desculpe, não consegui encontrar uma resposta para sua pergunta."

    def sugerir_perguntas(self, user_input):
        # Sugerir perguntas com base no que o usuário começou a digitar
        suggestions = []
        for faq in self.faq_data['faq']:
            if user_input.lower() in faq['question'].lower():
                suggestions.append(faq['question'])
        return suggestions
