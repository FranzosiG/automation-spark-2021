"""
1. Crear un nuevo repositorio
2. Tomar de base el programa de la clase pasada
3. Vamos a modificar el programa para que solo tome como válidos números entre 1 y 120
 (si pone un número entre -inf y 0 o 121 a inf debe volver a preguntar)
3. Al inicio del programa preguntar cuantas personas registrar
4. Hacer que el programa que se hizo se ejecute esas n veces que se pusieron en el punto 3
5. Subir el programa al repositorio creado.
"""

peopleToRegister = int(input('Ingrese número de personas a registrar: '))
for i in range(peopleToRegister):
    age = 0
    while age <= 0 or age >= 120:  
        age = int(input('Digame su edad: '))

    if age<0:
        print('Usted no nació')
    elif age <18:
        print('Usted es menor de edad')
    elif age <65:
        print('Usted es mayor de edad')
    elif age <120:
        print('Usted es jubilado')
else:
    print('Proceso de carga finalizado')
