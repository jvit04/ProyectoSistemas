"""
Script de prueba para demostrar las funcionalidades del sistema de estacionamiento
"""

from vehiculo import Vehiculo
from registro_historial import RegistroHistorial
import time

print("\n" + "="*70)
print("       PRUEBA DEL SISTEMA DE ESTACIONAMIENTO")
print("="*70)

# Crear instancia del registro
registro = RegistroHistorial()
vehiculos_activos = {}

# --- PRUEBA 1: Registrar ingresos ---
print("\n[PRUEBA 1] Registrando 3 vehículos...\n")

v1 = Vehiculo("ABC-123", "Juan Pérez", "auto")
v1.registrar_entrada()
vehiculos_activos["ABC-123"] = v1
registro.agregar('INGRESO', 'ABC-123')
time.sleep(1)

print()

v2 = Vehiculo("XYZ-789", "María González", "moto")
v2.registrar_entrada()
vehiculos_activos["XYZ-789"] = v2
registro.agregar('INGRESO', 'XYZ-789')
time.sleep(1)

print()

v3 = Vehiculo("MNO-456", "Carlos López", "camioneta")
v3.registrar_entrada()
vehiculos_activos["MNO-456"] = v3
registro.agregar('INGRESO', 'MNO-456')

# --- PRUEBA 2: Ver vehículos activos ---
print("\n[PRUEBA 2] Vehículos activos en el estacionamiento:\n")
print("="*70)
print("VEHÍCULOS ACTIVOS EN EL ESTACIONAMIENTO")
print("="*70)
print(f"{'Placa':<12} {'Propietario':<20} {'Tipo':<15} {'Hora Entrada':<15}")
print("-"*70)

for placa, vehiculo in vehiculos_activos.items():
    hora = vehiculo.hora_entrada.strftime("%H:%M:%S")
    print(f"{placa:<12} {vehiculo.propietario:<20} {vehiculo.tipo:<15} {hora:<15}")

print("="*70)
print(f"Total de vehículos: {len(vehiculos_activos)}\n")

# --- PRUEBA 3: Simular tiempo de estadía ---
print("[PRUEBA 3] Esperando 3 segundos para simular estadía...\n")
time.sleep(3)

# --- PRUEBA 4: Registrar salidas ---
print("[PRUEBA 4] Registrando salidas...\n")

v1.registrar_salida()
minutos1 = v1.calcular_permanencia()
registro.agregar('SALIDA', 'ABC-123', minutos1)
del vehiculos_activos["ABC-123"]
print(f"⏱️  Permanencia: {minutos1} segundos\n")

time.sleep(1)

v2.registrar_salida()
minutos2 = v2.calcular_permanencia()
registro.agregar('SALIDA', 'XYZ-789', minutos2)
del vehiculos_activos["XYZ-789"]
print(f"⏱️  Permanencia: {minutos2} segundos\n")

# --- PRUEBA 5: Ver vehículos activos (actualizado) ---
print("[PRUEBA 5] Vehículos aún activos:\n")
print("="*70)
print("VEHÍCULOS ACTIVOS EN EL ESTACIONAMIENTO")
print("="*70)
print(f"{'Placa':<12} {'Propietario':<20} {'Tipo':<15} {'Hora Entrada':<15}")
print("-"*70)

if vehiculos_activos:
    for placa, vehiculo in vehiculos_activos.items():
        hora = vehiculo.hora_entrada.strftime("%H:%M:%S")
        print(f"{placa:<12} {vehiculo.propietario:<20} {vehiculo.tipo:<15} {hora:<15}")
    print("="*70)
    print(f"Total de vehículos: {len(vehiculos_activos)}\n")
else:
    print("⚠️  No hay vehículos activos en el estacionamiento.\n")

# --- PRUEBA 6: Ver historial completo ---
print("[PRUEBA 6] Historial completo de movimientos:")
registro.mostrar()

print("✓ PRUEBAS COMPLETADAS EXITOSAMENTE\n")
