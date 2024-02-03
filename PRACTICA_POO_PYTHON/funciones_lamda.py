doble = lambda x: x * 2
print(doble(50)) 

#8so de filter 
lista = [1,3,4,5,23,4,534,23,12]
lista_pares = list(filter(lambda x: (x % 2 == 0),lista))
print(lista_pares)

#uso de map
lista2 = [1,2,3,4,5,6,7,8,9,10]
lista_doble = list(map(lambda x : x * 2, lista2))
print(lista_doble)

# args y kwargs
def empleado(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}  -  {value}")
    

empleado(nombre = "carlos", puesto = "programador", lenguaje = ("java"))

def notas(*args):
    for nota in args:
        print(nota)
notas(34,1,2,4,5,2,1,)