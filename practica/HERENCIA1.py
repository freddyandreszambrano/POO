
#HERENCIA 
#clase que hereda propiedades de la clase padre 

#clase animas - padre -

class animal:

    #variables
    comida = 50 
    #constructor 
    def __init__(self, name, age, velocity, acuatic):
        self.name = name
        self.age = age
        self.velocity = velocity
        self.acuatic = acuatic

    def __ishungry(self):
        return self.food<50
    def padahambre(self, food ):
        self.food -= food
    def eat(self):
        if self.__ishungry():
            self.fodd+=10
    def defend(self):
        print(f"{self.name} me estoy defencdiendo de mi enemigo")

#hijos 
#caso mas simple hereda todas las caracteristicas sin importar nada 
class amorfo(animal):
    pass
#mamifero 
class mamifer(animal):
    def __init__(self, name, age,velocity, acuatic, milf):
        super().__init__(name, age,velocity, acuatic)
        self.milf = milf
    
    #metodos
    def amamatar(self):
        print("amamantando")

#main 
amorfo = amorfo("caracol", 1, 5, True)
amorfo.defend()

mami =mamifer("oso", 356, 45, True, 80)
print(mami.milf)
mami.amamatar()
