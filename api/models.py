from django.db import models
from db_connection import db

# Create your models here.
user_collection = db['Users']
evento_collection = db['Eventos']
