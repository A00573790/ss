import random

def pedir_numero():
    try:
        herramienta = int(input())
        boolean = 1
    except ValueError:
        boolean = 0
        herramienta = 1000000
        print("Jaja, eso no es un numero")
    return herramienta, boolean

print("Caja de herramientas de [tu nombre]")
print("Dile adios al Syntax Error!")
print("Que deseas hacer?")
print("0 - Imprimir una variable")
print("1 - Pedirle algo al usuario")
print("2 - Crear un condicional")
print("3 - Crear un ciclo while")
print("4 - Crear un ciclo for")
print("5 - Crear una lista")
print("6 - Divertirme")

boolean = 0
while boolean == 0:
    herramienta, boolean=pedir_numero()

while herramienta not in list(range(7)):
    print("Escribe un numero valido.")
    print(list(range(7)))
    herramienta, boolean=pedir_numero()
    while boolean == 0:
        herramienta, boolean=pedir_numero()

if herramienta == 0:
    print("Usa la función:")
    print("    print()")
    print("Dentro del paréntesis puedes poner ya sea un texto que quieras entre comillas (dobles o simples funciona bien) o una variable, yeii")
    print("Ejemplos:")
    print("    print('Que ondiux')")
    print("    print('Elegiste el número',numero)")
elif herramienta == 1:
    print("Usa la función:")
    print("    input()")
    print("Dentro del paréntesis puedes poner un texto indicando al usuario que debe de escribir, yeii")
    print("OJO: para usar el dato hay que meterlo dentro de una variable, y no olvides convertirlo al tipo de dato adecuado, awesome!")
    print("Los tipos de datos son número entero int(), número decimal float() y texto str()")
    print("Ejemplos:")
    print("    numero_entero = int(input())")
    print("    numero_decimal = float(input())")
    print("    texto = str(input())")
elif herramienta == 2:
  print("usa la funcion:")
  print( "if")
  print("despues del if debes esciibir la condicion que quieres que se cumpla para dar paso a una serie de acciones ") 
  print("el if funciona como concicional para restringir una accion amenos que se cumpla la condicion")
  print("ejemplos: ")
  print("if personas  >= 10 ")
  print(" print capacidad maxima")
  print("listo :3")
elif herramienta == 3:
  
  


elif herramienta == 6:
    aleatorio = random.randint(1,3)
    if aleatorio == 1:
        print("Las variables tipo float se llaman así porque en los decimales el punto flota, ja, que gracioso, no?")
    elif aleatorio == 2:
        print("Sabías que las computadoras no entienden las letras ni las palabras, solo entienden 0 y 1, imaginate hablar así, 000111000 jajaja que gracioso.")
    elif aleatorio == 3:
        print("Python tiene además de las listas, unas cosas llamadas tuplas, la única diferencia es que ocupan menos espacio en la memoria, jaja, que manera tan rara de ahorrar")
    
