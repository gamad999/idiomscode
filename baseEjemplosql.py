import psycopg2

conexion1 = psycopg2.connect(database = "players", user = "postgres", password = "postgres")
cursor1 = conexion1.cursor()

sql = "insert into playeridiom(nickname, gems, goldcoins, score, cash) values(%s, %s, %s, %s, %s)"
datos = ("gamard54", 4, 0, 100, 100)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()