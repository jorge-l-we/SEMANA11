def calcular_temperatura_promedio(temperaturas):

    promedios = []
    for ciudad_temperaturas in temperaturas:
        promedio = sum(ciudad_temperaturas) / len(ciudad_temperaturas)
        promedios.append(promedio)
    return promedios

# Ejemplo de uso
datos_temperaturas = [
    [40, 32, 21, 17],  # Temperaturas de la ciudad 1 durante 4 semanas
    [15, 10, 14, 19],  # Temperaturas de la ciudad 2 durante 4 semanas
    [25, 29, 40, 17]   # Temperaturas de la ciudad 3 durante 4 semanas
]

promedios = calcular_temperatura_promedio(datos_temperaturas)
print(promedios)  # Salida esperada: [21.5, 15.5, 25.5]
