import json 
import os 
import psycopg2 
from dotenv import load_dotenv





load_dotenv()

print("DB:", os.getenv("POSTGRES_DB"))
print("HOST:", os.getenv("POSTGRES_HOST"))
print("PORT:", os.getenv("POSTGRES_PORT"))