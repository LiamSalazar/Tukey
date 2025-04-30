nombres = [
    "Juan", "María", "Carlos", "Laura", "Pedro", "Ana", "Luis", "Sofía", "Miguel", "Elena",
    "Jorge", "Paula", "Andrés", "Valeria", "Raúl", "Gabriela", "Esteban", "Marta", "Felipe", "Camila",
    "Ricardo", "Beatriz", "Daniel", "Patricia", "Fernando", "Rosa", "Héctor", "Clara", "Alberto", "Diana",
    "Emilio", "Verónica", "Roberto", "Isabel", "Manuel", "Lucía", "Gonzalo", "Teresa", "Ramón", "Natalia",
    "Victor", "Susana", "Oscar", "Jimena", "Diego", "Alicia", "Samuel", "Lorena", "Pablo", "Julia"
]
generos = [
    "M", "F", "M", "F", "M", "F", "M", "F", "M", "F",
    "M", "F", "M", "F", "M", "F", "M", "F", "M", "F",
    "M", "F", "M", "F", "M", "F", "M", "F", "M", "F",
    "M", "F", "M", "F", "M", "F", "M", "F", "M", "F",
    "M", "F", "M", "F", "M", "F", "M", "F", "M", "F"
]
edades_actuales = [
    25, 50, 34, 40, 60, 70, 45, 55, 80, 90,
    30, 48, 37, 42, 65, 75, 50, 60, 85, 95,
    28, 53, 32, 47, 58, 67, 40, 52, 76, 88,
    22, 44, 36, 41, 63, 72, 46, 57, 78, 89,
    27, 49, 31, 43, 59, 68, 39, 51, 77, 87
]
enfermedades = [
    "No", "Sí", "No", "No", "Sí", "No", "Sí", "No", "No", "Sí",
    "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí",
    "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí",
    "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí",
    "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí"
]

nombresOrdenados = []
edadesOrdenadas = sorted(edades_actuales)

def ordenaNombres(edades, nombres):
    for edad in edadesOrdenadas:
        if edad in edades:
            nombresOrdenados.append(nombres[edades.index(edad)])

def imprimirNombreEdad(edadesOrdenadas, nombresOrdenados):
    for i in range(len(edadesOrdenadas)):
        print(f"Nombre: {nombresOrdenados[i]}, Edad: {edadesOrdenadas[i]}")

ordenaNombres(edades_actuales,nombres)
#print(nombresOrdenados)
#print(sorted(edades_actuales))
imprimirNombreEdad(edadesOrdenadas,nombresOrdenados)