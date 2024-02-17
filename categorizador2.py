from openai import OpenAI
from dotenv import load_dotenv
import os
#APENAS COLOQUE O CÓDIGO PARA FUNCIONAR
#Neste caso aqui você seleciona as categorias que deseja e depois coloca um produto
#Ai a própria IA dirá a qual classe ela pertence (caso tenha alguma)

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
versao = "gpt-3.5-turbo"

def categoriza_produto(nome_produto, lista_categorias_possiveis):
    prompt_sistema = f"""
        Você é um assistente de loja.
        Sua função é ajudar os clientes falando sobre o produto.
        
        # Lista de categorias válidas:
        {lista_categorias_possiveis.split(",")}
        
        
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
    
    resposta = cliente.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content":prompt_sistema
            },
            {
                "role" : "user",
                "content" : nome_produto
            }
            
        ],
        model=versao,
        temperature = 1,
        max_tokens=257,
    )
    
    return resposta.choices[0].message.content

categorias_validas = input("informe as categorias válidas, separando por vírgula: ")

while True:
    nome_produto = input("Digite o nome do produto:")
    texto_resposta = categoriza_produto(nome_produto,categorias_validas)
    print(texto_resposta)

    