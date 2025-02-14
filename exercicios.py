#### Exercicio 1: Verificação de qualidade
# Você está analisando um conjunto de dados de vendas e precisa garantir
# que todos os registros tenham valores positivos para 'quantidade' e 'preco'.
# Escreva um programa que verifique esses campos e imprima "Dados validos" se ambos
# forem positivos, ou "Dados invalidos" caso contrário.

quantidade = 10
preco = 20

if quantidade > 0 and preco > 0:
    print("Dados validos")
else:
    print("Dados invalidos")

#### Exercicio 2: Classificação de Dados Sensor
# Imagine que você está trabalhando com dados de sensores IoT.
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura
# como 'Baixa','Normal' ou 'Alta'. Considerando que:

