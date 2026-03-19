import threading
import logging

logger = logging.getLogger(__name__)

class Estacionamiento:
    nombre: str
    capacidad_total: int
    cupos_disponibles: int          #recurso compartido básico
    registro_vehiculos: dict        #recurso compartido complejo
    _lock: threading.Lock

    def __init__(self, nombre: str, capacidad_total: int):
        self.nombre = nombre
        self.capacidad_total = capacidad_total
        self.cupos_disponibles = capacidad_total
        self.registro_vehiculos = {}
        self._lock = threading.Lock()

    def ingresar(self, vehiculo) -> bool:
        logger.debug(f"Intentando adquirir lock para ingreso | placa={vehiculo.placa}")
        with self._lock:
            logger.debug(f"Lock adquirido | placa={vehiculo.placa} | cupos_disponibles={self.cupos_disponibles}")
            if self.cupos_disponibles <= 0:
                logger.warning(f"Sin cupo — ingreso rechazado | placa={vehiculo.placa}")
                print(f"No hay cupo para {vehiculo.placa}")
                return False
            
            self.cupos_disponibles -= 1

            vehiculo.registrar_entrada()
            self.registro_vehiculos[vehiculo.placa] = vehiculo

            logger.info(f"Ingreso registrado | placa={vehiculo.placa} | cupos_restantes={self.cupos_disponibles}")
            print(f"Ingreso exitoso: {vehiculo.placa}; Cupos restantes: {self.cupos_disponibles}")
            return True

    def salir(self, placa: str):
        logger.debug(f"Intentando adquirir lock para salida | placa={placa}")
        with self._lock:
            logger.debug(f"Lock adquirido | placa={placa}")
            
            if placa not in self.registro_vehiculos:
                logger.warning(f"Placa no encontrada en registro | placa={placa}")
                print(f"{placa} no se encuentra en el estacionamiento")
                return None

            vehiculo = self.registro_vehiculos[placa]

            vehiculo.registrar_salida()
            permanencia = vehiculo.calcular_permanencia()

            self.cupos_disponibles += 1

            del self.registro_vehiculos[placa]

            logger.info(f"Salida registrada | placa={placa} | permanencia={permanencia}s | cupos_disponibles={self.cupos_disponibles}")

            print(f"Salida exitosa: {placa}; Permanencia: {permanencia} seg; Cupos: {self.cupos_disponibles}")
            return permanencia

    def estado(self):
        with self._lock:
            ocupados = self.capacidad_total - self.cupos_disponibles
            logger.info(f"Estado consultado | ocupados={ocupados} | disponibles={self.cupos_disponibles}")
            print(f"{self.nombre}")
            print(f"Capacidad total: {self.capacidad_total}")
            print(f"Ocupados: {ocupados}")
            print(f"Disponibles: {self.cupos_disponibles}")
            if self.registro_vehiculos:
                print("Vehículos dentro:")
                for v in self.registro_vehiculos.values():
                    print(f"{v}")
            else:
                print("No hay vehículos.") 

    def __str__(self):
        return f"Estacionamiento(nombre='{self.nombre}', capacidad={self.capacidad_total}, disponibles={self.cupos_disponibles})"