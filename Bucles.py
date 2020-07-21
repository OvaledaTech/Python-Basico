# %%
import math
print("Mi primer Bucle")
for i in [1, 2, 3]:
    print(f"{i}.  Hola Mundo")


# %%
miemail = str(input("Ingrese su email: "))
arroba = False
punto = False  # hola@hotmail.com
contador = 0
for j in miemail:
    if (j == "@"):
        arroba = True
        contador = contador+1
    elif (j == "."):
        punto = True
if arroba == True and punto == True and contador == 1:
    print(f"El email: {miemail} es correcto")
else
print(f"El email: {miemail} no es correcto")


# %%
for i in range(5, 20, 4):
    print(f"{i}: Hola a todos")

# %%
for i in range(1, 6, 1):
    print(f"{i}: Hola")

# %%
for i in range(5):
    print(f"{i+1}: Hola")


# %%
# Hola@hotmail.com
correo = False
email = str(input("Ingrese su email: "))
for i in range(len(email)):
    if email[i] == "@":
        correo = True
if correo == True:
    print("El email es correcto")
else:
    print("El email es incorrecto")


# %%
print("Calculo de la Edad")
edad = int(input("Ingrese su edad: "))
while edad <= 0 or edad > 100:
    print("Ingrese una edad positiva y menor que 100")
    edad = int(input("Ingrese su edad: "))

print(f"Tu tienes {edad} años")

# %%
print("programa que calcula la raiz cuadrada de un numero")
contador = 0
numero = (float(input("ingrese un numero: ")))

while numero < 0:
    print("No se puede sacar raices de numeros negativos")
    contador = contador+1
    if contador == 3:
        print("Has sobrepaso tus 3 intentos")
        break
    numero = (float(input("ingrese un numero: ")))
if contador < 3:
    z = math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es: {z}")
    print("Programa finalizado.....")

# %%
