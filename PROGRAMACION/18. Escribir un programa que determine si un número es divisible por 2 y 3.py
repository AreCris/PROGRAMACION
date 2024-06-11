#18. Escribir un programa que determine si un número es divisible por 2 y 3.

numero = 30
d1 = numero%2
d2 = numero%3

if d1==0 and d2==0:
    print(numero,"es divisible entre 2 y 3")
else:
    print(numero,"no es divisible entre 2 y 3")