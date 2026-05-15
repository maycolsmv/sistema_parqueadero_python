import streamlit as st
import datetime

def agregar_placa(placa):
    with open("data/vehiculos.txt", "a") as archivo:
        archivo.write(f"{placa}\n")
    fecha_actual = datetime.datetime.now()
    with open("data/historial.txt", "a") as archivo_historial:
        archivo_historial.write(f"La placa {placa} ingreso: {fecha_actual}\n")

def mostrar_placas():
    with open("data/vehiculos.txt", "r") as archivo:
        return archivo.readlines()

def buscar_placa(placa):
    with open("data/vehiculos.txt", "r") as archivo:
        placas = archivo.read()
    return placa.strip() in [p.strip() for p in placas.splitlines()]

def eliminar_placa(placa):
    with open("data/vehiculos.txt", "r") as archivo:
        placas = archivo.readlines()
    nuevas_placas = [l for l in placas if l.strip() != placa.strip()]
    if len(nuevas_placas) < len(placas):
        with open("data/vehiculos.txt", "w") as archivo:
            archivo.writelines(nuevas_placas)
        fecha_actual = datetime.datetime.now()
        with open("data/historial.txt", "a") as archivo_historial:
            archivo_historial.write(f"La placa {placa} salio: {fecha_actual}\n")
        return True
    return False

def historial_placas():
    with open("data/historial.txt", "r") as archivo:
        return archivo.read()

# ── UI ──
st.title("🚗 Parqueadero")

tab1, tab2, tab3, tab4 = st.tabs(["Agregar", "Buscar", "Eliminar", "Historial"])

with tab1:
    st.subheader("Agregar vehículo")
    placa = st.text_input("Placa del vehículo:", key="agregar")
    if st.button("Agregar"):
        if placa:
            agregar_placa(placa.upper())
            st.success(f"Placa {placa.upper()} agregada correctamente")
        else:
            st.warning("Ingresa una placa primero")
    st.subheader("Placas en el parqueadero:")
    placas = mostrar_placas()
    if placas:
        for p in placas:
            st.write(f"🚘 {p.strip()}")
    else:
        st.info("No hay vehículos en el parqueadero")

with tab2:
    st.subheader("Buscar vehículo")
    placa_buscar = st.text_input("Placa a buscar:", key="buscar")
    if st.button("Buscar"):
        if placa_buscar:
            if buscar_placa(placa_buscar.upper()):
                st.success(f"✅ La placa {placa_buscar.upper()} SÍ está en el parqueadero")
            else:
                st.error(f"❌ La placa {placa_buscar.upper()} NO está en el parqueadero")
        else:
            st.warning("Ingresa una placa primero")

with tab3:
    st.subheader("Eliminar vehículo")
    placa_eliminar = st.text_input("Placa a eliminar:", key="eliminar")
    if st.button("Eliminar"):
        if placa_eliminar:
            if eliminar_placa(placa_eliminar.upper()):
                st.success(f"Placa {placa_eliminar.upper()} eliminada correctamente")
            else:
                st.error(f"La placa {placa_eliminar.upper()} no se encontró")
        else:
            st.warning("Ingresa una placa primero")

with tab4:
    st.subheader("Historial de entradas y salidas")
    historial = historial_placas()
    if historial:
        st.text(historial)
    else:
        st.info("El historial está vacío")