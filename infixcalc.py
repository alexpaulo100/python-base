""" Calculadora infix
Funcionamento:
[operação] [n1] [n2]
Operações:
sum -> +
sub -> -
mul -> *
div -> /


Uso: Exemplo
$ infixcalc.py sum 5 2
7

$ infixcalc.py 
operação: sum
n1: 5
n2: 4
9

Salvar resultados em log 

__version__ = "0.1.0"
__author__ = "Alex
"""
import os
import sys
from datetime import datetime

arguments = sys.argv[1:]

# Validação

if not arguments:
    operation = input("operação: ")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
elif len(arguments) !=3:
    print("Número de argumentos inválidos.")
    print("ex: `sum 5 5` ")
    sys.exit(1)

operation, *nums = arguments

validated_operations = ("sum", "sub", "mul", "div")
if operation not in validated_operations:
    print("Operação invalida")
    print(validated_operations)
    sys.exit(1)


validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Numero inválido {num}")
        sys.exit(1)

    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

try:
    n1, n2 = validated_nums
except ValueError as e:
    print(str(e))
    sys.exit(1)
    
# TODO: Usar dict de funções
if operation == "sum":
    result = n1 + n2
elif operation =="sub":
    result = n1 - n2
elif operation =="mul":
    result = n1 * n2
elif operation =="div":
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')



print(f"O resultado é = {result}")

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation}, {n1},{n2} = {result}\n")
except  PermissionError as e:
    print(str(e))
    sys.exit(1)



