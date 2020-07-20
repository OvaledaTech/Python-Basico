# %%
import math


def suma(a, b):
    resultado = a+b
    return(resultado)


z = suma(3, 7)
y = suma(3, 8)
print(z, y)


# %%
print("Programa que calculo si un alumno reprueba o aprueba")
nota = float(input("Ingrese su nota: "))


def evaluacion(valor):
    valorar = "Aprueba"
    if valor < 7:
        valorar = "Reprueba"
    return(valorar)


print("Con la nota de: ", nota, "el alumno: ", evaluacion(nota))


# %%
print("programa para el calculo de figuras geometricas")
operacion = str(input(
    "ingresar que figura geometrica desea calcular: triangulo, rectangulo, circulo"))
print(operacion)


def opcion(valor):
    if valor == "triangulo":
        base = float(input("ingresar valor de la base: "))
        altura = float(input("ingresar valor de la altura: "))
        resultado = (base*altura)/2
    elif valor == "rectangulo":
        lado = float(input("ingresar valor del lado: "))
        ancho = float(input("ingresar valor del ancho: "))
        resultado = lado*ancho
    elif valor == "circulo":
        radio = float(input("ingresar valor del radio: "))
        resultado = math.pi*(radio**2)
    return(resultado)


z = opcion(operacion)
print("El area del: ", operacion, "es: ", z)

print("Otra manera")
print(f" El area del circulo {operacion} es: {z} ")

# %%


# %%
