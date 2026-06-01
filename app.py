from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API de Gestión de Estudiantes")

# Modelo de datos
class Estudiante(BaseModel):
    id: int
    nombre: str
    curso: str
    calificacion_diagnostico: float

# Base de datos simulada
db_estudiantes = []

@app.get("/estudiantes", response_model=List[Estudiante])
def obtener_estudiantes():
    """Obtiene la lista completa de estudiantes."""
    return db_estudiantes

@app.post("/estudiantes", response_model=Estudiante, status_code=201)
def crear_estudiante(estudiante: Estudiante):
    """Registra un nuevo estudiante en el sistema."""
    for e in db_estudiantes:
        if e.id == estudiante.id:
            raise HTTPException(status_code=400, detail="El ID del estudiante ya existe")
    db_estudiantes.append(estudiante)
    return estudiante

@app.get("/estudiantes/{estudiante_id}", response_model=Estudiante)
def obtener_estudiante(estudiante_id: int):
    """Busca un estudiante específico por su ID."""
    for e in db_estudiantes:
        if e.id == estudiante_id:
            return e
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")