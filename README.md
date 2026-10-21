# 🎓 API de Aprendices

API sencilla hecha con **FastAPI** para gestionar los datos de aprendices: crear, ver, actualizar y eliminar. Guarda la información en **MongoDB Atlas** y está desplegada en **Render**. 🚀

🌐 **API en línea:** https://first-proejct-in-fastapi.onrender.com
📖 **Documentación:** https://first-proejct-in-fastapi.onrender.com/docs

> ⏳ Usa el plan gratis de Render, así que la primera petición puede tardar hasta un minuto en responder.

## 🛠️ Tecnologías

- 🐍 Python
- ⚡ FastAPI
- ✅ Pydantic y email-validator
- 🦄 Uvicorn
- 🍃 MongoDB Atlas con PyMongo
- 📡 requests y httpx
- ☁️ Render

## 📁 Estructura del proyecto

```
t1_fastAPI/
├── data/
├── src/
│   ├── main.py              # Rutas de la API
│   ├── models/
│   │   ├── database.py      # Conexión a MongoDB
│   │   └── model.py         # Modelos de datos
│   ├── templates/
│   │   └── controllers.py   # Lógica del CRUD
│   └── views/
│       └── view.py          # Consumo de la API por consola (CLI)
├── test/
│   └── test_main.py
├── requirements.txt
├── structure.sh
└── README.md
```

## 🔗 Endpoints

| Método | Ruta | Qué hace |
|--------|------|----------|
| GET | `/` | Mensaje de bienvenida 👋 |
| GET | `/trainee/` | Ver todos los aprendices 📋 |
| POST | `/trainee/` | Registrar un aprendiz ➕ |
| GET | `/trainee/{id}` | Ver un aprendiz por su id 🔍 |
| PUT | `/trainee/{id}` | Actualizar un aprendiz ✏️ |
| DELETE | `/trainee/{id}` | Eliminar un aprendiz 🗑️ |

## 🧾 Datos de un aprendiz

```json
{
  "document": "1234567890",
  "firstName": "Juan",
  "lastName": "Pérez",
  "email": "juan@example.com",
  "age": 22,
  "programn": "Software developer",
  "record_number": 1
}
```

🍃 Base de datos: `data_ap` · Colección: `trainee`

## 💻 Correrlo en tu computador

1. Clona el proyecto:
```
   git clone https://github.com/juanpablozapatagonsales-prog/t1_fastAPI.git
   cd t1_fastAPI
```
2. Crea y activa el entorno virtual:
```
   python -m venv venv
   venv\Scripts\activate
```
3. Instala las librerías:
```
   pip install -r requirements.txt
```
4. Crea un archivo `.env` con la conexión a tu MongoDB Atlas:
```
   MONGO_URI="mongodb+srv://juanpablozapatagonsales_db_user:8XY747K70EzLYcVl@clusterapi.ln61rig.mongodb.net/?appName=Taller1_fastAPI"
```
   🔒 Este archivo no se sube a GitHub.
5. Arranca el servidor:
```
   uvicorn src.main:app --reload
```
6. Abre http://127.0.0.1:8000/docs para probar la API. 🎉

## ☁️ Despliegue en Render

1. Sube el proyecto a GitHub.
2. En Render crea un **Web Service** y conecta el repositorio.
3. Configura:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn src.main:app --host 0.0.0.0 --port $PORT`
4. En **Environment** agrega la variable `MONGO_URI` con tu conexión de Atlas.
5. En MongoDB Atlas, entra a **Network Access** y permite la conexión desde Render.
6. Cada `git push` vuelve a desplegar la API automáticamente. 🔄

## 🖥️ Consumir la API desde la consola (CLI)

Con el entorno virtual activo:

```
python src/views/view.py
```

Sale un menú para ver todos, ver uno por id, crear, actualizar y eliminar aprendices. 🕹️

## 👨‍💻 Autor

[juanpablozapatagonsales-prog](https://github.com/juanpablozapatagonsales-prog)

Proyecto de práctica para aprender FastAPI. 💪
