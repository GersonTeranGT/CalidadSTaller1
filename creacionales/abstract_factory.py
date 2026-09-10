from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

class Alerta(ABC):
    @abstractmethod
    def mostrar(self, mensaje):
        pass



class NotificacionCorreo(Notificacion):
    def enviar(self, mensaje):
        print(f"\nEnviando mensaje por correo electronico: {mensaje}")

class AlertaCorreo(Alerta):
    def mostrar(self, mensaje):
        print(f"Alerta enviada por correo electronico: {mensaje}")

class NotificacionSMS(Notificacion):
    def enviar(self, mensaje):
        print(f"\nEnviando mensaje SMS: {mensaje}")

class AlertaSMS(Alerta):
    def mostrar(self, mensaje):
        print(f"Alerta enviada por SMS: {mensaje}")

class NotificacionPush(Notificacion):
    def enviar(self, mensaje):
        print(f"\nEnviando una notificacion push: {mensaje}")

class AlertaPush(Alerta):
    def mostrar(self, mensaje):
        print(f"Alerta push enviada: {mensaje}")



class FabricaCorreos:
    def crear_notificacion(self):
        return NotificacionCorreo()

    def crear_alerta(self):
        return AlertaCorreo()

class FabricaSMS:
    def crear_notificacion(self):
        return NotificacionSMS()

    def crear_alerta(self):
        return AlertaSMS()

class FabricaPush:
    def crear_notificacion(self):
        return NotificacionPush()

    def crear_alerta(self):
        return AlertaPush()


tipo_canal = "Correo"

if tipo_canal == "Correo":
    fabrica = FabricaCorreos()
elif tipo_canal == "SMS":
    fabrica = FabricaSMS()
elif tipo_canal == "Push":
    fabrica = FabricaPush()
else:
    raise ValueError("Canal no soportado")

notificacion = fabrica.crear_notificacion()
alerta = fabrica.crear_alerta()

notificacion.enviar(" ¡¡¡BIENVENIDO!!! ")
alerta.mostrar("Ingreso al sistema detectado\n")
