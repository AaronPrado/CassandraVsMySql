import mysql.connector
import pandas as pd
import time

# 1. Conectar a la base de datos MySQL
conn = mysql.connector.connect(
    host='localhost',        # Cambia esto si tu MySQL está en otro host
    user='root',             # Tu usuario MySQL
    password='Abc123',       # Tu contraseña
    database='mydatabase'    # El nombre de tu base de datos
)

# 2. Crear un cursor
cursor = conn.cursor()

# 3. Definir las consultas SQL que quieras medir
queries = [
    "SELECT COUNT(*) FROM contactos;",  # Conteo de registros
    "SELECT * FROM contactos LIMIT 10;",  # Obtener los primeros 10 registros
    "SELECT direccion  FROM contactos  WHERE direccion like '%example.org';"  # Filtrado por correo
]

# 4. Medir el tiempo de ejecución de cada consulta
for query in queries:
    print(f"\nEjecutando consulta: {query}")
    
    # Iniciar temporizador
    start_time = time.time()

    # Ejecutar consulta
    cursor.execute(query)
    result = cursor.fetchall()  # Obtener los resultados

    # Detener temporizador
    end_time = time.time()

    # Mostrar algunos resultados y tiempo de ejecución
    print(f"Primeros resultados: {result[:5]}")  # Mostrar los primeros 5 resultados
    print(f"Tiempo de ejecución: {end_time - start_time} segundos\n")

# 5. Usar pandas para ver los resultados de una consulta compleja
query = "SELECT * FROM contactos LIMIT 10;"
start_time = time.time()

# Usar pandas para ejecutar la consulta directamente
df = pd.read_sql(query, conn)

# Finalizar temporizador
end_time = time.time()
print(f"Consulta ejecutada en: {end_time - start_time} segundos")

# Mostrar el DataFrame con los primeros 5 registros
df.head()

# 6. Cerrar la conexión al finalizar
cursor.close()
conn.close()