import sqlite3

try:
    conexion = sqlite3.connect("database//assets.db")
except Exception as ex:
    print(ex)
    
cursor = conexion.cursor()