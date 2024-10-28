# Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
# a. Imprima o resultado da soma de todos os valores da matriz no terminal;
# b. E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;
import numpy as np

# a. Criando a matriz A  tamanho 10 x 10 com valores inteiros randômicos
A = np.random.randint(0, 100, size=(10, 10))  # Valores entre 0 e 99

# Imprimir a matriz A
print("Matriz A:")
print(A)

# Calcular e imprimir a soma de todos os valores da matriz A
soma_A = np.sum(A)
print("Soma de todos os valores da matriz A:", soma_A)

# b. Criando a  matriz B, onde cada item é o valor da matriz A * 3
B = A * 3

# Imprimir a matriz B
print("Matriz B (A * 3):")
print(B)