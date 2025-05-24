import math

# Función para calcular el promedio
def promedio(numeros):
    return sum(numeros) / len(numeros)

# Función para calcular el promedio multiplicativo
def promedio_multiplicativo(numeros):
    producto = 1
    for num in numeros:
        producto *= num
    return producto ** (1 / len(numeros))

# Función para calcular potencia del mayor al menor
def potencia_mayor_menor(numeros):
    mayor = max(numeros)
    menor = min(numeros)
    return mayor ** menor

# Función para calcular la raíz cúbica del menor número
def raiz_cubica_menor(numeros):
    menor = min(numeros)
    return menor ** (1/3) if menor >= 0 else -(-menor) ** (1/3)

# Solicitar 5 números reales
numeros = []
for i in range(5):
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# Resultados
print(f"\nPromedio: {promedio(numeros):.2f}")
print(f"Promedio multiplicativo: {promedio_multiplicativo(numeros):.2f}")
print(f"Potencia del mayor elevado al menor: {potencia_mayor_menor(numeros):.2f}")
print(f"Raíz cúbica del menor número: {raiz_cubica_menor(numeros):.2f}")