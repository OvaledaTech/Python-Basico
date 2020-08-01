# %%
import time
print("Programacion Orientada a Objetos")


class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    def arrancar(self):  # comportamiento= funcion pero siempre coloco self
        self.enmarcha = True

    def estado(self):
        if (self.enmarcha == True):
            return("El coche esta en movimiento")
        else:
            return("El coche esta detenido")


miCoche = Coche()
print("El largo del coche es: ", miCoche.largoChasis)
#print("El coche tiene", miCoche.ruedas,"ruedas")
print(f"El coche tiene {miCoche.ruedas} ruedas")
miCoche.arrancar()  # mandan a ejecutar el comportamiento
print(miCoche.estado())
miCoche2 = Coche()
print("El largo del coche2 es: ", miCoche2.largoChasis)
miCoche2.arrancar()
print(miCoche2.estado())
miCoche2.ruedas = 5
print(f"El coche2 tiene {miCoche2.ruedas} ruedas")

# %%


class doscificacion():
    largoTanque = 2
    Volumen = 3
    radio = 2
    ev1 = False
    ev2 = False
    motor = False

    def naranja_on(self):
        self.ev1 = True

    def naranja_off(self):
        self.ev1 = False

    def agua_on(self):
        self.ev2 = True

    def agua_off(self):
        self.ev2 = False

    def batir_on(self):
        self.motor = True

    def batir_off(self):
        self.motor = False

    def estado1(self):
        if self.ev1 == True:
            return("Electrovalvula1 abierta")
        else:
            return("Electrovalvula1 cerrada")

    def estado2(self):
        if self.ev2 == True:
            return("Electrovalvula2 abierta")
        else:
            return("Electrovalvula2 cerrada")

    def estado3(self):
        if self.motor == True:
            return("Motor Activado")
        else:
            return("Motor Desactivado")


tanque1 = doscificacion()
print(f"El largo del Tanque es:{tanque1.largoTanque}")
print(tanque1.estado1())
tanque1.naranja_on()
print(tanque1.estado1())
time.sleep(5)
tanque1.naranja_off()
print(tanque1.estado1())
time.sleep(2)
print(tanque1.estado2())
tanque1.agua_on()
print(tanque1.estado2())
time.sleep(7)
tanque1.agua_off()
print(tanque1.estado2())
time.sleep(2)

# Completar el funcionamiento del motor

# %%
print("Manejo de Constructores y Encapsulamiento")


class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def encendido(self, suitch):  # comportamiento= funcion pero siempre coloco self
        self.__enmarcha = suitch
        if self.__enmarcha == True:
            chequeo = self.__chequeoInt()
        if self.__enmarcha == True and chequeo == True:
            return("El coche esta en marcha")
        elif self.__enmarcha == True and chequeo == False:
            return("Algo ha salido mal...")
        else:
            return("El coche esta parado")

    def estado(self):
        return(f"El coche tiene {self.__ruedas} ruedas. Un largo de chasis de {self.__largoChasis} m")

    def __chequeoInt(self):
        print("Realizando chequeo interno. Espere.........")
        self.gasolina = "OK"
        self.aceite = "OK"
        self.puertas = "cerradas"

        if self.gasolina == "OK" and self.aceite == "OK" and self.puertas == "cerradas":
            return(True)
        else:
            return(False)


miCoche = Coche()
print(miCoche.encendido(False))
print(miCoche.estado())


# %%
