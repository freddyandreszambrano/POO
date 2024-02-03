class Estudiante:
    # Variable de clase(statica) de clase para contar el total de estudiantes
    _total_estudiantes = 0

    def __init__(self, cedula, nombres, direccion, carrera):
        # Atributos privados
        self.__cedula = cedula
        self.nombres = nombres
        self.direccion = direccion
        self.carrera = carrera
        # Incrementar el total de estudiantes cada vez que se crea un nuevo estudiante
        Estudiante._total_estudiantes += 1

    # Property para obtener la cedula
    @property
    def cedula(self):
        return self.__cedula

    # Setter para la cedula
    @cedula.setter
    def cedula(self, nueva_cedula):
        self.__cedula = nueva_cedula

  
    # Método estático para obtener el total de estudiantes
    @staticmethod
    def total_estudiantes():
        return Estudiante._total_estudiantes

    # Método para imprimir los detalles del estudiante, se sobrescribirá en la clase Notas
    def imprimir_detalles(self):
        return f"Cedula: {self.cedula}, Nombres: {self.nombres}, Direccion: {self.direccion}, Carrera: {self.carrera}"


class Notas(Estudiante):
    
    def __init__(self, id, asignatura, profesor, nota1, nota2, promedio, cedula, nombres, direccion, carrera):
        # Llamada al constructor de la clase padre
        super().__init__(cedula, nombres, direccion, carrera)
        # Atributos privados
        self.__id = id
        self.asignatura = asignatura
        self.profesor = profesor
        self.nota1 = nota1
        self.nota2 = nota2
        self.promedio = promedio

    # Property para obtener el id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    # Sobrescribir el método imprimir_detalles para incluir las notas
    def imprimir_detalles(self):
        return super().imprimir_detalles() + f", Asignatura: {self.asignatura}, Profesor: {self.profesor}, Nota1: {self.nota1}, Nota2: {self.nota2}, Promedio: {self.promedio}"

 # Crear un objeto de la clase Notas
est = Estudiante('1234567890', 'Juan Perez', 'Calle X', 'Ingenieria') 
nota1 = Notas(1, 'Matematicas', 'Profesor X', 90, 95, 92.5, '1234567890', 'Juan Perez', 'Calle X', 'Ingenieria')
nota2 = Notas(2, 'Matematicas', 'Profesor X', 90, 95, 92.5, '1234567890', 'Juan Perez', 'Calle X', 'Ingenieria')
 # Imprimir los detalles del estudiante y sus notas
#print(nota1.imprimir_detalles())
#print(Notas._total_estudiantes)
#print(nota2.imprimir_detalles())
print(Notas._total_estudiantes)
print(Estudiante.total_estudiantes())





