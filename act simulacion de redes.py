import time
import random

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []
        self.buffer = []  # almacena mensajes temporalmente

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

    def eliminar_conexion(self, nodo):
        if nodo in self.conexiones:
            self.conexiones.remove(nodo)

    def enviar_mensaje(self, mensaje):
        print(f"\n{self.nombre} envía: {mensaje}")
        for nodo in self.conexiones:
            # simulamos pérdida de paquetes (30% probabilidad)
            if random.random() < 0.3:
                print(f"⚠️ Mensaje perdido hacia {nodo.nombre}")
            else:
                nodo.recibir_mensaje(mensaje, self.nombre)

    def recibir_mensaje(self, mensaje, remitente):
        print(f"{self.nombre} recibió de {remitente}: {mensaje}")
        self.buffer.append((mensaje, remitente))  # se guarda en buffer

    def procesar_buffer(self):
        print(f"\n{self.nombre} procesando buffer...")
        while self.buffer:
            mensaje, remitente = self.buffer.pop(0)  # FIFO
            print(f"{self.nombre} procesó mensaje de {remitente}: {mensaje}")


# Crear nodos
servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")

# Conectar
servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)

# Enviar mensaje
servidor.enviar_mensaje("Hola clientes, este es el servidor")

# Procesar buffer de clientes
cliente1.procesar_buffer()
cliente2.procesar_buffer()
cliente3.procesar_buffer()

# Simulación de desconexión
time.sleep(2)
print("\nSimulando desconexión y reconexión dinámica...")

servidor.eliminar_conexion(cliente2)

servidor.enviar_mensaje("Cliente 2 desconectado")

cliente1.procesar_buffer()
cliente2.procesar_buffer()
cliente3.procesar_buffer()

# Reconexión
time.sleep(2)
servidor.agregar_conexion(cliente2)

servidor.enviar_mensaje("¡Hola de nuevo a todos!")

cliente1.procesar_buffer()
cliente2.procesar_buffer()
cliente3.procesar_buffer()