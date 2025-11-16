import redis
from conexion import baseDatosRedis as bd


#1. Crear registros clave-valor(0.25 puntos)
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
print("="*50)
print("1. Crear registros clave-valor\n")
print("Esta función introduce 10 intereses en Redis, cada uno con una clave única.")
print("Se almacenan las claves 'interes_1' a 'interes_10' con sus valores correspondientes.")
print("="*50)


# 2. Obtener y mostrar el número de claves registradas
claves = bd.keys("*")
total_claves = len(claves)

print("="*50)
print("2. Obtener y mostrar el número de claves registradas\n")
print(f"Total de claves registradas: {total_claves}")
print("="*50)

# 3. Obtener y mostrar un registro en base a una clave
clave = "interes_4" 
valor = bd.get(clave)

print("="*50)
print("3. Obtener y mostrar un registro por clave\n")
print(f"Busca la clave {clave} y muestra su valor.")
print(f"Clave: {clave}")
print(f"Valor: {valor}")
print("="*50)

# 4. Actualizar el valor de una clave y mostrar el nuevo valor
clave = "interes_4"  
nuevo_valor = "Fútbol"

bd.set(clave, nuevo_valor)

valor_actualizado = bd.get(clave)

print("="*50)
print("4. Actualizar el valor de una clave\n")
print(f"Clave: {clave}")
print(f"Nuevo valor: {valor_actualizado}")
print("="*50)

# 5. Eliminar una clave-valor y mostrar la clave y el valor eliminado

clave = "interes_4" 

valor_eliminado = bd.get(clave)

bd.delete(clave)

print("="*50)
print("5. Eliminar una clave-valor\n")
print(f"Clave eliminada: {clave}")
print(f"Valor eliminado: {valor_eliminado}")
print("="*50)

# 6. Obtener y mostrar todas las claves guardadas

claves = bd.keys("*")

print("="*50)
print("6. Obtener y mostrar todas las claves guardadas\n")
print("Claves:")
for clave in claves:
    print(f" - {clave}")
print("="*50)


# 7. Obtener y mostrar todos los valores guardados

claves = bd.keys("*")

valores = [bd.get(clave) for clave in claves]

print("="*50)
print("7. Obtener y mostrar todos los valores guardados\n")
print("Valores:")
for valor in valores:
    print(f" - {valor}")
print("="*50)

# 8. Obtener y mostrar varios registros con un patrón usando *

patron = "interes_*"

claves_filtradas = bd.keys(patron)

print("="*50)
print("8. Obtener y mostrar varios registros con patrón '*'\n")
print(f"Patrón usado: {patron}")
print("Claves y valores encontrados:")

for clave in claves_filtradas:
    valor = bd.get(clave)
    print(f" - {clave}: {valor}")

print("="*50)

# 9. Obtener y mostrar varios registros con un patrón usando []

patron = "interes_[1-3]"

claves_filtradas = bd.keys(patron)

print("="*50)
print("9. Obtener y mostrar varios registros con patrón '[]'\n")
print(f"Patrón usado: {patron}")
print("Claves y valores encontrados:")

for clave in claves_filtradas:
    valor = bd.get(clave)
    print(f" - {clave}: {valor}")

print("="*50)


