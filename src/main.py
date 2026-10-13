#importamos los controladores y modelos
from src.templates.controllers import create_trainee, get_all_trainees, get_trainee_by_ID, update_trainee, delete_trainee
from src.models.model import traineeModel, traineeUpdateModel
from fastapi import FastAPI, HTTPException,status
#  python -m uvicorn src.main:app --reload  para arrancar el servidor
app = FastAPI(
  title = "Gestion de datos de los aprendices",
  description = "API simple con FastAPI para consumir los datos con los aprendices",
  version = "1.0.0"
)
#mensaje de bienvenida
@app.get("/")
async def root():
  return {"message": "API simple con FastAPI"}

#Registrar aprendices
@app.post(
  "/trainee/",response_description="registrar un nuevo aprendiz",
  status_code=status.HTTP_201_CREATED,
)

def create_trainee_API(trainee:traineeModel):
  #validar si ya existe el documento
  return create_trainee(trainee)

#obtener la lista de aprendizes
@app.get(
   "/trainee/",response_description="listar todos los aprendizes"
)
def get_all_trainees_API():
  return get_all_trainees()

#obtener aprendiz por su id
@app.get(
  "/trainee/{id}",response_description="obtener un aprendiz por su id"

)
def get_trainee_by_ID_API(id:str):
  trainee = get_trainee_by_ID(id)
  if not trainee:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Aprendiz con id {id} no encontrado")
  return trainee

#Update un aprendiz por su id
@app.put(
  "/trainee/{id}",response_description=" Update DATA de un aprendiz por su id"
)
def update_trainee_API(id:str, trainee:traineeUpdateModel):
  trainee = update_trainee(id,trainee)
  if not trainee:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Aprendiz no encontrado o sin datos que actualizar")
  return trainee

#eliminar un aprendiz por su id
@app.delete(
  "/trainee/{id}",response_description="eliminar un aprendiz por su id"
)
def delete_trainee_API(id:str):
  trainee = delete_trainee(id)
  if not trainee:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Aprendiz con id {id} a sido eliminado.")
  return {"message":f"aprendiz eliminado con exito."}
