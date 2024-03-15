# Estructuras Iterativas 

#PROBLEMA 1: Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
#en el rango de 1500 y 2700 (ambos incluidos).

#Paso1. Crear una lista vacía para almacenar los números encontrados
numeros_divisibles = []

#Paso2. Iterar a través del rango de 1500 a 2700 (ambos incluidos)
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        # Si es cierto, agregarlo a la lista
        numeros_divisibles.append(num)

# Imprimir los números encontrados
print("Los números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:")
print(numeros_divisibles)


#PROBLEMA 2: 
#Escriba un programa en Python para construir el siguiente patrón.
#*
#**
#***
#****
#*****
#****
#***
#**
#*

#Paso1. Para dar con la forma del triángulo definimos la altura = 5
h = 5
for i in range(h):
    print('*'*(i+1))
#---Similar el comando para imprimir la parte inferior del triángulo 
for i in range(h-1,0,-1):
    print('*'*i)


#PROBLEMA 3: Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El ingreso 
#de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos números. Con dichos números, 
#su programa debe evaluar cada uno de estos números e indicar la cantidad de números pares e impares.

#Paso1. Crear una lista vacía para almacenar los números
numeros = []  
pares = 0
impares = 0

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()
    if respuesta == "SI":
        n = int(input("Ingrese el número: "))
        #Paso2. Agregar el número a la lista
        numeros.append(n) 
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    elif respuesta == "NO":
        #Paso3. Cortar el bucle si la respuesta es "NO"
        break 
    else:
        print("Respuesta inválida. Por favor ingrese SI o NO.")

print("Números ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)


#PROBLEMA 4: Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
#pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus materias.
#Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado completo de los alumnos.
#Nota:El uso de listas con diccionarios le será de utilidad

def ingresar_alumnos():
    alumnos = []
    continuar_ingreso = True
    while continuar_ingreso:
        nombre = input("Ingrese el nombre del alumno ('fin' para terminar): ")
        if nombre.lower() == 'fin':
            continuar_ingreso = False
            break
        else:
            notas = []
            for i in range(3):
                nota = float(input(f"Ingrese la calificación {i+1} del alumno {nombre}: "))
                notas.append(nota)
            alumno = {'Alumno': nombre, 'Notas': notas}
            alumnos.append(alumno)
    return alumnos

def mostrar_alumnos(alumnos):
    print("Listado de alumnos:")
    for alumno in alumnos:
        print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

#Ingresar datos de los alumnos
alumnos = ingresar_alumnos()

#Mostrar listado de alumnos
mostrar_alumnos(alumnos)


# Funciones
#PROBLEMA 5: Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
#Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
# Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método count.

def contar_digitos(numero, digito):
    cantidad = str(numero).count(str(digito))
    return cantidad

def main():
    numero = int(input("Ingrese un número entero: "))
    digito = int(input("Ingrese un dígito: "))
    
    cantidad = contar_digitos(numero, digito)
    
    print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")

if __name__ == "__main__":
    main()


#PROBLEMA 6: Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
#Nota: La secuencia de Fibonacci es la serie de números: 0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
#Cada número siguiente se obtiene sumando los dos números anteriores.
    
def fibonacci(n):
    fib_series = [0, 1]
    while True:
        next_number = fib_series[-1] + fib_series[-2]
        if next_number > n:
            break
        fib_series.append(next_number)
    return fib_series

fibonacci_series = fibonacci(50)
print("Serie de Fibonacci hasta 50:", fibonacci_series)


#PROBLEMA 7: Escriba una función de Python que tome un número como parámetro y verifique que el número sea
#primo o no.

#Paso1. Solicitar un numero al usuario
numero = int(input('Ingrese numero: '))

#Paso2. Evaluar si numero es primo, si encuentro un divisor del numero en rango <1; n> entonces numero no va ser primo
es_primo = True
for i in range (2, numero):

    if numero%i==0:
        es_primo = False
        break

if es_primo:
    print('El número es primo')
else:
    print('El número no es primo')


#PROBLEMA 8: Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
#función acepta el número como argumento.

#Paso1. Solicitar un numero al usuario
numero = int(input("Ingrese un número entero no negativo: "))

def calcular_factorial(numero):
    if numero < 0:
        return False, None
    elif numero == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial
        
#Paso2. Calcular el factorial del número ingresado por el usuario
resultado = calcular_factorial(numero)
if resultado is not None:
    print("El factorial de", numero, "es:", resultado)


#PROBLEMA 9: Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
#por ejemplo, omitiendo las vocales. Implemente un programa que solicite al usuario una cadena de texto y luego retorne 
#ese mismo texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o minúsculas.

#Paso1. Solicitar al usuario que ingrese una cadena de texto
texto = input("Ingrese una cadena de texto: ")

def omitir_vocales(cadena):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    #Paso2. abrir una cadena vacía para almacenar el resultado
    resultado = ''

    # Iterar sobre cada caracter en la cadena
    for caracter in cadena:
        # Si el caracter no es una vocal, agregarlo al resultado
        if caracter not in vocales:
            resultado += caracter

    return resultado

#Paso3. Llamar a la función omitir_vocales y mostrar el resultado
texto_sin_vocales = omitir_vocales(texto)
print("Texto sin vocales:", texto_sin_vocales)


#PROBLEMA 10:  En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las fechas 
#en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en lugar del primero. Intente ordenar, 
#por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente en cualquier programa (por ejemplo, una hoja de cálculo). 
#Las fechas en ese formato también son ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como 
#el 9 de agosto de 1636!. Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
#8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en la lista abajo:
#["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
#Luego, genere esa misma fecha en formato AAAA-MM-DD
#Nota: Los métodos de listas y string le resultarán de gran utilidad.
#Nota que si empleamos print(f"{n:02}") , esta completará con 0 valos a la izquierda de un número

#Paso1. Pedir al usuario que ingrese una fecha
fecha = input("Ingrese una fecha (en formato mes-día-año o mes día, año): ")

def obtener_mes_numero(mes):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    try:
        return str(meses.index(mes) + 1).zfill(2)
    except ValueError:
        return None

def obtener_fecha_en_formato_iso(fecha):
    # Dividir la fecha en sus componentes: mes, día y año
    partes = fecha.split()
    if len(partes) == 3:
        mes_numero = obtener_mes_numero(partes[0])
        dia = partes[1].strip(',')
        año = partes[2]
        # Componer la fecha en formato AAAA-MM-DD
        if mes_numero is not None:
            return f"{año}-{mes_numero}-{dia.zfill(2)}"
    return None

# Obtener la fecha en formato ISO
fecha_iso = obtener_fecha_en_formato_iso(fecha)

# Mostrar la fecha en formato ISO si se pudo obtener
if fecha_iso is not None:
    print("La fecha en formato AAAA-MM-DD es:", fecha_iso)
else:
    print("La fecha ingresada no tiene el formato esperado.")