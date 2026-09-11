from abc import ABC, abstractmethod


class Puerta(ABC):
    @abstractmethod
    def abrir(self):
        pass

    @abstractmethod
    def cerrar(self):
        pass

    @abstractmethod
    def bloquear(self, activar):
        pass


class PuertaGaraje(Puerta):
    def __init__(self):
        self.abierta = False
        self.bloqueada = False

    def abrir(self):
        self.abierta = True
        print("Puerta del garaje abierta")

    def cerrar(self):
        self.abierta = False
        print("Puerta del garaje cerrada")

    def bloquear(self, activar):
        self.bloqueada = activar
        estado = "bloqueada" if activar else "desbloqueada"
        print(f"Puerta del garaje {estado}")


class PuertaOficina(Puerta):
    def __init__(self):
        self.abierta = False
        self.bloqueada = False

    def abrir(self):
        self.abierta = True
        print("Puerta de la oficina abierta")

    def cerrar(self):
        self.abierta = False
        print("Puerta de la oficina cerrada")

    def bloquear(self, activar):
        self.bloqueada = activar
        estado = "bloqueada" if activar else "desbloqueada"
        print(f"Puerta de la oficina {estado}")



class ControlPuerta:
    """Control basico: abrir y cerrar"""
    def __init__(self, puerta):
        self.puerta = puerta

    def abrir(self):
        self.puerta.abrir()

    def cerrar(self):
        self.puerta.cerrar()


class ControlPuertaSeguridad(ControlPuerta):
    """Control con funciones de seguridad"""

    def bloquear(self):
        self.puerta.bloquear(True)

    def desbloquear(self):
        self.puerta.bloquear(False)



garaje = PuertaGaraje()
oficina = PuertaOficina()

print("\n<<<<< Control del garaje >>>>>>>")
control_garaje = ControlPuerta(garaje)
control_garaje.abrir()
control_garaje.cerrar()

print("\n<<<<<<< Control de seguridad de la oficina >>>>>")
control_seguridad = ControlPuertaSeguridad(oficina)
control_seguridad.abrir()
control_seguridad.cerrar()
control_seguridad.bloquear()
control_seguridad.desbloquear()