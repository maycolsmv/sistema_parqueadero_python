def agregar_placa():
    import datetime

    #Le pide al usuario la placa y la guarda en el archivo vehiculos
    placa = input("Ingresa la placa del vehiculo: ")
    archivo = open("data/vehiculos.txt", "a")
    archivo.write(f"{placa}\n")
    archivo.close()

    #Abre el archivo historial y guarda el registro
    fecha_actual = datetime.datetime.now()
    archivo_historial = open("data/historial.txt", "a")
    archivo_historial.write(f"La placa {placa} ingreso: {fecha_actual}\n")
    archivo_historial.close()

    print(f"Placa {placa} agregada correctamente")

def mostrar_placas():
    #Llama al archivo vehiculos e imprime las plcas guardadas 
    archivo = open("data/vehiculos.txt","r")
    contenido = archivo.read()
    archivo.close()
    print(f"Las placas actualmente en el parqueadero son:\n{contenido}")
    
def buscar_placa():
    #Abre el archivo y le pide al usuario la placa a buscar 
    archivo = open("data/vehiculos.txt", "r")
    busqueda = archivo.read()
    archivo.close()
    buscar = input("Ingresa la placa que quieres buscar: ")
    
    #Busca si la placa esta en el archivo
    if buscar in busqueda:
        print(f"El vehiculo con placa: {buscar}, si se encuentra en el parqueadero.")

    else:
        print(f"El vehiculo con placa: {buscar}, no se encuentra en el parqueadero.")

def eliminar_placa():
    import datetime

    #Le pide al usuario la placa a Eliminar
    placa = input("Ingresa la placa del vehiculo a eliminar: ")

    archivo = open("data/vehiculos.txt", "r")
    placas = archivo.readlines()
    archivo.close()

    placa_encontrada = False
    nuevas_placas = []

    #Busca si la placa existe
    for linea in placas:
        if linea.strip() == placa.strip():
            placa_encontrada = True
        else:
            nuevas_placas.append(linea)

    if placa_encontrada:
        # Reescribir el archivo 
        archivo = open("data/vehiculos.txt", "w")
        archivo.writelines(nuevas_placas)
        archivo.close()

        # Registrar en historial
        fecha_actual = datetime.datetime.now()
        archivo_historial = open("data/historial.txt", "a")
        archivo_historial.write(f"La placa {placa} salio: {fecha_actual}\n")
        archivo_historial.close()

        print(f"Placa {placa} eliminada correctamente.")
    else:
        print(f"La placa {placa} no se encontro en el parqueadero.")

def historial_placas():
    #Llama al archivo historial y imprime todo su contenido 
    archivo = open("data/historial.txt", "r")
    busqueda = archivo.read()
    archivo.close()
    print(busqueda)