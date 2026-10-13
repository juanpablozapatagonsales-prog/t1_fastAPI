#importamos los controladores y modelos
from src.templates.controllers import create_trainee, get_all_trainees, get_trainee_by_ID, update_trainee, delete_trainee
from src.models.model import traineeModel, traineeUpdateModel
from fastapi import FastAPI, HTTPException,status
#  src.main:app --reload para arrancar el servidor
app = FastAPI(
  title = "Gestion de datos de los aprendices",
  description = "API simple con FastAPI para consumir los datos con los aprendices",
  version = "1.0.0"
)
@app.get("/")
async def root():
  return {"message": "Hello world"}
