# %%  [markdown]
# # Manejo de Listas

# %%
datos = [2, "david", 5.88]
print(datos[-3])
print(type(datos[0]), type(datos[1]), type(datos[2]))

# %%
print(datos[0:2])

# %%
print(datos[1:3])

# %%
datos.append("sandra")
print(datos)

# %%
datos.insert(2, "luis")
print(datos)

# %%
datos.extend(["jairo", "oscar"])
print(datos)

# %%
print(datos.index("david"))

# %%
print(5.89 in datos)

# %%
datos.remove("oscar")
print(datos)

# %%
datos.pop()
print(datos)

# %%
data1 = [2, "david", 5.88]
data2 = ["alejandra", "jairo", "oscar"]
data3 = data1+data2
print(data3)

# %%
print(len(data3))

# %%
