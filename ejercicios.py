# %%
import time

while True:
    hoy = time.localtime()
    print(hoy.tm_hour, ":", hoy.tm_min, ":", hoy.tm_sec)
    time.sleep(5)


# %%
i = 9
while i < 10:
    print(i)
    i = i-1
    time.sleep(1)

# %%
contador = 0
while True:
    if contador == 0:

        rojo = True
        amarillo = False
        verde = False
        contador = contador+1
        print(
            f"\nsemaforo: \nRojo: {rojo} \nAmarillo: {amarillo} \nVerde: {verde}")
        time.sleep(4)

    elif contador == 1:
        rojo = False
        amarillo = True
        verde = False
        contador = contador+1
        print(
            f"\nsemaforo:\nRojo: {rojo} \nAmarillo: {amarillo} \nVerde: {verde}")
        time.sleep(2)

    elif contador == 2:
        rojo = False
        amarillo = False
        verde = True
        contador = 0
        print(
            f"\nsemaforo: \nRojo: {rojo} \nAmarillo: {amarillo} \nVerde: {verde}")
        time.sleep(3)


# %%
contador = 0
while True:
    if contador == 0:
        pass
        rojo = True
        amarillo = False
        verde = False
        contador = 1
        tiempo = 5

    elif contador == 1:
        rojo = False
        amarillo = True
        verde = False
        contador = 2
        tiempo = 2

    elif contador == 2:
        rojo = False
        amarillo = False
        verde = True
        contador = 0
        tiempo = 8

    print(
        f"\nsemaforo: \nRojo: {rojo} \nAmarillo: {amarillo} \nVerde: {verde}")
    time.sleep(tiempo)


# %%
contador = 0
tiempo = 0
while True:

    def semaforo(data1, data2, data3, data4):
        rojo = data1
        amarillo = data2
        verde = data3
        tiempo = data4
        print(
            f"\nsemaforo: \nRojo: {rojo} \nAmarillo: {amarillo} \nVerde: {verde}")
        time.sleep(tiempo)

    if contador == 0:
        semaforo(True, False, False, 5)
        contador = 1

    elif contador == 1:
        semaforo(False, True, False, 2)
        contador = 2

    elif contador == 2:
        semaforo(False, False, True, 8)
        contador = 0


# %%
