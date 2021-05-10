#1. Crear un nuevo repositorio
#2. Tomar de base el la tarea de la clase 2
#3. Si es menor de edad, vamos a venderle juguetes
#3.1: preguntarle si es electrónico, color, camina
#4. Si es mayor de edad, vamos a venderle ropa
#4.1: preguntarle si es camisa o pantalon, color y el talle
#5. Si es jubilado vamos a venderle pasajes
#5.1 Preguntarle si quiere viajar a Federación, Cataratas o Santa Teresita
#Mostrar por pantalla los datos de la persona y el producto seleccionado


def ventaMenores(edad):
    esElectronico = ''
    colorJuguete = ''
    jugueteCamina = ''
    mensajePedido = [str(edad) + ' años']
    while esElectronico != 'Y' and  esElectronico != 'N':  
        esElectronico = input('¿Compra juguete electrónico? Y/N :')
    
    while colorJuguete != 'rojo' and colorJuguete != 'verde' and colorJuguete != 'azul':  
        colorJuguete = input('¿De qué color? (rojo/verde/azul) :')

    while jugueteCamina != 'Y' and jugueteCamina != 'N':  
        jugueteCamina = input('¿El juguete camina? Y/N :')

    mensajePedido.append('Juguete color ' + colorJuguete)
    if esElectronico == 'Y':
        mensajePedido.append('Juguete electrónico')
    else:
        mensajePedido.append('Juguete NO electrónico')
    
    if jugueteCamina == 'Y':
        mensajePedido.append('camina')
    else:
        mensajePedido.append('no camina')
    

    return mensajePedido

def ventaMayores(edad):
    esCamisaPantalon = ''
    colorPrenda = ''
    tallePrenda = ''
    mensajePedido = [str(edad) + ' años']
    while esCamisaPantalon != 'C' and esCamisaPantalon != 'P':  
        esCamisaPantalon = input('¿Compra camisa o pantalón? C/P :')
    
    while colorPrenda != 'negro' and colorPrenda != 'azul' and colorPrenda != 'gris':  
        colorPrenda = input('¿De qué color? (negro/azul/gris) :')

    while tallePrenda != 'S' and tallePrenda != 'M' and tallePrenda != 'L' and tallePrenda != 'XL':  
        tallePrenda = input('¿Cuál es el talle? S/M/L/XL :')
    
    mensajePedido.append(colorPrenda)
    mensajePedido.append(tallePrenda)
    if esCamisaPantalon == 'C':
        mensajePedido.append('Camisa')
    else:
        mensajePedido.append('Pantalon')

    return mensajePedido

def ventaJubilados(edad):
    destino = ''
    mensajePedido = [str(edad) + ' años']
    while destino != 'C' and destino != 'F' and destino != 'S':  
        destino = input('Elija destino Cataratas (C), Federación(F), Santa Teresita(S) :')
    
    if destino == 'C':
        mensajePedido.append('Cataratas')
    elif destino == 'F':
        mensajePedido.append('Federación')
    else: 
        mensajePedido.append('Santa Teresita')

   
    return mensajePedido


    

personasParaRegistrar = int(input('Ingrese número de personas a registrar: '))
mensaje = ''
for i in range(personasParaRegistrar):
    edad = 0
    while edad <= 0 or edad >= 120:  
        edad = int(input('Digame su edad: '))
    if edad<0:
        print('Usted no nació')
    elif edad <18:
        print('Usted es menor de edad')
        mensaje = ventaMenores(edad)
    elif edad <65:
        print('Usted es mayor de edad')
        mensaje = ventaMayores(edad)
    elif edad <120:
        print('Usted es jubilado')
        mensaje = ventaJubilados(edad)
else:
    print(mensaje)
    print('Proceso de carga finalizado')


