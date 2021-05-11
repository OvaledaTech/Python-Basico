# %% [markdown]
# PROGRAMA QUE EJECUTA LA CALCULADORA
# %% [markdown]
# ** SUMA**
# %%
a = 4
b = 8
suma = a + b
print("El valor de la suma:", suma)


print  # %%
# **RESTA**
a = 10
b = 10
RESTA = a-b
print("el resultado DE *LA RESTA* es:", RESTA)
# %%  [markdown]
# ## multiplicación
a = 5
b = 7
resultado = a*b
print("el resultado es:", resultado)

# %%  [markdown]
# ## Division
x = "david"
a = 5.2
c = type(x)
b = 7
resultado = a/b
print("el resultado de la division es:", resultado)
print(c)


# %%  [markdown]
# ## Calculadora


# %%
print("PROGRAMA DE LA CALCULADORA")

# %%
operacion = str(
    input("Indique la operación que desea realizar suma, resta, producto, division"))
a = float(input("ingrese el primer numero: "))
# print(a)
b = float(input("ingrese el segundo número: "))
# print(b)

if operacion == "suma":
    resultado = a+b
    print(resultado)
elif operacion == "resta":
    resultado = a-b
    print(resultado)
elif operacion == "producto":
    resultado = a*b
    print(resultado)
elif operacion == "division":
    resultado = a/b
    print(resultado)

else:
    print("error elija correctamente")


# %%
