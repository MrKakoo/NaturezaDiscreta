
def realizaroperacao(conj1, conj2, operacao):
    if operacao == 'U':
        resultado = conj1 | conj2
        nome_operacao = 'União'
    elif operacao == 'I':
        resultado = conj1 & conj2
        nome_operacao = 'Interseção'
    elif operacao == 'D':
        resultado = conj1 - conj2
        nome_operacao = 'Diferença'
    elif operacao == 'C':
        resultado = {(a, b) for a in conj1 for b in conj2}
        nome_operacao = 'Produto Cartesiano'
    else:
        resultado, nome_operacao = set(), 'Operação desconhecida'

    print(f'{nome_operacao}:\n Conjunto 1: {conj1}\n Conjunto 2: {conj2}\n Resultado: {resultado}')
#Aqui embaixo bote o arquivo que você quer usar 
with open('NatuDiscretaTDE1.3.txt', 'r') as arquivo:
    linhas = [linha.strip() for linha in arquivo.readlines()]

num_operacoes = int(linhas[0])
indice = 1

for _ in range(num_operacoes):
    operacao = linhas[indice]
    conj1 = set(linhas[indice + 1].split(','))
    conj2 = set(linhas[indice + 2].split(','))
    realizaroperacao(conj1, conj2, operacao)
    indice += 3

