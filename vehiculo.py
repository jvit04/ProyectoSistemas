from datetime import datetime


class Vehiculo:
    """
    Representa un vehículo que ingresa al estacionamiento.
    Contiene todos los datos del vehículo y los métodos para registrar tiempos.
    """
    #Atributos
    placa: str
    propietario: str
    tipo: str
    hora_entrada: datetime
    hora_salida: datetime
    
    def __init__(self, placa, propietario, tipo):
        """
        Inicializa un nuevo vehículo.
        
        Args:
            placa (str): Identificador único del vehículo
            propietario (str): Nombre del dueño del vehículo
            tipo (str): Categoría del vehículo (auto, moto, camioneta)
        """
        self.placa = placa
        self.propietario = propietario
        self.tipo = tipo
        self.hora_entrada = None
        self.hora_salida = None
    
    def registrar_entrada(self):
        """Asigna la hora actual como hora de entrada"""
        self.hora_entrada = datetime.now()
        print(f"Vehículo {self.placa} ingresó a las {self.hora_entrada.strftime('%H:%M:%S')}")
    
    def registrar_salida(self):
        """Asigna la hora actual como hora de salida"""
        self.hora_salida = datetime.now()
        print(f"Vehículo {self.placa} salió a las {self.hora_salida.strftime('%H:%M:%S')}")
    
    def calcular_permanencia(self):
        """
        Retorna los segundos de estadía en el estacionamiento.
        
        Returns:
            int: Segundos de permanencia, o None si no ha completado entrada/salida
        """
        if self.hora_entrada is None or self.hora_salida is None:
            return None
        
        diferencia = self.hora_salida - self.hora_entrada
        segundos = int(diferencia.total_seconds())
        return segundos
    
    def __str__(self):
        """Representa el vehículo como string"""
        return f"Vehículo(placa='{self.placa}', propietario='{self.propietario}', tipo='{self.tipo}')"
    
    def __repr__(self):
        """Representación técnica del vehículo"""
        return self.__str__()
