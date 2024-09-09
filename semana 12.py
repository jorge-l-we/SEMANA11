# Crear una matriz 3D para almacenar datos de temperaturas
temperaturas = [
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 9},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 28}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 39},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 30}
        ]
    ]
]

# Nombres de ciudades
ciudades = ["Quito", "Guayaquil"]

def calcular_promedios(temperaturas):
    promedios = []
    for ciudad in temperaturas:
        promedios_ciudad = []
        for semana in ciudad:
            suma_temperaturas = sum(dia["temp"] for dia in semana)
            promedio = suma_temperaturas / len(semana)
            promedios_ciudad.append(promedio)
        promedios.append(promedios_ciudad)
    return promedios

promedios = calcular_promedios(temperaturas)

for i, ciudad in enumerate(promedios):
    print(f"Ciudad {ciudades[i]}:")
    for j, promedio in enumerate(ciudad):
        print(f"  Semana {j+1}: {promedio:.2f}°C")
