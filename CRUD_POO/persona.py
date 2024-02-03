from abc import ABC, abstractmethod
class Persona(ABC):
    #atrinuto estatico
    _secuencia = 0
    def __init__(self, nom, apellido):
        Persona._secuencia += 1
        self.__Id = Persona._secuencia
        self.nombre = nom
        self.apellido = apellido

    @property
    def id(self):
        #funcioin ternaria
        return -1 if self.__Id == 0 else self.__Id
    @abstractmethod
    def mostrar(self):
        pass

class Alumno(Persona):
    # no ejecuto constructor por que mi clase alumno no tiene atributos nuevos
    def mostrar(self):
        print(f"ID del  ALUMNO: {self.id}")
        print(f"el nombre del ALUMNO es : {self.nombre}")
        print(f"y su apellido es  : {self.apellido}")
        print()
    
    
class Profesor(Persona):
    # no ejecuto constructor por que mi clase alumno no tiene atributos nuevos
    def mostrar(self):
        print(f"ID del PROFESOR: {self.id}")
        print(f"el nombre del PROFESOR es : {self.nombre}")
        print(f"y su apellido es  : {self.apellido}")
        print()
    
        

if __name__ == "__main__":
    alumno = Alumno('Juan', 'acosta')
    print("Informacion del alumno:")
    alumno.mostrar()

    profesor = Profesor('Mar', 'Loor')
    print("Informacion del profesor:")
    profesor.mostrar()

    
    