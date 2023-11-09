import random

amigos = ["Jose", "Maria", "Sara", "Juan", "Marco"]
taza = amigos.copy()

# lista_final = {"Jose":"Sara", "Maria":"Marco", "Juan":"Jose"}
# lista_final["Juan"] = "Jose"

lista_final = {}

for amigo in amigos:
    continuar = False
    while not continuar:
        nombre = random.choice(taza)
        if amigo != nombre:
            print("Amigo invisible asignado")
            taza.remove(nombre)
            lista_final[amigo] = nombre
            continuar = True
        else:
            print("No se puede eligir su propio nombre")
            continuar = False
        
print(lista_final)