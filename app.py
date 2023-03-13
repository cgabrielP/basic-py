# Funciones para las operaciones
def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


def rest(a, b):
    return a % b


# Menú de opciones
print("Seleccione la operación que desea realizar:")
print("+. Suma")
print("-. Resta")
print("x. Multiplicación")
print("/. División")
print("%. Resto de division")

# Entrada de datos
opcion = input("Ingrese la opción (+,-,x,/,%): ")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar la operación seleccionada
if opcion == "+":
    print(num1, "+", num2, "=", suma(num1, num2))

elif opcion == "-":
    print(num1, "-", num2, "=", resta(num1, num2))

elif opcion == "x":
    print(num1, "*", num2, "=", multiplicacion(num1, num2))

elif opcion == "/":
    print(num1, "/", num2, "=", division(num1, num2))
elif opcion == "%":
    print(num1, "%", num2, "=", division(num1, num2))
else:
    print("Opción inválida")
