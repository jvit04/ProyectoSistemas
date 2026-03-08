import threading
from datetime import datetime


class RegistroHistorial:
    """
    Entidad auxiliar de auditoría que guarda el historial completo 
    de movimientos del estacionamiento.
    """
    #Atributos
    historial: list[dict]
    _lock: threading.Lock
    
    def __init__(self):
        """
        Inicializa el registro de historial con protección de mutex.
        """
        self.historial = []
        self._lock = threading.Lock()
    
    def agregar(self, tipo, placa, segundos=None):
        """
        Añade un nuevo evento al historial.
        
        Args:
            tipo (str): Tipo de evento ('INGRESO' o 'SALIDA')
            placa (str): Identificador del vehículo
            segundos (int, optional): Segundos de permanencia (solo para salidas)
        """
        with self._lock:
            evento = {
                'timestamp': datetime.now(),
                'tipo': tipo,
                'placa': placa,
                'segundos': segundos
            }
            self.historial.append(evento)
            print(f"✓ Evento registrado: {tipo} - {placa}")
    
    def mostrar(self):
        """
        Imprime el historial completo con timestamps.
        """
        with self._lock:
            if not self.historial:
                print("\n⚠️  El historial está vacío.\n")
                return
            
            print("\n" + "="*70)
            print("HISTORIAL DE MOVIMIENTOS DEL ESTACIONAMIENTO")
            print("="*70)
            print(f"{'Fecha/Hora':<20} {'Tipo':<12} {'Placa':<12} {'Permanencia':<15}")
            print("-"*70)
            
            for evento in self.historial:
                timestamp = evento['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
                tipo = evento['tipo']
                placa = evento['placa']
                segundos = f"{evento['segundos']} seg" if evento['segundos'] else "N/A"
                
                print(f"{timestamp:<20} {tipo:<12} {placa:<12} {segundos:<15}")
            
            print("="*70 + "\n")
    
    def obtener_historial(self):
        """
        Retorna una copia del historial (thread-safe).
        
        Returns:
            list[dict]: Copia de la lista de eventos
        """
        with self._lock:
            return self.historial.copy()
    
    def limpiar_historial(self):
        """
        Limpia el historial (uso administrativo).
        """
        with self._lock:
            self.historial.clear()
            print("✓ Historial limpiado.")
