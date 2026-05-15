import funciones

def menu_principal():
    accion = 0 

    while accion != 6: 
        print ("¿Que accion quieres hacer?\n1. Agregar placa \n2. Mostrar placas \n3. Buscar placa \n4. Eliminar placa \n5. Ver historial \n6. Salir")
        accion = int(input("Elige una opcion: "))

        if accion == 1:
            funciones.agregar_placa()
        
        if accion == 2:
            funciones.mostrar_placas()

        if accion == 3:
            funciones.buscar_placa()

        if accion == 4:
            funciones.eliminar_placa()

        if accion == 5:
            funciones.historial_placas()

        if accion == 6: 
            break