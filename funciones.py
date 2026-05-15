def agregar_placa():
    import datetime

    placa = input("Ingresa la placa del vehiculo: ")
    archivo = open("data/vehiculos.txt", "a")
    archivo.write(f"{placa} \n")
    archivo.close()

    fecha_actual = datetime.datetime.now()
    archivo_historial = open("data/historial.txt", "a")
    archivo_historial.write(f"La placa {placa} ingreso: {fecha_actual}\n")
    archivo_historial.close()

    print(f"Placa {placa} agregada correctamente")

def mostrar_placas():
    archivo = open("data/vehiculos.txt","r")
    contenido = archivo.read()
    print("Las placas actualmente en el parqueadero son:\n",contenido)
    archivo.close()

def buscar_placa():
    archivo = open("data/vehiculos.txt", "r")
    busqueda = archivo.read()
    buscar = input("Ingresa la placa que quieres buscar: ")
    
    if buscar in busqueda:
        print(f"El vehiculo con placa: {buscar}, si se encuentra en el parqueadero.")

    else:
        print(f"El vehiculo con placa: {buscar}, no se encuentra en el parqueadero.")

    archivo.close()

def eliminar_placa():
    print ("eliminar")

def historial_placas():
    archivo = open("data/historial.txt", "r")
    busqueda = archivo.read()
    print(busqueda)