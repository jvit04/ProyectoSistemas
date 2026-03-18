import info_estudiantes
import info_proyecto
from vehiculo import Vehiculo
from registro_historial import RegistroHistorial
from simulacion_hilos import ejecutar_simulacion 

# Instancia global del registro de historial
registro = RegistroHistorial()
# Diccionario para almacenar vehículos activos en el estacionamiento
vehiculos_activos = {}


def menu_estacionamiento():
    """Menú de gestión del estacionamiento"""
    salir_submenu = False
    
    while not salir_submenu:
        print("\n" + "="*50)
        print("    GESTIÓN DE ESTACIONAMIENTO")
        print("="*50)
        print("\n  1. Registrar ingreso de vehículo")
        print("  2. Registrar salida de vehículo")
        print("  3. Ver historial de movimientos")
        print("  4. Ver vehículos activos")
        print("  5. Volver al menú principal\n")
        
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            print()
            placa = input("Ingrese placa del vehículo: ").upper()
            propietario = input("Ingrese nombre del propietario: ")
            
            print("\nTipos disponibles: auto, moto, camioneta")
            tipo = input("Ingrese tipo de vehículo: ").lower()
            
            if placa in vehiculos_activos:
                print(f"\n⚠️  El vehículo {placa} ya está registrado en el estacionamiento.\n")
            else:
                vehiculo = Vehiculo(placa, propietario, tipo)
                vehiculo.registrar_entrada()
                vehiculos_activos[placa] = vehiculo
                registro.agregar('INGRESO', placa)
                print()
        
        elif opcion == "2":
            print()
            placa = input("Ingrese placa del vehículo a retirar: ").upper()
            
            if placa not in vehiculos_activos:
                print(f"\n⚠️  El vehículo {placa} no se encuentra activo.\n")
            else:
                vehiculo = vehiculos_activos[placa]
                vehiculo.registrar_salida()
                segundos = vehiculo.calcular_permanencia()
                registro.agregar('SALIDA', placa, segundos)
                del vehiculos_activos[placa]
                print(f"✓ Tiempo de permanencia: {segundos} segundos\n")
        
        elif opcion == "3":
            print()
            registro.mostrar()
        
        elif opcion == "4":
            print()
            if not vehiculos_activos:
                print("⚠️  No hay vehículos activos en el estacionamiento.\n")
            else:
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
        
        elif opcion == "5":
            salir_submenu = True
        
        else:
            print("\n⚠️  Opción inválida. Intente de nuevo.\n")


def main():
    """Función principal con menú"""
    salir = False

    while not salir:
        print("\n" + "="*50)
        print("         MENÚ PRINCIPAL")
        print("="*50)
        print("\n  1. Mostrar nombres de estudiantes")
        print("  2. Mostrar descripción del proyecto")
        print("  3. Acceder a gestión de estacionamiento")
        print("  4. Ejecutar simulación caótica de hilos")
        print("  0. Salir\n")

        opcion = input("Ingrese su opción: ")


        elif opcion == "4":
            print()
            ejecutar_simulacion() 

        
        elif opcion == "0":
            print("\n" + "="*50)
            print("         Fin del programa.")
            print("="*50 + "\n")
            salir = True
        
        else:
            print("\n⚠️  Opción inválida. Intente de nuevo.\n")


if __name__ == "__main__":
    main()

