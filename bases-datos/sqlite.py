# importar modulo
import sqlite3

# conexión
conexion = sqlite3.connect('pruebas.db')

# crear cursor
# permite ejecutar consultas
cursor = conexion.cursor()

# crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos(" +
               "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "titulo VARCHAR(255), " +
               "descripcion text, " +
               "precio int(255) " +
               ")")

# otra forma de ordenar mejor es
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
titulo VARCHAR(255), 
descripcion text, 
precio int(255) 
)""")

# Guardar cambios
conexion.commit()


# Insertar datos
'''
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripcion del productoro', 556)")
conexion.commit()
'''


#borrar registros
cursor.execute("DELETE FROM productos")

#Insertar muchos registros de golpe
productos = [
    ( "Ordenador A", "Bunea compra", 400),
    ( "Ordenador B", "exelente compra", 3400),
    ( "Ordenador C", "nada mal la compra", 344),
    ( "Ordenador D", "Bunea compra", 500),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?,?,?)", productos)

conexion.commit()
#Update
cursor.execute("UPDATE productos SET precio=333 WHERE precio=400")

# Leer datos
cursor.execute("SELECT * FROM productos")
print(cursor)
productos = cursor.fetchall()
# print(productos)
for producto in productos:
    print("Titulo:", producto[1])
    print("Descripción:", producto[2])
    print('----------------------------')


cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone()
print(producto)




# cerrar conexión
conexion.close()
