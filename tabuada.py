""" Imprime a tubuada do 1 ao 10"""
__version__ = "0.1.0"
__author__ = "Alex"

# numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))


# Iterable (percorriveis)

for numero in numeros:
    print("Tabuada do :", numero)
    for outro_numero in numeros:
        print("Resultado = ", numero * outro_numero)
    print("= "* 10)

# String
a = "Alex " * 10
for letra in a:
    print("--> ", letra)




     
