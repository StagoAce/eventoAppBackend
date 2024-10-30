import pymongo
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()

# URL de conexión obtenida de variables de entorno
url = os.getenv("MONGODB_URL")
client = None

try:
    client = pymongo.MongoClient(url)
    db = client['Eventos']
    print("Conexión a MongoDB exitosa")
except pymongo.errors.ConnectionError as e:
    print(f"Error de conexión a MongoDB: {e}")
