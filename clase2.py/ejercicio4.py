import random
numeros = [random.randint(1, 100) for _ in range(10)]
promedio = sum(numeros) / len(numeros)
print("Números:", numeros)
print("Promedio:", promedio)
