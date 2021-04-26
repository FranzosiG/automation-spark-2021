"""
1-Se pregunte por el nombre de la persona
2-Se pregunte por el apellido de la persona
3-Se pregunte por la edad de la persona.
El formato de salida debe ser:
"Su nombre es: " + nombre + apellido + "y usted es " {condición de edad}
La condición de edad es:
1. Si es menor de 18 escribir menor
2. Si tiene entre 18 y 65 escribir mayor
3. Si tiene entre 65 y 120 escribir jubilado
4. Si tiene más escribir cadaver
"""

name = input("Ingrese su Nombre: ")
lastname = input ("Ingrese su Apellido: ")
age = input ("Ingrese su Edad: ") # age = int(input(age)) se puede ahorrar ese paso
age = int(age)

if age < 18:
    condition = 'menor'
elif age < 65:
    condition = 'mayor'
elif age <= 120:
    condition = 'jubilado'
else:
    condition = 'cadaver'


print ("Su Nombre es: " + name +" "+ lastname +" y su usted es " + condition)
