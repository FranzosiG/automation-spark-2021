print('hola mundo')

#puedo elegir el rango con una variable
#clientes = 3
#range (clientes)
#tambien puedo asignar un input para definir la cantidad de vueltas

# uso de BREAK

clientes = int(input('ingrese clientes: '))
for i in range (clientes):
    print (i)


for i in range (0,3):

    edad = input ('Digame su edad: ')
    #print(edad)
    edad = int(edad)
    #if edad >= 18:
    #    print('Usted es mayour de edad')
    #    if edad == 65:
    #        print ('tramites!')
    #else:
    #    print('Usted es menor de edad')


    if edad<0:
        print('Usted no nació')
    elif edad <18:
        print('Usted es menor de edad')
    elif edad <65:
        print('Usted es mayor de edad')
    elif edad <120:
        print('Usted es jubilado')
    else:
        print('Usted está en el otro mundo')
        