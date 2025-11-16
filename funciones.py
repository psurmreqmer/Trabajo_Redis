import redis
from conexion import *

# =====================================================
# PRIMERA PARTE
# =====================================================        

# =====================================================
# 1. Crear registros clave-valor
# =====================================================
def crear_registros():
    #Intereses
    bd.set("interes_1", "Programación")
    bd.set("interes_2", "Deporte")
    bd.set("interes_3", "Arte")
    bd.set("interes_4", "Música")
    bd.set("interes_5", "Videojuegos")
    bd.set("interes_6", "Cocina")
    bd.set("interes_7", "Idiomas")
    bd.set("interes_8", "Lectura")
    bd.set("interes_9", "Robótica")
    bd.set("interes_10", "Diseño")
    #Notas de corte grados
    bd.set("grado_dam_nota", 7.5)
    bd.set("grado_electricidad_nota", 6.8)
    bd.set("grado_mecanica_nota", 7.2)
    bd.set("grado_quimica_nota", 8.0)
    bd.set("grado_informatica_nota", 7.9)

    print("="*50)
    print("1. Crear registros clave-valor\n")
    print("Introduce 10 intereses y 10 notas de corte en Redis, cada uno con una clave única.")
    print("Se almacenan las claves con sus valores correspondientes.")
    print("="*50)

# =====================================================
# 2. Obtener y mostrar el número de claves registradas
# =====================================================
def mostrar_numero_claves():
    claves = bd.keys("*")
    total_claves = len(claves)
    print("="*50)
    print("2. Obtener y mostrar el número de claves registradas\n")
    print(f"Total de claves registradas: {total_claves}")
    print("="*50)

# =====================================================
# 3. Obtener y mostrar un registro en base a una clave
# =====================================================
def mostrar_registro_por_clave():
    clave = "interes_4" 
    valor = bd.get(clave)
    print("="*50)
    print("3. Obtener y mostrar un registro por clave\n")
    print(f"Busca la clave {clave} y muestra su valor.")
    print(f"Clave: {clave}")
    print(f"Valor: {valor}")
    print("="*50)

# =====================================================
# 4. Actualizar el valor de una clave y mostrar el nuevo valor
# =====================================================
def actualizar_valor_clave():
    clave = "interes_4"  
    valor = bd.get(clave)
    nuevo_valor = "Fútbol"
    bd.set(clave, nuevo_valor)
    valor_actualizado = bd.get(clave)
    print("="*50)
    print("4. Actualizar el valor de una clave\n")
    print(f"Cambia el valor de {clave} de {valor} a {valor_actualizado}.")
    print(f"Clave: {clave}")
    print(f"Nuevo valor: {valor_actualizado}")
    print("="*50)

# =====================================================
# 5. Eliminar una clave-valor y mostrar la clave y el valor eliminado
# =====================================================
def eliminar_clave():
    clave = "interes_4" 
    valor_eliminado = bd.get(clave)
    bd.delete(clave)
    print("="*50)
    print("5. Eliminar una clave-valor\n")
    print(f"Borra la clave {clave} y muestra el valor que tenía antes.")
    print(f"Clave eliminada: {clave}")
    print(f"Valor eliminado: {valor_eliminado}")
    print("="*50)

# =====================================================
# 6. Obtener y mostrar todas las claves guardadas
# =====================================================
def mostrar_todas_claves():
    claves = bd.keys("*")
    print("="*50)
    print("6. Obtener y mostrar todas las claves guardadas\n")
    print("Obtiene todas las claves de Redis.")
    print("Claves:")
    for clave in claves:
        print(f" - {clave}")
    print("="*50)

# =====================================================
# 7. Obtener y mostrar todos los valores guardados
# =====================================================
def mostrar_todos_valores():
    claves = [c for c in bd.keys("*") if not c.endswith("_json") and not c.endswith("_list")if not c.startswith("estudiante")]
    valores = [bd.get(clave) for clave in claves]
    print("="*50)
    print("7. Obtener y mostrar todos los valores guardados\n")
    print("Obtiene el valor de cada clave existente.")
    print("Valores:")
    for valor in valores:
        print(f" - {valor}")
    print("="*50)

# =====================================================
# 8. Obtener y mostrar varios registros con un patrón usando *
# =====================================================
def mostrar_patron_asterisco():
    patron = "interes_*"
    claves_filtradas = bd.scan_iter(patron)
    print("="*50)
    print("8. Obtener y mostrar varios registros con patrón '*'\n")
    print("Busca todas las claves que empiecen por 'interes_' y muestra su valor.")
    print(f"Patrón usado: {patron}")
    print("Claves y valores encontrados:")
    for clave in claves_filtradas:
        valor = bd.get(clave)
        print(f" - {clave}: {valor}")
    print("="*50)

# =====================================================
# 9. Obtener y mostrar varios registros con un patrón usando []
# =====================================================
def mostrar_patron_corchetes():
    patron = "interes_[1-3]"
    claves_filtradas = bd.scan_iter(patron)
    print("="*50)
    print("9. Obtener y mostrar varios registros con patrón '[]'\n")
    print("Busca las claves 'interes_1' a 'interes_3' usando [] y muestra sus valores.")
    print(f"Patrón usado: {patron}")
    print("Claves y valores encontrados:")
    for clave in claves_filtradas:
        valor = bd.get(clave)
        print(f" - {clave}: {valor}")
    print("="*50)

# =====================================================
# 10. Obtener y mostrar varios registros con un patrón usando ?
# =====================================================
def mostrar_patron_interrogacion():
    patron = "interes_?"
    claves_filtradas = bd.scan_iter(patron)
    print("10. Obtener y mostrar varios registros con patrón '?'\n")
    print("Busca todas las claves con un solo carácter después de 'interes_', por ej. no debería devolver interes_10.")
    print(f"Patrón usado: {patron}")
    print("Claves y valores encontrados:")
    for clave in claves_filtradas:
        valor = bd.get(clave)
        print(f" - {clave}: {valor}")
    print("="*50)

# =====================================================
# 11. Obtener y mostrar varios registros y filtrarlos por un valor en concreto
# =====================================================
def filtrar_valores_por_valor():
    valor_buscado = "Arte"  # valor que queremos filtrar
    claves_filtradas = [clave for clave in bd.scan_iter("*") if not clave.endswith("_json") if not clave.startswith("estudiante") and not clave.endswith("_list") and bd.get(clave) == valor_buscado]
    
    print("="*50)
    print("11. Obtener y mostrar registros filtrados por un valor concreto\n")
    print(f"Busca todas las claves cuyo valor sea exactamente '{valor_buscado}'.")
    print("Claves y valores encontrados:")
    
    for clave in claves_filtradas:
        valor = bd.get(clave)
        print(f" - {clave}: {valor}")
    
    print("="*50)
# =====================================================
# 12. Actualizar una serie de registros en base a un filtro
# =====================================================
def actualizar_notas():
    
    print("="*50)
    print("12. Actualizar una serie de registros en base a un filtro\n")
    print("Incrementa en 1 punto todas las notas medias menores de 8.")
    
    claves = bd.scan_iter("grado_*_nota")
    
    for clave in claves:
        valor_actual = float(bd.get(clave))
        if valor_actual < 8:
            nuevo_valor = round(valor_actual + 1, 1)
            bd.set(clave, nuevo_valor)
            print(f" - {clave}: {valor_actual} -> {nuevo_valor}")
        else:
            print(f" - {clave}: {valor_actual}")
    
    print("="*50)

# =====================================================
# 13. Eliminar una serie de registros en base a un filtro
# =====================================================
def eliminar_notas_bajas():
    print("="*50)
    print("13. Eliminar una serie de registros en base a un filtro\n")
    print("Elimina todas las notas medias menores de 8 de los registros de Redis.")
    
    # Buscamos todas las claves que terminan con '_nota'
    claves = bd.scan_iter("grado_*_nota")
    
    for clave in claves:
        valor = float(bd.get(clave))
        if valor < 8:
            bd.delete(clave)
            print(f" - Clave eliminada: {clave}, Valor eliminado: {valor}")
        else:
            print(f" - Clave conservada: {clave}, Valor: {valor}")
    
    print("="*50)

# =====================================================
# 14. Crear una estructura en JSON de array de habilidades
# =====================================================
def crear_json_habilidades():
    print("="*50)
    print("14. Crear una estructura en JSON de array de habilidades\n")
    print("Esta función crea un array de habilidades y lo guarda directamente en Redis usando RedisJSON.")
    
    # Creamos un array vacío en Redis
    bd.json().set("habilidades_json", "$", [])

    # Añadimos habilidades al array
    bd.json().arrappend("habilidades_json", "$", {"nombre_habilidad": "Programación", "tipo_habilidad": "Tecnológica", "descripcion": "Capacidad de desarrollar software"})
    bd.json().arrappend("habilidades_json", "$", {"nombre_habilidad": "Electricidad", "tipo_habilidad": "Técnica", "descripcion": "Instalación y mantenimiento de sistemas eléctricos"})
    bd.json().arrappend("habilidades_json", "$", {"nombre_habilidad": "Diseño Gráfico", "tipo_habilidad": "Creativa", "descripcion": "Creación de elementos visuales"})
    bd.json().arrappend("habilidades_json", "$", {"nombre_habilidad": "Mecánica", "tipo_habilidad": "Técnica", "descripcion": "Reparación y mantenimiento de maquinaria"})
    bd.json().arrappend("habilidades_json", "$", {"nombre_habilidad": "Idiomas", "tipo_habilidad": "Social", "descripcion": "Capacidad de comunicarse en varios idiomas"})
    
    print("Array JSON de habilidades guardado en Redis bajo la clave 'habilidades_json'.")
    print("="*50)

# =====================================================
# 15. Realizar un filtro por cada atributo del JSON
# =====================================================
def filtrar_habilidades_json():
    print("="*50)
    print("15. Filtrar habilidades por cada atributo usando JSONPath\n")

    # 1. Filtrar por nombre_habilidad
    print("\nFiltrar por nombre_habilidad = 'Programación':")
    res1 = bd.json().get("habilidades_json", '$[?(@.nombre_habilidad == "Programación")]')
    print(res1)

    # 2. Filtrar por tipo_habilidad
    print("\nFiltrar por tipo_habilidad = 'Técnica':")
    res2 = bd.json().get("habilidades_json", '$[?(@.tipo_habilidad == "Técnica")]')
    print(res2)

    # 3. Filtrar por descripcion (ejemplo: contiene 'mantenimiento')
    print("\nFiltrar por descripcion que sea exactamente 'Instalación y mantenimiento de sistemas eléctricos':")
    res3 = bd.json().get("habilidades_json", '$[?(@.descripcion == "Instalación y mantenimiento de sistemas eléctricos")]')
    print(res3)

    print("="*50)
    
# =====================================================
# 16. Crear una lista en Redis
# =====================================================
def crear_lista():
    print("="*50)
    print("16. Crear una lista en Redis\n")
    
    # Eliminar lista si ya existe
    bd.delete("cursos_favoritos_list")

    # Añadir elementos a la lista
    bd.lpush("cursos_favoritos_list", "Matemáticas:1")
    bd.lpush("cursos_favoritos_list", "Física:2")
    bd.lpush("cursos_favoritos_list", "Química:3")
    bd.lpush("cursos_favoritos_list", "Programación:4")
    bd.lpush("cursos_favoritos_list", "Diseño:5")

    #mostrar
    lista = bd.lrange("cursos_favoritos_list", 0, -1)
    print("Lista de cursos favoritos:")
    for elemento in lista:
        print(f" - {elemento}")

# =====================================================
# 17. Obtener elementos de una lista con un filtro en concreto
# =====================================================
def filtrar_lista():
    print("="*50)
    print("17. Obtener elementos de la lista 'cursos_favoritos_list' cuyo número sea mayor que 3\n")

    # Obtener todos los elementos de la lista
    lista = bd.lrange("cursos_favoritos_list", 0, -1)

    # Filtrar elementos cuyo número (después de ':') sea mayor que 3
    filtrados = [elem for elem in lista if int(elem.split(":")[1]) > 3]

    print("Elementos filtrados (número > 3):")
    for elem in filtrados:
        print(f" - {elem}")

    print("="*50)

# =====================================================
# 18. Crear datos con índices definiendo un esquema de al menos tres campos
# =====================================================
def crear_estudiantes_con_indice():
    print("="*50)
    print("18. Crear datos de estudiantes con índice en Redis\n")


    # Creamos algunos estudiantes como objetos JSON
    estudiante1 = {
        "nombre": "Ana López",
        "edad": 21,
        "ciudad": "Madrid",
        "curso": "Matemáticas"
    }

    estudiante2 = {
        "nombre": "Carlos Pérez",
        "edad": 24,
        "ciudad": "Barcelona",
        "curso": "Física"
    }

    estudiante3 = {
        "nombre": "Lucía Gómez",
        "edad": 22,
        "ciudad": "Valencia",
        "curso": "Programación"
    }

    # Guardamos los estudiantes en RedisJSON
    bd.json().set("estudiantes:1", Path.root_path(), estudiante1)
    bd.json().set("estudiantes:2", Path.root_path(), estudiante2)
    bd.json().set("estudiantes:3", Path.root_path(), estudiante3)

    print("Datos de estudiantes guardados bajo claves 'estudiantes:1', 'estudiantes:2', 'estudiantes:3'")
    print("="*50)


# =====================================================
# 19. Realizar una búsqueda con índices en base a un campo
# =====================================================
def buscar_estudiantes():
    print("="*50)
    print("19. Buscar estudiantes de Madrid usando el índice\n")

    resultados = bd.ft("indice:estudiantes").search('@ciudad:{Madrid}')

    print(resultados)
    print("="*50)


# =====================================================
# 20. Realiza un group  by usando los índices
# =====================================================
def groupby_estudiantes():
    print("="*50)
    print("20. Group by: contar estudiantes por ciudad usando índice\n")

    # Creamos la agregación
    groupby = aggregations.AggregateRequest("*").group_by(
        '@ciudad', reducers.count().alias('count')
    )

    # Ejecutamos la agregación usando el índice de estudiantes
    resultado = bd.ft("indice:estudiantes").aggregate(groupby)

    resultado = bd.ft("indice:estudiantes").aggregate(groupby).rows
    print(resultado)
# =====================================================
# SEGUNDA PARTE
# =====================================================

# =====================================================
# 21. Obtener datos de MariaDB y guardarlos en Redis
# =====================================================
def importar_estudiantes_mariadb():
    print("="*50)
    print("21. Importar estudiantes desde MariaDB a Redis\n")

    # Conectar a MariaDB
    conn, cursor = conexion_mariadb()
    if conn is None:
        return

    # Obtener los estudiantes
    cursor.execute("""
        SELECT id, nombre, edad, genero, nivel_socioeconomico, direccion, situacion_familiar
        FROM estudiantes
    """)
    estudiantes = cursor.fetchall()

    # Guardar cada estudiante en Redis
    for est in estudiantes:
        clave_redis = f"estudiantes_db:{est['id']}"
        bd.json().set(clave_redis, '$', est)
        print(f" - Guardado en Redis: {clave_redis} -> {est['nombre']}")

    cursor.close()
    conn.close()
    print(f"\nTotal de estudiantes importados: {len(estudiantes)}")
    print("="*50)

# =====================================================
# 22. Exportar nombre y edad de estudiantes desde Redis a MariaDB
# =====================================================
def exportar_a_mariadb():
    print("="*50)
    print("22. Exportar nombre y edad de estudiantes desde Redis a MariaDB\n")

    # Conectar a MariaDB
    conn, cursor = conexion_mariadb()
    if conn is None:
        return

    # Obtener claves de estudiantes en Redis
    claves_redis = bd.keys("estudiantes:*")
    total = 0

    for clave in claves_redis:
        estudiante = bd.json().get(clave, '$')[0]  # bd.json().get devuelve lista
        # Preparar inserción en MariaDB (solo nombre y edad)
        try:
            cursor.execute("""
                INSERT INTO estudiantes (nombre, edad)
                VALUES (%s, %s)
            """, (
                estudiante.get('nombre'),
                estudiante.get('edad')
            ))
            total += 1
            print(f" - Insertado en MariaDB: {estudiante.get('nombre')} ({estudiante.get('edad')} años)")
        except Exception as e:
            print(f"Error insertando {estudiante.get('nombre')}: {e}")

    conn.commit()
    cursor.close()
    conn.close()
    print(f"\nTotal de estudiantes exportados a MariaDB: {total}")
    print("="*50)


# ========================================