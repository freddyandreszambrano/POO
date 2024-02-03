from abc import ABC, abstractmethod

class persona(ABC):
    _secuencia = 0 
    def __init__(self, nombre, apellido):
        persona._secuencia += 1
        self.__id = persona._secuencia
        self.nombre = nombre
        self.apellido = apellido
    
    @property
    def id(self):
        # Función ternaria
        return -1 if self.__id == 0 else self.__id
    
    @abstractmethod
    def mostrar(self):
        pass

class Alumno(persona):

    # No ejecuto constructor porque mi clase Alumno no tiene atributos nuevos
    def mostrar(self):
        print(f"ID del ALUMNO: {self.id}")
        print(f"El nombre del ALUMNO es: {self.nombre}")
        print(f"Y su apellido es: {self.apellido}")
        print()
    
class Profesor(persona):
    # No ejecuto constructor porque mi clase Profesor no tiene atributos nuevos
    def mostrar(self):
        print(f"ID del PROFESOR: {self.id}")
        print(f"El nombre del PROFESOR es: {self.nombre}")
        print(f"Y su apellido es: {self.apellido}")
        print()
    
if __name__ == "__main__":
    alumno = Alumno('Juan', 'acosta')
    print("Información del alumno:")
    alumno.mostrar()

    profesor = Profesor('Mar', 'Loor')
    print("Información del profesor:")
    profesor.mostrar()
