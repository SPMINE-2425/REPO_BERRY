## Conexión a la API con sus endpoints

# Importar librerías
import pandas as pd
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os #<-- incluido para manejar la ruta de acuerdo con la estructura que dió el profe

# Crear la aplicación FastAPI
app = FastAPI()

# Definir el modelo de datos
class ChurnData(BaseModel):
    EDAD: int
    GENERO: str
    ESTRATO_VIVIENDA: str
    NIVEL_EDUCATIVO: str
    TIPO_AREA_VIVIENDA: str
    SEGMENTO_PLAN: str
    MIN_LLAMADAS_SEM: int
    MIN_REDES_SOC_SEM: int
    MIN_WEB_SEM: int
    DIAS_PAGO_FACT: int
    VECES_LLAM_COMPETENCIA: int
    MESES_SUSCRITO: int
    NUM_INTERRUPCIONES: int
    DUR_INTERRUPCIONES: int
    SUSCRIP_STREAMING: str

# Indicar la ruta de forma dinámica usando la ubicación del archivo actual (__file__)
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_modelo = os.path.join(ruta_actual, "..", "..", "data", "Processed", "pipeline.pkl")

# Cargar el modelo
modelo_cargado = joblib.load(ruta_modelo)

# Decoradores/endpoints:

# Decorador URL raíz (/)
# Trae el primer mensaje
@app.get("/")
def read_root():
    return {"Saludos": "Agente Comercial de operadora de Telefonía Móvil"}


# Decorador para la ruta [http://dominio.com/prediccion/]
# Recibe los datos y devuelve la predicción
@app.post("/prediccion/")
def predict_churn(item: ChurnData):
    X_new = pd.DataFrame([item.dict()]) 
    prediction = modelo_cargado.predict(X_new)
    return {'prediction': prediction.tolist()}