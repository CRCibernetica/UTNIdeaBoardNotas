# Tipos de datos (integrados)

# Booleanos
x = False
y = True

# Entero (integers)
z = 10
print(type(z))

# Decimal (float)
w = 12.34

# String (cadenas de caracteres)
texto = "hola"
texto2 = 'hola'

# Lista
animales = ["tigre", "leon", "leopardo", "pantera"]
numeros = [1, 7, 9, 15, 10]
loaquesea = [1, 5, "hola", [8,9,5]]

# Iteraciones de una lista
for animal in animales:
    print(animal)

# Iteraciones de una lista con indice
for indice, animal in enumerate(animales):
    print(indice, animal)

# Tupla es un lista pero no se puede modificar
coordinados = (10.5, -84.7, 931)
print(coordinados)

# Desempacar una Tupla
latitud, longitud, altura = coordinados
print(latitud)
print(longitud)
print(altura)

# Diccionario
direccion = {"calle":"Avenida 2",
             "ciudad":"San Jose"}

estudiante = {
    "nombre":"Jose",
    "tel":"5555-5555",
    "direccion":direccion
    }

# Acceder datos en un diccionario
nombre = estudiante["nombre"]
telefono = estudiante["tel"]
print(nombre)
print(telefono)
d = estudiante["direccion"]
print(d)







