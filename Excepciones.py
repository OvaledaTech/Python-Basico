# %%
import math


def suma(x, y):
    return x+y


def resta(n1, n2):
    return n1-n2


def producto(n1, n2):
    return n1*n2


def division(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print("No se puede dividir para 0")
        return("Operacion Incorrecta...")


print("Programa que realiza la calculadora")
while True:

    try:
        op1 = int(input("Ingrese el primer numero: "))
        op2 = int(input("Ingrese el segundo numero: "))
        break
    except ValueError:
        print("Los valores introducidos no son  correctos, intentelo de nuevo")


operacion = input(
    "Ingrese la operacion a realizar(suma,resta,producto,division): ")


if operacion == "suma":
    print(f"El resultado de la {operacion} es: {suma(op1,op2)}")

elif operacion == "resta":
    print(f"El resultado de la {operacion} es: {resta(op1,op2)}")

elif operacion == "producto":
    print(f"El resultado de la {operacion} es: {producto(op1,op2)}")

elif operacion == "division":
    print(f"El resultado de la {operacion} es: {division(op1,op2)}")

else:
    print("Operacion no contemplada")

print("Programa terminado........")


# %%
print("Programa que realiza la division")

try:
    op1 = int(input("Ingrese el primer numero: "))
    op2 = int(input("Ingrese el segundo numero: "))
    print(f"El resultado de la division es: {op1/op2}")
except ZeroDivisionError:
    print("No se puede dividir para zero")

except ValueError:
    print("Ingrese un numero no una letra")

finally:
    print("Programa Terminado.............")


# %%
def evaluacion(edad):
    if edad < 0:
        raise ValueError("No se puede ingresar valores negativos")
    elif edad < 20:
        return("eres muy joven")
    elif edad < 40:
        return("eres joven")
    elif edad < 65:
        return("eres adultero")
    elif edad < 100:
        return("Cuidate")


print(evaluacion(-40))


# %%
print("Programa que calcula la raiz cuadrada de un numero")
num = float(input("Ingrese un numero: "))

while True:
    try:
        y = math.sqrt(num)
        break
    except ValueError:
        print("El valor del numero ingresado debe ser positivo")
    num = float(input("Ingrese un numero: "))
print(f"La raiz cuadrada de {num} es: {y}")

# %%


def raiz(a):
    if a < 0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return(math.sqrt(a))


num = float(input("Ingrese un numero: "))
try:
    print(f"La raiz cuadrada de {num} es: {raiz(num)}")
except ValueError as ErrNumNegativo:
    print("ErrNumNegativo")
    print("Ingrese un numero positivo")

print("Programa finalizado")


# %%
