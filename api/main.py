from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import re
from api.utils import jugadores_info, goals_info, goals_by_country,goles_por_equipo, top_goleadores


# Crear la instancia de FastAPI
app = FastAPI()

# Cargar los datos
df=pd.read_csv('datos/goleadores.csv')

# Modelo de Pydantic para la validación de datos
class Player(BaseModel):
    name: str
    team: str
    country: str
    team_nationality: str
    goals: int
    penalty_goals: int

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/players/")
def read_players():
    return df.to_dict(orient='records')

@app.get("/players/{player_name}")
def read_player(player_name: str):
    player_data = jugadores_info
    if player_data:
        return player_data
    return {"error": "Player not found"}

@app.get("/goalsinfo/{position}")
def get_goals_rank(position: int):
    """
    Retorna el país y goles acumulados en la 'position' del ranking (1 = primer lugar).
    """
    goals_data = goals_info(position)
    
    if goals_data:
        return goals_data
    return {"error": "Goals not found"}

@app.get("/goalsbycountry")
def get_goals_by_country():
    """
    Retorna el total de goles acumulados por cada país en un arreglo.
    """
    return goals_by_country(df)

@app.get("/goalsrankplayers")
def top_goleadores():
    """
    Retorna el total de goles acumulados por cada país en un arreglo.
    """
    return top_goleadores(df)

@app.get("/teamsgoals")
def goles_por_equipo():
    return goles_por_equipo()