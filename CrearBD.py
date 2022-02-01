import sqlite3

miConexion = sqlite3.connect("players")

miCursor = miConexion.cursor()

miCursor.execute("CREATE TABLE playeridiom(CODIGO SERIAL PRIMARY KEY, NICKNAME VARCHAR(20), GEMS INTEGER, GOLDCOINS INTEGER, SCORE INTEGER, GEMSGAND INTEGER)")



miConexion.close()
