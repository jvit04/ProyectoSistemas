import info_estudiantes
import info_proyecto

salir = 0
while salir == 0:
    print("\n" + "="*50)
    print("         MENÚ PRINCIPAL")
    print("="*50)
    print("\n  1. Mostrar nombres de estudiantes")
    print("  2. Mostrar descripción del proyecto")
    print("  0. Salir\n")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        print()
        info_estudiantes.nombre_estudiantes()
    elif opcion == "2":
        print()
        info_proyecto.descripcion_proyecto()
    elif opcion == "0":
        print("\n" + "="*50)
        print("         Fin del programa.")
        print("="*50 + "\n")
        salir = 1
    else:
        print("\n⚠️  Opción inválida. Intente de nuevo.\n")

