# %%
class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(
            f"\nMarca: {self.marca} \nModelo:{self.modelo} \nEnMarcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenado={self.frena}")


class Moto(Vehiculos):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = True

    def estado(self):
        print(f"\nMarca: {self.marca} \nModelo:{self.modelo} \nEnMarcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenado={self.frena} \ncaballito= {self.hcaballito}")


class furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado == True):
            return("La furgoneta esta cargada")
        else:
            return("La furgoneta no esta cargada")


class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 80

    def cargaElectrica(self):
        self.cargando = True

    def estado(self):
        super().estado()
        print(
            f"\nCargando: {self.cargando} \nCon una autonomia del(%): {self.autonomia}")


class EBykes(VElectricos, Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def asistencia(self, valor):
        self.asistir = valor
        if (self.asistir == True):
            return("Asistencia Electrica Activada")
        else:
            return("Asistencia Electrica Dsactivada")


# miMoto=Moto("Honda","HF135")
# miMoto.caballito()
# miMoto.estado()
# miFugoneta=furgoneta("Toyota","T135")
# miFugoneta.arrancar()
# miFugoneta.estado()
# miFugoneta.carga(False)
# miTrole=VElectricos("Patito","P123")
# miTrole.cargaElectrica()
# miTrole.estado()
mibici = EBykes("Pedalec", "P456")
mibici.arrancar()
mibici.cargaElectrica()
mibici.estado()
print(mibici.asistencia(False))


# %%
# Polimorfismo

class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

# miVehiculo=Moto()
# miVehiculo.desplazamiento()
# miVehiculo2=Coche()
# miVehiculo2.desplazamiento()
# miVehiculo3=Camion()
# miVehiculo3.desplazamiento()


def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Coche()
desplazamientovehiculo(miVehiculo)


# %%
