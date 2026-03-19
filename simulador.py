import threading
import time
import random
import logging
from estacionamiento import Estacionamiento
from vehiculo import Vehiculo
from registro_historial import RegistroHistorial

#config log
logging.basicConfig(
    filename='bitacora.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
)
 
logger = logging.getLogger(__name__)

#

def simular_vehiculo(estacionamiento, registro, placa, propietario, tipo):
    v = Vehiculo(placa, propietario, tipo) #ejecuta cada hilo
    
    #Intentar ingresar
    if estacionamiento.ingresar(v):
        registro.agregar('INGRESO', placa)
        
        #Simular tiempo de permanencia
        tiempo_estadia = random.randint(1, 4)
        time.sleep(tiempo_estadia)
        
        #Salir
        segundos = estacionamiento.salir(placa)
        registro.agregar('SALIDA', placa, segundos)

def ejecutar_simulacion():
    #Instanciamos los objetos necesarios
    mi_estacionamiento = Estacionamiento("Parking Central", capacidad_total=5)
    mi_registro = RegistroHistorial()
  
    datos_vehiculos = [
        ("ABC-123", "Juan", "auto"),
        ("XYZ-789", "Maria", "moto"),
        ("DEF-456", "Pedro", "camioneta"),
        ("GHI-012", "Ana", "auto"),
        ("JKL-345", "Luis", "moto"),
        ("MNO-678", "Elena", "auto"), # Este debería quedar fuera
    ]

    hilos = []

    logger.info(f"SIMULACIÓN INICIADA — {mi_estacionamiento.nombre} | capacidad={mi_estacionamiento.capacidad_total}")
    print(f"--- Iniciando simulación en {mi_estacionamiento.nombre} ---")

    # INSTANCIACIÓN DEL GRUPO DE HILOS
    for placa, dueño, tipo in datos_vehiculos:
        # Creamos el hilo asignando la función y los argumentos
        hilo = threading.Thread(
            target=simular_vehiculo, 
            args=(mi_estacionamiento, mi_registro, placa, dueño, tipo)
        )
        hilos.append(hilo)
        hilo.start() # Inicia la ejecución concurrente

    # Esperar a que todos los hilos terminen
    for h in hilos:
        h.join()

    logger.info("SIMULACIÓN FINALIZADA — todos los hilos completados")

    print("\n Simulación finalizada")
    mi_estacionamiento.estado()
    mi_registro.mostrar()

if __name__ == "__main__":
    ejecutar_simulacion()