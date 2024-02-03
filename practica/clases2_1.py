# PRACTICA DE POO FECHA 28/09/2023

class gato: 
    #variable 
    life = 300 
    damage = 150 
    #constructor 
    def __init__ (self, name, age, velocity):
        self.name = name
        self.age = age
        self.velocity = velocity


    #metodos 
    def takidamage(self, daglerecive):
        self.life -=daglerecive



#main
#puntero del objeto que apunta a la clase gato 
gatoobjeto  = gato("espiga", 3, 50)
print("nombre= "+gatoobjeto.name)
print("edad= "+str(gatoobjeto.age))
print("valocidad= "+str(gatoobjeto.velocity))
    
#vamos hacer danio al gato 
gatoobjeto.takidamage(10)
print(f"vida actual = {gatoobjeto.life}")

#modificar una propiedad directamente 

gatoobjeto.age = 11
gatoobjeto.life = 20
print(f"edad = {str(gatoobjeto.age)}, vida = {str(gatoobjeto.life)}")

