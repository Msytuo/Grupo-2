"""
Vamos a hacer un simple programa que coja a todos los alumnos de clase y los junte en grupos de forma aleatoria.
Utilizaremos la biblioteca random.

"""
# Iniciamos la biblioteca random

import random

# Hacemos la lista de alumnos y luego la  randomizamos.

alumnos = ["German", "Javi", "Alejandro", "Diego_1", "Diego_2",
           "Marcos", "Nora", "Sara", "Ricardo", "Bella", "Nerea", "Uriel", "Diego_3"]

random.shuffle(alumnos)

#Creamos una lista de listas que sean los grupos

grupos = [
    alumnos[0:3],
    alumnos[3:6],
    alumnos[6:9]
]

# He tenido que sacar el grupo de 4 (somos impares y hay un grupo de 4 en vez de tres), porque me daba error.

grupos.append(alumnos[9:13])

#Añadimos numero al grupo y mostramos todos los grupos.

numero_grupo = 1

for grupo in grupos:
    print(f"Grupo {numero_grupo}: {grupo}")
    numero_grupo += 1
    