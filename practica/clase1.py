class Persona:
    estado=True # atributos de clase o static   
    def __init__(self,nombre,ced,edad):
        # atributos de instancia
        self.nombre=nombre
        self.cedula=ced
        self.edad=edad
    
    def __repr__(self):
        return f"Persona({self.nombre},{self.cedula})"
    
    def __str__(self):
        return f"{self.nombre} {self.edad}"
    
    def mostrar(self):
        print(f"nombre:{self.nombre} - cedula:{self.cedula} - edad:{self.edad} -Estado:{self.estado}")
# se crea un objeto(variable) de la instancia de la clase Persona
persona1= Persona("Daniel","0914192183",54) # llama automaticamente al constructor
persona2= Persona("Jose","0914192183",54) # llama automaticamente al constructor
print(persona1)
#print(repr(persona1))
print(persona2)
estudiantes=[]
estudiantes.append(persona1)
estudiantes.append(persona2)
estudiantes.append(Persona("Ana","0914192183",54))
for est in estudiantes:
    print(est)
    
print(estudiantes)
# print(persona1.nombre)
# persona1.nombre="Ana"
# persona1.cedula="0913"
# persona1.edad="30"
#persona1.mostrar()
#print(Persona.estado)
    
    