from abc import ABC, abstractmethod

class Estudiantes(ABC):
    def __init__(self, nombre, edad, grado, escuela, promedio):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.escuela = escuela
        self.promedio = promedio

    @abstractmethod
    def notas(self):
        pass
  
    def mostrar(self):
        print(self.nombre)
# Crear una clase que herede la clase abstracta con un método de presentar datos.
class Estudiante(Estudiantes):
    def notas(self):
        return self.promedio

    def presentar_datos(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}, Escuela: {self.escuela}, Promedio: {self.promedio}'

#estudiante = Estudiantes('Ana', 20, 'Segundo', 'Escuela XYZ', 85)
estudiante = Estudiante('Juan', 20, 'Segundo', 'Escuela XYZ', 85)
print(estudiante.notas())
print(estudiante.presentar_datos())