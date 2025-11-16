import redis
import mariadb
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers


# ----------------------------
# Conexión a Redis
# ----------------------------
conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
bd = redis.Redis(connection_pool=conexionRedis)

if bd.ping():
    print("Conexión a Redis exitosa")
else:
    print("No se pudo conectar a Redis")

# ----------------------------
# Esquema de estudiantes
# ----------------------------
esquema = (
    TextField("$.nombre", as_name="nombre"),
    TagField("$.ciudad", as_name="ciudad"),
    NumericField("$.edad", as_name="edad"),
    TextField("$.curso", as_name="curso")
)

try:
    bd.ft("indice:estudiantes").create_index(
        esquema,
        definition=IndexDefinition(
            prefix=["estudiantes:"],
            index_type=IndexType.JSON
        )
    )
    print("Índice 'indice:estudiantes' creado correctamente")
except Exception as e:
    print(f"El índice ya existe o hubo un error: {e}")


# ----------------------------
# Función para conectar a MariaDB
# ----------------------------
def conexion_mariadb():
    try:
        conn = mariadb.connect(
            user="Usuario",
            password="Usuario",
            host="localhost",
            port=3307,
            database="estudiantes"
        )
        cursor = conn.cursor(dictionary=True)
        print("Conexión a MariaDB exitosa")
        return conn, cursor
    except mariadb.Error as e:
        print(f"Error al conectar a MariaDB: {e}")
        return None, None
