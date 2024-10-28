# Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
# números repetidos no vetor VET e em que posições se encontram.
vet = [17,34,51,86,86,102,119,136,69,666]
repetidos = []
for i in range(len(vet)):
    for j in range(i+1, len(vet)):
        if vet[i] == vet[j]:
            repetidos.append(vet[i])
            break
            print (repetidos)
            
numero_a_procurar = repetidos
posicoes = [index for index, valor in enumerate(vet) if valor == numero_a_procurar]
print("As posições do número", numero_a_procurar, "são:", posicoes)
            