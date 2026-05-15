import funciones

def menu_principal():
    accion = 0 

    while accion != 6: 
        print ("¿Que accion quieres hacer?\n1. Agregar placa \n2. Mostrar placas \n3. Buscar placa \n4. Eliminar placa \n5. Ver historial \n6. Salir")

        try:
            accion = int(input("Elige una opcion: "))
        except ValueError:
            print("Por favor ingresa un numero valido.")
            continue

        if accion == 1:
            funciones.agregar_placa()
        
        elif accion == 2:
            funciones.mostrar_placas()

        elif accion == 3:
            funciones.buscar_placa()

        elif accion == 4:
            funciones.eliminar_placa()

        elif accion == 5:
            funciones.historial_placas()

        elif accion == 6: 
            print("¡Hasta la proxima!")
            break
        
        else:
            print("Opcion no valida, elige un numero entre 1 y 6.")