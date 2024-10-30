from cassandra.cluster import Cluster

cluster = Cluster(['localhost'], port=9042)

session = cluster.connect()

try:
    session.execute("SELECT release_version FROM system.local")
    print("Conexión exitosa a Cassandra")
except Exception as e:
    print("Error conectando a Cassandra:", e)
finally:
    cluster.shutdown()