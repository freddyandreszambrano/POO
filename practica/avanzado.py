# Crear una lista de 10 números
#          0  1  2 
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros[0]=2
numeros.append(20)
#numeros[len(numeros)]=30
# Presentar solo los números pares utilizando un bucle for
# print("Recorrido con bucle for basico:")
# for numero in numeros:
#     if numero % 2 == 0:
#         print(numero)

# print("Recorrido con bucle for con enumerate:")
# for indice,numero in enumerate(numeros):
#     if numero % 2 == 0:
#         print(indice,numero," Es par")
        
# # Ejemplo de recorrido de un diccionario mostrando clave y valor:

# diccionario = {"a": 1, "b": 2, "c": 3}
# for clave, valor in diccionario.items(): #values, keys()
#     print(f"Clave: {clave}, Valor: {valor}")

# Ejemplo:
lista = [1, 2, 3, 4, 5]  # Ejemplo de lista
tupla = (1, 2, 3, 4, 5)  # Ejemplo de tupla
conjunto = {1, 2, 3, 4, 5}  # Ejemplo de conjunto
# La principal diferencia entre las listas/tuplas y los conjuntos 
# es que los conjuntos no permiten elementos duplicados, mientras 
# que las listas y las tuplas sí. Esto significa que los conjuntos
# son útiles cuando se necesita almacenar una colección de elementos
# únicos y no se necesita un orden específico, mientras que las 
# listas y las tuplas son más adecuadas cuando se necesita mantener
# un orden específico y se permiten elementos duplicados.
# print(lista)
# print(tupla)
# print(conjunto)


# Ejemplo 4: Verificar si un número es par utilizando una lista
def es_par_lista(numero):
    lista = [2, 4, 6, 8, 10]
    if numero in lista:
        return True
    else:
        return False

# Ejemplo 5: Verificar si un número es par utilizando una tupla
def es_par_tupla(numero):
    tupla = (2, 4, 6, 8, 10)
    if numero in tupla:
        return True
    else:
        return False

# Ejemplo 6: Verificar si un número es par utilizando un conjunto
def es_par_conjunto(numero):
    conjunto = {2, 4, 6, 8, 10}
    if numero in conjunto:
        return True
    else:
        return False

numero = 6
# print(f"¿El número {numero} es par?")
# print(f"Usando una lista: {es_par_lista(numero)}")
# print(f"Usando una tupla: {es_par_tupla(5)}")
# print(f"Usando un conjunto: {es_par_conjunto(numero)}")

# Tipos de funciones en Python:
# 1. Funciones anónimas (lambda)
# 2. Funciones dentro de otras funciones
# 3. Funciones como parámetros

# Ejemplo de función anónima (lambda):
def sumar(x,y): 
    return x+y

# Lambda es una función anónima en Python que se define sin un nombre.
# Se utiliza cuando se necesita una función rápida y simple sin definir
# una función completa.
# Un ejemplo de uso de lambda en Python es para ordenar una lista 
# de acuerdo a un criterio específico.

# suma = lambda x, y: x + y
# print(suma(2,5))
# es_par = lambda x: x % 2 == 0
# if es_par(5):
#     print("Par")
# else:    
#     print("Impar")
    
#suma(2, 3)
#sm = (x,y) => x+y  javascript
#sm=(2,5)
#Ejemplo de función dentro de otra función:
def funcion_padre():
    def funcion_hija():
        print("Soy una función dentro de otra función")
    funcion_hija()

# Ejemplo de función como parámetro:
def funcion_principal(funcion):
    print("Ejecutando función principal")
    
    print(funcion(4,5))

# Ejecutar ejemplos:

# funcion_padre()
#funcion_principal(lambda: print("Soy una función como parámetro"))
# funcion_principal(suma)

# Comprehension en Python es una forma concisa de crear listas, 
# conjuntos y diccionarios utilizando una sintaxis compacta.
# Se recomienda su uso cuando se necesita crear una nueva estructura de datos a partir de una existente, aplicando una transformación o filtrando elementos.
# Aquí hay tres ejemplos de comprehension en Python:

# Ejemplo 1: Crear una lista de los cuadrados de los números del 1 al 10
#cuadrados = [x**2 for x in range(1,11) if x % 2 ==0 ] # (1,2,3,4,5,6,7,8,9,10)
# cua=[]
# for x in range(1,11):
#    if x % 2 ==0:
#      cua.append(x)
    
# # Ejemplo 2: Crear un conjunto de los números pares del 1 al 10
# impares = tuple(x for x in range(1, 11) if x % 2 != 0)

# # Ejemplo 3: Crear un conjunto de los números pares del 1 al 10
# pares = {x for x in range(1, 11) if x % 2 == 0}

# # Ejemplo 3: Crear un diccionario con los números del 1 al 5 como claves y sus cuadrados como valores
# diccionario = {x: x**2 for x in range(1, 6)}
# dic = {}
# for c,v in enumerate([1,2,3,4,5]):
#     dic[str(c)]=v**2
    
    
# Recomendaría el uso de comprehension cuando se necesite crear una nueva estructura de datos de manera concisa y legible.

#print(cuadrados,impares,pares,diccionario)
# funciones de orden superior
# El concepto de map en Python es una función incorporada que se utiliza para aplicar una función a cada elemento de una lista (u otro iterable) y devolver un nuevo iterable con los resultados.
# Se utiliza para realizar operaciones en paralelo en todos los elementos de una lista sin necesidad de utilizar bucles explícitos.
# Un ejemplo de uso de map en Python es para aplicar una función lambda a cada elemento de una lista.


# lista = [1, 2, 3, 4, 5]
# suma = lambda x: x + 2
# resultado = list(map(suma, lista))
# print(resultado)

# El concepto de filter en Python es una función incorporada que se utiliza para filtrar elementos de una lista (u otro iterable) según una condición.
# Se utiliza para seleccionar los elementos que cumplen con la condición especificada y devolver un nuevo iterable con esos elementos.
# Un ejemplo de uso de filter en Python es para filtrar los números pares de una lista.

# lista = [1, 2, 3, 4, 5]
# resultado = list(filter(lambda x: x % 2 == 0, lista))
# print(resultado)

# argumentos           (1,2,3,8)  {"num1":4,"num2:5"}
def suma_con_args_kwargs(*args, **kwargs):
    suma = 0
    print(args)
    print(kwargs)
    #x,y=kwargs
    for arg in args:
        suma += arg
    for key, value in kwargs.items():
        suma += value
    return suma

resultado = suma_con_args_kwargs(1, 2, 3,8, num1=4, num2=5)
print(resultado)

def manejar_division_por_cero(func):
    # Esta es la función wrapper que envuelve la función original
    def nueva_funcionalidad(*args, **kwargs):
        try:
            # Intentamos ejecutar la función original
            print("args: ",args)
            print("args: ",kwargs)
            return func(*args, **kwargs)
        except ZeroDivisionError:
            # Si hay una división por cero, devolvemos un mensaje de error
            return "Error: División por cero"
    # Devolvemos la función wrapper
    return nueva_funcionalidad

@manejar_division_por_cero
def dividir(a, b):
    return a / b
print(dividir(2,0))


