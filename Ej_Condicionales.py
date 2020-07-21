# %% [markdown]
# Ejercicio de Condicionales:
# Voy un numero 0 a 10. Cuando el numero este entre 0 y 5, el nombre que ingresen se almacena al final la lista 1, cuando ingresen un numero entre 6a 10 se nombre se alamacena en una lista 2. Si el numero ingresado es negativo o mayo a 10 escriben en pantalla error en el numero ingresado

# %%
print("USO DE CONDICIONALES")
lista1 = []
lista2 = []
# %%
numero = int(input("ingresar un numero entre 0 y 10"))
nombre = str(input("ingresar un nombre"))
if 0 < numero < 5:
    print(lista1.append(nombre))
    print(lista1)
elif 5 <= numero <= 10:
    print(lista2.append(nombre))
    print(lista2)
else:
    print("Error en el dato ingresado")
# %%
print(lista2)

# %%
