# %%
import time


class Banda():
    def __init__(self):
        self.largo = 2
        self.motor1 = False
        self.motor2 = False
        self.SF1 = False
        self.SF2 = False
        self.SF3 = False
        self.SF4 = False
        self.SF5 = False
        self.cilindro = False
        self.contador = 0
        self.contador2 = 0

    def motor1_0n(self):
        self.motor1 = True
        return(print(f"Motor 1 encendido......"))

    def motor1_0ff(self):
        self.motor1 = False
        return(print(f"Motor 1 apagado......"))

    def motor2_0n(self):
        self.motor2 = True
        return(print(f"Motor 2 encendido......"))

    def motor2_0ff(self):
        self.motor2 = False
        return(print(f"Motor 2 apagado......"))

    def SF1_0n(self):
        self.SF1 = True
        return(print(f"Sensor Fotoelectrico 1 encendido......"))

    def SF1_0ff(self):
        self.SF1 = False
        return(print(f"Sensor Fotoelectrico 1 apagado......"))

    def SF2_0n(self):
        self.SF2 = True
        return(print(f"Sensor Fotoelectrico 2 encendido......"))

    def SF2_0ff(self):
        self.SF2 = False
        return(print(f"Sensor Fotoelectrico 2 apagado......"))

    def SF3_0n(self):
        self.SF3 = True
        return(print(f"Sensor Fotoelectrico 3 encendido......"))

    def SF3_0ff(self):
        self.SF3 = False
        return(print(f"Sensor Fotoelectrico 3 apagado......"))

    def SF4_0n(self):
        self.SF4 = True
        print(f"Sensor Fotoelectrico 4 encendido......")
        return(True)

    def SF4_0ff(self):
        self.SF4 = False
        print(f"Sensor Fotoelectrico 4 apagado......")
        return(False)

    def SF5_0n(self):
        self.SF5 = True
        print(f"Sensor Fotoelectrico 5 encendido......")
        return(True)

    def SF5_0ff(self):
        self.SF5 = False
        print(f"Sensor Fotoelectrico 5 apagado......")
        return(False)

    def cilindro_on(self):
        self.cilindro = True
        return(print(f"Cilindro 1 encendido......"))

    def cilindro_off(self):
        self.cilindro = False
        return(print(f"Cilindro 1 apagado......"))

    def estado_sensores(self):
        self.est_sf1 = str(input("Ingrese el estado del SF1:"))
        self.est_sf2 = str(input("Ingrese el estado del SF2:"))
        if (self.est_sf1 == "ON" and self.est_sf2 == "ON"):
            self.caja = "Grande"
        elif (self.est_sf1 == "OFF" and self.est_sf2 == "ON"):
            self.caja = "Pequeña"
        else:
            self.caja = "Motor1 apagado"

        return(print(f"SF1: {self.est_sf1} SF2: {self.est_sf2} \nSe ha sensada una caja: {self.caja}"))

    def clasificacion(self):
        self.tiempo = 0
        if self.caja == "Grande":
            self.tiempo = 5
        else:
            self.tiempo = 3
        return(self.tiempo)

    def contaje(self):

        if self.caja == "Grande":
            valsf4 = self.SF4_0n()
        if self.caja == "Grande" and valsf4 == True:
            self.contador = self.contador+1

        else:
            valsf5 = self.SF5_0n()

            # self.contador2=self.contador2+1
        # return()
        return(print(f" Contador1= {self.contador} "))


MiBanda = Banda()
MiBanda.motor1_0n()
time.sleep(3)
MiBanda.motor1_0ff()
MiBanda.estado_sensores()
MiBanda.motor1_0n()
Y = MiBanda.clasificacion()
time.sleep(Y)
MiBanda.contaje()


# %%
