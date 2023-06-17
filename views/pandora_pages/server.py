import openai
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


def get_answer(question):
    prompt= f"""Responda igual um pirata a pergunta a seguir: {question}"""
    return (get_completion)


def ask_question():
    question = request.json['question']
    # Aqui você pode processar a pergunta e retornar uma resposta
    # Vamos supor que você tenha uma função chamada `get_answer` que recebe a pergunta e retorna a resposta
    answer = get_answer(question)
    return jsonify({'answer': answer})

app =  Flask(__name__)
@app.route('/api/ask', method=['POST'])

if __name__ == '__main__':
    app.run()
