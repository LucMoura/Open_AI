import tiktoken

modelo = "gpt-4"
codificador = tiktoken.encoding_for_model(modelo)
lista_tokens = codificador.encode("Você é um categorizador de produtos")

#print("Lista de Tokens:\n", lista_tokens)
#print("Quantos tokens temos:", len(lista_tokens))
print(f"O custo para o modelo {modelo} é de ${(len(lista_tokens)/1000) * 0.03}")

modelo = "gpt-3.5-turbo-1106"
codificador = tiktoken.encoding_for_model(modelo)
lista_tokens = codificador.encode("Você é um categorizador de produtos")

#print("Lista de Tokens:\n", lista_tokens)
#rint("Quantos tokens temos:", len(lista_tokens))
print(f"O custo para o modelo {modelo} é de ${(len(lista_tokens)/1000) * 0.001}")

print(f"O custo do GPT-4 é {0.03/0.001}x maior que o GPT-3.5-Turbo")