# Interfaz de usuario con Streamlit

import streamlit as st
import requests

# Título del formulario de ingreso de datos al modelo
st.title("Predicción de Churn para Operadora de Telefonía Móvil")

with st.form("formulario"):
    EDAD = st.number_input("Edad", min_value=18, max_value=100)
    GENERO = st.selectbox("Género", ["mujer", "hombre", "otro"])
    ESTRATO_VIVIENDA = st.selectbox("Estrato de Vivienda", ["1", "2", "3", "4", "5", "6"])
    NIVEL_EDUCATIVO = st.selectbox("Nivel Educativo Alcanzado", ["primaria", "secundaria", "educacion superior"])
    TIPO_AREA_VIVIENDA = st.selectbox("Zona de la Vivienda", ["urbana", "rural"])
    SEGMENTO_PLAN = st.selectbox("Tipo de Plan Pospago", ["basico", "medio", "premium"])
    MIN_LLAMADAS_SEM = st.number_input("Minutos promedio de Llamadas en la semana", min_value=1)
    MIN_REDES_SOC_SEM = st.number_input("Minutos promedio de uso de Redes Sociales en la semana", min_value=1)
    MIN_WEB_SEM = st.number_input("Minutos promedio de uso de la Web en la semana", min_value=1)
    DIAS_PAGO_FACT = st.number_input("Días Pago en que demora en pagar la Factura", min_value=0)
    VECES_LLAM_COMPETENCIA = st.number_input("Veces en que recibió llamadas de la Competencia", min_value=0)
    MESES_SUSCRITO = st.number_input("Meses Suscrito al operador móvil", min_value=0)
    NUM_INTERRUPCIONES = st.number_input("Número de Interrupciones", min_value=0)
    DUR_INTERRUPCIONES = st.number_input("Duración de Interrupciones", min_value=0)
    SUSCRIP_STREAMING = st.selectbox("Suscripción a Streaming", ["si", "no"])

    submit_button = st.form_submit_button(label='Ingresar datos y predecir')

        # Definir la URL del endpoint de la API
        # PENDIENTE MODIFICAR
end_point_url = 'http://localhost:8000/prediccion'

# Realizar predicción
if submit_button:
    data = {"EDAD":  EDAD,
            "GENERO":  GENERO,
            "ESTRATO_VIVIENDA":  ESTRATO_VIVIENDA,
            "NIVEL_EDUCATIVO":  NIVEL_EDUCATIVO,
            "TIPO_AREA_VIVIENDA":  TIPO_AREA_VIVIENDA,
            "SEGMENTO_PLAN":  SEGMENTO_PLAN,
            "MIN_LLAMADAS_SEM":  MIN_LLAMADAS_SEM,
            "MIN_REDES_SOC_SEM":  MIN_REDES_SOC_SEM,
            "MIN_WEB_SEM":  MIN_WEB_SEM,
            "DIAS_PAGO_FACT":  DIAS_PAGO_FACT,
            "VECES_LLAM_COMPETENCIA":  VECES_LLAM_COMPETENCIA,
            "MESES_SUSCRITO":  MESES_SUSCRITO,
            "NUM_INTERRUPCIONES":  NUM_INTERRUPCIONES,
            "DUR_INTERRUPCIONES":  DUR_INTERRUPCIONES,
            "SUSCRIP_STREAMING":  SUSCRIP_STREAMING}
    # Hacer la solicitud POST a la API
    response = requests.post(end_point_url, json=data)
    prediction = response.json()['prediction']
    st.write(f'La predicción es: {prediction}')