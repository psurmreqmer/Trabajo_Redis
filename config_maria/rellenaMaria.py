from faker import Faker
import mysql.connector
import random

fake = Faker("es_ES")

# ---------- CONFIGURACIÓN DE CONEXIÓN A MARIADB ----------
try:
    conn = mysql.connector.connect(
        user="Usuario",
        password="Usuario",
        host="localhost",
        port=3306,
        database="estudiantes"
    )
    cursor = conn.cursor(dictionary=True)
    print("Conexión a MariaDB/MySQL exitosa")
except mysql.connector.Error as e:
    print(f"Error al conectar a MariaDB/MySQL: {e}")
    exit(1) 



# ---------- FUNCIÓN PARA INSERTAR EN MARIADB ----------
def insertar(query, values):
    cursor.execute(query, values)

# ---------- RELLENAR TABLAS ----------
print("Insertando datos...")

# Estudiantes
for _ in range(10):
    data = (
        fake.name(),
        random.randint(18, 30),
        random.choice(["Masculino", "Femenino", "Otro"]),
        random.choice(["Bajo", "Medio", "Alto"]),
        fake.address(),
        fake.sentence(),
        fake.date_this_decade()
    )
    insertar("""
        INSERT INTO estudiantes (nombre, edad, genero, nivel_socioeconomico, direccion, situacion_familiar, fecha_registro)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, data)

# Intereses
for _ in range(10):
    data = (fake.word(), fake.sentence())
    insertar("INSERT INTO intereses (nombre_interes, descripcion) VALUES (%s, %s)", data)

# Habilidades
for _ in range(10):
    data = (fake.word(), random.choice(["Técnica", "Social", "Creativa"]), fake.sentence())
    insertar("INSERT INTO habilidades (nombre_habilidad, tipo_habilidad, descripcion) VALUES (%s, %s, %s)", data)

# Formaciones
for _ in range(10):
    data = (
        fake.job(),
        random.randint(1, 10),
        random.choice(["Básico", "Medio", "Avanzado"]),
        random.randint(3, 24),
        fake.company(),
        fake.address(),
        random.randint(1, 50)
    )
    insertar("""
        INSERT INTO formaciones (nombre_formacion, area_id, nivel_requerido, duracion_meses, centro, direccion, provincia)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, data)

# Actividades Extraescolares
for _ in range(10):
    data = (
        fake.word(),
        random.choice(["Deporte", "Arte", "Música", "Voluntariado"]),
        f"{random.randint(1,12)} meses",
        fake.date_this_decade(),
        fake.date_this_decade()
    )
    insertar("""
        INSERT INTO actividades_extraescolares (nombre, tipo, duracion, fecha_ini, fecha_fin)
        VALUES (%s,%s,%s,%s,%s)
    """, data)

# Historial Académico
for _ in range(10):
    data = (
        random.randint(1, 10),
        fake.word(),
        round(random.uniform(5, 10), 2),
        fake.date_this_decade()
    )
    insertar("""
        INSERT INTO historial_academico (id_estudiante, nombre_curso, calificacion, fecha_finalizacion)
        VALUES (%s,%s,%s,%s)
    """, data)

# Estudiantes_Intereses
for _ in range(10):
    data = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 5))
    insertar("""
        INSERT INTO estudiantes_intereses (id_estudiante, id_interes, nivel_interes)
        VALUES (%s,%s,%s)
    """, data)

# Estudiante_Habilidades
for _ in range(10):
    data = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 5))
    insertar("""
        INSERT INTO estudiante_habilidades (id_estudiante, id_habilidad, nivel)
        VALUES (%s,%s,%s)
    """, data)

# Preferencias_Formaciones_Estudiantes
for _ in range(10):
    data = (
        random.randint(1, 10),
        random.randint(1, 10),
        random.choice(["Alta", "Media", "Baja"]),
        fake.date_this_decade()
    )
    insertar("""
        INSERT INTO preferencias_formaciones_estudiantes (id_estudiante, id_formacion, nivel_interes, fecha_registro)
        VALUES (%s,%s,%s,%s)
    """, data)

# Estudiantes_Actividades
for _ in range(10):
    data = (random.randint(1, 10), random.randint(1, 10), fake.date_this_decade())
    insertar("""
        INSERT INTO estudiantes_actividades (id_estudiante, id_actividad, fecha_inscripcion)
        VALUES (%s,%s,%s)
    """, data)

# ---------- CONFIRMAR ----------
conn.commit()
cursor.close()
conn.close()

print("Inserción completa en MariaDB.")