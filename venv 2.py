carreras = ("Ingeniería de Software", "Contabilidad", "Derecho")

# Datos iniciales (Tuplas dentro de una lista)
personas = [
    ("Juan", "Pérez", 38, 0),
    ("Carlos", "Santana", 29, 1),
    ("Raúl", "Sosa", 19, 2)
]

estudiantes = []

# Cambiamos "para i en rango" por "for i in range"
# He ajustado el rango a 2 para que la prueba sea rápida, puedes volver a 5 si gustas.
for i in range(2):
    print(f"\n--- Registro del estudiante {i+1} ---")
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingrese apellido: ")
    edad = int(input("Ingrese edad: "))
    # Usamos el índice para seleccionar de la tupla 'carreras'
    carrera = int(input("Ingrese carrera: (0: Software, 1: Contabilidad, 2: Derecho): "))

    estudiante_tupla = (nombre, apellido, edad, carrera)
    personas.append(estudiante_tupla)

# Procesamiento: Convertir tuplas en diccionarios con el nombre de la carrera
for persona in personas:
    nombre = persona[0]  
    apellido = persona[1]
    edad = persona[2]
    # Obtenemos el texto de la carrera usando el número como índice
    carrera_selecta = carreras[persona[3]]

    estudiante_dict = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "carrera": carrera_selecta
    }
    estudiantes.append(estudiante_dict)

print("\n" + "="*30)
print("       LISTA DE ESTUDIANTES")
print("="*30)

for p in estudiantes:
    print(f"{p['nombre']} {p['apellido']} tiene {p['edad']} años y estudia {p['carrera']}")