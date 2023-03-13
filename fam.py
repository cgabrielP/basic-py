for i in range(5):
    print(i)

# Pedir los datos de los abuelos
abuelo_paterno = input("Ingresa el nombre del abuelo paterno: ")
abuela_paterna = input("Ingresa el nombre de la abuela paterna: ")
abuelo_materno = input("Ingresa el nombre del abuelo materno: ")
abuela_materna = input("Ingresa el nombre de la abuela materna: ")

edad_abuelo_paterno = input("Ingresa la edad del abuelo paterno: ")
edad_abuela_paterna = input("Ingresa la edad de la abuela paterna: ")
edad_abuelo_materno = input("Ingresa la edad del abuelo materno: ")
edad_abuela_materna = input("Ingresa la edad de la abuela materna: ")

# Pedir los datos de los padres
padre = input("Ingresa el nombre del padre: ")
madre = input("Ingresa el nombre de la madre: ")

edad_padre = input("Ingresa la edad del padre: ")
edad_madre = input("Ingresa la edad de la madre: ")

# Pedir los datos de los hermanos
numero_hermanos = int(input("¿Cuántos hermanos tienes? "))

hermanos = []
edades_hermanos = []
for i in range(numero_hermanos):
    hermano = input(f"Ingresa el nombre del hermano {i+1}: ")
    edad_hermano = input(f"Ingresa la edad del hermano {i+1}: ")
    hermanos.append(hermano)
    edades_hermanos.append(edad_hermano)

# Pedir los datos de las mascotas
numero_mascotas = int(input("¿Cuántas mascotas tienes? "))

mascotas = []
edades_mascotas = []

for i in range(numero_mascotas):
    mascota = input(f"Ingresa el nombre de la mascota {i+1}: ")
    edad_mascota = input(f"Ingresa la edad de la mascota {i+1}: ")
    mascotas.append(mascota)
    edades_mascotas.append(edad_mascota)

# Imprimir los datos del registro familiar
print("Registro Familiar")
print("=================")
print("Abuelos:")
print(f"- Abuelo paterno: {abuelo_paterno} ({edad_abuelo_paterno} años)")
print(f"- Abuela paterna: {abuela_paterna} ({edad_abuela_paterna} años)")
print(f"- Abuelo materno: {abuelo_materno} ({edad_abuelo_materno} años)")
print(f"- Abuela materna: {abuela_materna} ({edad_abuela_materna} años)")

print("Padres:")
print(f"- Padre: {padre} ({edad_padre} años)")
print(f"- Madre: {madre} ({edad_madre} años)")

print("Hermanos:")
for i in range(numero_hermanos):
    print(f"- Hermano {i+1}: {hermanos[i]} ({edades_hermanos[i]} años)")

print("Mascotas:")
for i in range(numero_mascotas):
    print(f"- Mascota {i+1}: {mascotas[i]} ({edades_mascotas[i]} años)")
