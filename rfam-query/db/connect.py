import mysql.connector
from config import Config

def get_connection():
    return mysql.connector.connect(
        user=Config.USER,
        password=Config.PASSWORD,
        host=Config.HOST,
        port=Config.PORT,
        database=Config.DATABASE
    )