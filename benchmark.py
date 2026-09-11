import random
import time

numeros = [random.randint(1, 10000) for _ in range(1000)]

inicio = time.time()

for i in range(len(numeros)):
    for j in range(len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

fim = time.time()

print("Bubble Sort:", fim - inicio)