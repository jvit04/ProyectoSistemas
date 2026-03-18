import threading
import time
from vehiculo import Vehiculo
from estacionamiento import Estacionamiento
import random
import string


"""
Análisis de arquitectura de hilos
Para la solución de este proyecto, se determinó utilizar la aquitectura
por objetos Thread y paso de argumentos, instanciando threading.Thread y pasando
la función mediante el parámetor 'target'.

Justificación:
Esta decisión nos permite separar la lógica del negocio de la lógica de la concurrencia.
No era indispensable heredad de threading.Thread, ya que nuestras entidias son objetos y
recursos compartidos accedidos simultáneamente por múltiples flujos de ejecución.
"""

import time
import threading

def accion_vehiculo(parqueadero, vehiculo):
    """
    Intenta ingresar. Si está lleno, espera 1 segundo y vuelve a intentar
    infinitamente hasta que consiga un cupo (ningún nodo se rinde).
    """
    print(f"[{threading.current_thread().name}] llegando: {vehiculo.placa}...")
    
    ingreso_exitoso = False
    intentos = 0
    
    # Bucle infinito: solo se rompe cuando ingreso_exitoso sea True
    while not ingreso_exitoso:
        ingreso_exitoso = parqueadero.ingresar(vehiculo)
        
        if ingreso_exitoso:
            # ¡Logró entrar!
            time.sleep(2) # Se queda 2 segundos estacionado
            # Mostrar cuántos intentos le tomó entrar hace que el log sea más interesante
            if intentos > 0:
                print(f"[{threading.current_thread().name}] 🟢 {vehiculo.placa} LOGRÓ ENTRAR tras {intentos} intentos. Retirando...")
            else:
                print(f"[{threading.current_thread().name}] 🟢 retirando {vehiculo.placa}...")
            
            parqueadero.salir(vehiculo.placa)
        else:
            # Está lleno, le toca esperar
            intentos += 1
            print(f"[{threading.current_thread().name}] 🟡 {vehiculo.placa} en espera... (Intento {intentos})")
            time.sleep(1) # Espera 1 segundo antes de volver a intentar entrar

def generar_placa_aleatoria():
    """Genera una placa con formato AAA-111"""
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros = ''.join(random.choices(string.digits, k=3))
    return f"{letras}-{numeros}"

def ejecutar_simulacion():
    print("="*60)
    print("   INICIANDO SIMULACIÓN CONCURRENTE (CAOS ALEATORIO)")
    print("="*60)
    
    # 1. Instanciamos el recurso compartido: Un estacionamiento con solo 3 cupos
    mi_parqueadero = Estacionamiento("Smart Parking UCOM", 3)
    
    # 2. Generación aleatoria de vehículos. Para que sea más interesante y realistala simulación
    nombres_posibles = ["Juan", "Maria", "Pedro", "Ana", "Luis", "Carlos", "Sofia", "Jorge", "Elena", "Diego", "Carmen", "Raul"]
    tipos_posibles = ["auto", "moto", "camioneta"]
    
    # Decidimos al azar cuántos vehículos van a llegar (ej. entre 8 y 15 vehículos)
    cantidad_vehiculos = random.randint(8, 15)
    vehiculos = []
    
    print(f"⚠️ ALERTA: ¡Una avalancha de {cantidad_vehiculos} vehículos se dirige al estacionamiento (Capacidad: 3)!\n")
    
    for _ in range(cantidad_vehiculos):
        placa = generar_placa_aleatoria()
        propietario = random.choice(nombres_posibles)
        tipo = random.choice(tipos_posibles)
        
        nuevo_vehiculo = Vehiculo(placa, propietario, tipo)
        vehiculos.append(nuevo_vehiculo)
    
    lista_de_hilos = []
    
    # 3. Instanciamos un grupo de hilos con los argumentos necesarios
    for i, vehiculo in enumerate(vehiculos):
        # Arquitectura: Objetos Thread y paso de argumentos
        hilo = threading.Thread(
            name=f"Hilo-{i+1}",
            target=accion_vehiculo, 
            args=(mi_parqueadero, vehiculo) # Paso de argumentos al target
        )
        lista_de_hilos.append(hilo)
    
    # 4. Arrancamos todos los hilos (simulando que todos llegan casi al mismo tiempo)
    for hilo in lista_de_hilos:
        hilo.start()
        # Un micro-retraso aleatorio (entre 0 y 0.5 segundos) hace que el caos sea 
        # más realista, simulando autos llegando uno detrás de otro muy rápido.
        time.sleep(random.uniform(0, 0.5))
        
    # 5. Esperamos a que todos los hilos terminen su ejecución antes de cerrar el programa
    for hilo in lista_de_hilos:
        hilo.join()

    print("\n" + "="*60)
    print("   SIMULACIÓN FINALIZADA. ESTADO FINAL:")
    print("="*60)
    mi_parqueadero.estado()

if __name__ == "__main__":
    ejecutar_simulacion()
