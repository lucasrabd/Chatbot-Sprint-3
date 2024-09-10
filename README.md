# Chatbot-Sprint-3

## Descrição
Este projeto implementa um chatbot simples utilizando Python e Flask. Ele pode ser utilizado para responder perguntas frequentes definidas em um arquivo JSON. O front-end é renderizado utilizando templates HTML e recursos estáticos.

## Índice
- Instalação
- Uso
- Documentação da API
- Testes
- Contribuição
- Licença
- Autores

## Instalação
Para rodar este projeto localmente, siga os seguintes passos:

### Pré-requisitos
- Python 3.x
- Pip (gerenciador de pacotes do Python)

### Passos para instalação:

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse o diretório do projeto:

```bash
cd Chatbot-Sprint-3
```

3. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows use venv\Scripts\activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Execute a aplicação:

```bash
python app.py
```

6. Acesse o projeto no navegador:

Abra o navegador e vá para `http://localhost:5000`.

## Uso
Após iniciar o projeto, o chatbot estará disponível para interação. Você pode inserir perguntas diretamente na interface da web, e o chatbot responderá com base nas respostas definidas no arquivo `faq.json`.

### Exemplo de Perguntas e Respostas

- **Pergunta:** "Qual o horário de atendimento?"
- **Resposta:** "Nosso horário de atendimento é de segunda a sexta, das 9h às 18h."

## Documentação da API
A API possui os seguintes endpoints:

- **GET /faq**: Retorna todas as perguntas e respostas.
- **POST /faq**: Adiciona uma nova pergunta e resposta.

### Exemplo de requisição para adicionar uma nova pergunta:

```bash
curl -X POST http://localhost:5000/faq -H "Content-Type: application/json" -d '{"pergunta": "Qual é o número de suporte?", "resposta": "Você pode nos contatar pelo número 0800-123-456."}'
```

## Testes
Para rodar os testes, utilize o comando:

```bash
python -m unittest discover
```


## Autores
- **Lucas Carabolad Bob** - [lucasrabd](https://github.com/lucasrabd)

---

