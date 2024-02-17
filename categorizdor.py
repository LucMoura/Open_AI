from openai import OpenAI
from dotenv import load_dotenv
import os
#APENAS COLOQUE O CÓDIGO PARA FUNCIONAR

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
versao = "gpt-3.5-turbo"

prompt_sistema = """
    Você é um assistente de loja.
    Sua função é ajudar os clientes falando sobre o produto.
    
    # Lista de categorias válidas:
    - Ferramenta
    - Sistema de Admissão
    - Sistema de transmissão
    - Parte Elétrica
    - Freios
    - Sistema de escape
    - Fluidos
    - Sistema de ignição
    
    
    
    # Formato de Saída
    Olá, sou o mini_luc.
    Posso ver que a peça que você pediu foi:
    Produto: Nome do produto
    Categoria: Apresente a categoria do produto
    
    # Exemplo de Saída
    Olá, sou o mini_luc.
    Posso ver que a peça que você pediu foi:
    Produto: Disco de freio
    Categoria: Freios
    
"""

prompt_usuario = input("Olá!\nMe diga qual produto que você quer saber a categoria:\n")

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content":prompt_sistema
        },
        {
            "role" : "user",
            "content" : prompt_usuario
        }
        
    ],
    model=versao,
    temperature = 1,
    max_tokens=257,

)

print(resposta.choices[0].message.content)
    