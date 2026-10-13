from bson import ObjectId
from src.models.database import collection
from src.models.model import traineeModel,traineeUpdateModel


def helper_trainee(trainee)-> dict:
  return {
    "id": str(trainee["_id"]),
    "document": trainee["document"],
    "firstName": trainee["firstName"],
    "lastName": trainee["lastName"],
    "email": trainee["email"],
    "age": trainee["age"],
    "programn": trainee["programn"],
    "record_number": trainee["record_number"]

  }
# crear datos de un aprendiz
def create_trainee(trainee: traineeModel)-> dict:
  trainee_dict  = trainee.model_dump() # es un metodo que me permite sanitizar los datos
  result = collection.insert_one(trainee_dict)
  new_trainee = collection.find_one({"_id": result.inserted_id})
  return helper_trainee(new_trainee)

#obtener todos los aprendices
def get_all_trainees():
  trainees = []
  for trainee in collection.find():
    trainees.append(helper_trainee(trainee))
  return trainees

#obtener datos de un aprendiz por su id
def get_trainee_by_ID(id:str):
  trainee = collection.find_one({"_id": ObjectId(id)})
  if trainee:
    return helper_trainee(trainee)
  return None

#actualizar datos de un aprendiz
def update_trainee(id:str, data:traineeUpdateModel):
  data_update = {k:v for k,v in data.model_dump().items() if v is not None}
  if data_update:
    collection.update_one({"_id": ObjectId(id)}, {"$set": data_update})
    trainee_upadated = collection.find_one({"_id": ObjectId(id)})
    return helper_trainee(trainee_upadated)
  return None

#Eliminar datos del aprendiz
def delete_trainee(id:str):
  trainee = collection.find_one({"_id": ObjectId(id)})
  if trainee:
    collection.delete_one({"_id": ObjectId(id)})
    return True
  return False


