import json
from transformers import pipeline

class ChatBot:
    def __init__(self):
        # Carregar as perguntas frequentes do arquivo JSON
        with open('faq.json', 'r') as f:
            self.faq_data = json.load(f)
        
        # Criar um pipeline de NLP usando o modelo BERT
        self.nlp_model = pipeline('question-answering', model='distilbert-base-uncased', tokenizer='distilbert-base-uncased')

    def responder(self, pergunta):
        pergunta_lower = pergunta.lower()

        # Tentar encontrar uma correspondência exata ou parcial nas FAQs
        for faq in self.faq_data['faq']:
            if pergunta_lower in faq['question'].lower():  # Comparação case-insensitive e parcial
                return faq['answer']
        
        # Se não houver correspondência exata ou parcial, usar o modelo NLP
        melhor_resposta = None
        maior_score = 0
        
        for faq in self.faq_data['faq']:
            contexto = faq['question'] + " " + faq['answer']
            
            # Usar o modelo NLP para verificar qual FAQ é mais relevante
            resposta = self.nlp_model(question=pergunta, context=contexto)
            
            if resposta['score'] > maior_score:
                melhor_resposta = faq['answer']
                maior_score = resposta['score']
        
        # Retornar a melhor resposta encontrada ou uma resposta padrão
        if maior_score > 0.5:
            return melhor_resposta
        else:
            return "Desculpe, não consegui encontrar uma resposta para sua pergunta. Pode reformular ou tentar outra?"

    def sugerir_perguntas(self, texto):
        texto_lower = texto.lower()
        sugestoes = []

        # Procurar perguntas que correspondam parcialmente ao texto digitado
        for faq in self.faq_data['faq']:
            if texto_lower in faq['question'].lower():
                sugestoes.append(faq['question'])

        return sugestoes
