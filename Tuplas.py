# %%[markdown]
# **TUPLAS**


# %%
datos = ("juan", 13, 1, 1995)
print(datos)

# %%
lista = list(datos)
print(lista)


# %%
tupla = tuple(lista)
print(tupla)


# %%
datos2 = ("DAVID", 5, 12, 1983, 5)
print(datos2)


# %%
print(datos2[0:2])


# %%
print(1983 in datos2)


# %%
print(datos2.count(5))


# %%
print(len(datos2))


# %%
print(datos2)

# %%
nombre, dia, mes, ano, aniversario = datos2
print(nombre)
print(dia)
print(mes)


# %%[markdown]
# **CONDICIONALES**


# %%[markdown]
# ## VERIFICACION DE LAS NOTAS

# %%
notatotal = float(input("Ingrese su nota: "))
if notatotal < 0:
    print("Nota fuera de Rango")
elif notatotal < 5:
    print("insufiCiente")
elif notatotal < 6:
    print("SufiCiente")
elif notatotal < 7:
    print("Bien")
elif notatotal < 9:
    print("Notable")
elif notatotal > 10:
    print("error")
    print("nota fuera de rango")
else:
    print("Sobresaliente")
print("Programa Finalizado")


# %%


# %%
