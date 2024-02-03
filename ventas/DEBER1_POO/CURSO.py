from CARRERA import Carrera
from ESTUDIANTE import Estudiante
class Asignatura:
    def __init__(self, Materias):
        self.Materiales = Materias

class Notas:
    def __init__(self):
        self.N1 = 0
        self.N2 = 0
        self.N3 = 0
        self.N4 = 0
        self.Exm1 = 0
        self.Exm2 = 0

    def AgregarNotas(self, N1, N2, N3, N4, Exm1, Exm2):
        # Asignar notas
        self.N1 = N1
        self.N2 = N2
        self.N3 = N3
        self.N4 = N4
        self.Examen1 = Exm1
        self.Examen2 = Exm2

    def CalcularPromedio(self):
        promedio = (self.N1 + self.N2 + self.N3 + self.N4 + self.Examen1 + self.Examen2) / 6
        return promedio

    def Mostrar(self):
        # Código para mostrar las notas
        pass

class ActaCalificacion:
    def __init__(self, IdCalificacion, Fecha, DetalleCalificacion):
        self.IdCalificacion = IdCalificacion
        self.Fecha = Fecha
        self.DetalleCalificacion = DetalleCalificacion



class Profesor:
    def __init__(self, idProfesor, Nombres, Apellidos, Estado):
        self.idProfesor = idProfesor
        self.Nombres = Nombres
        self.Apellidos = Apellidos
        self.Estado = Estado

    def AsignarNotas(self, estudiante, N1, N2, N3, N4, Examen1, Examen2):
        # Asignar notas al estudiante
        estudiante.AsignarNotas(N1, N2, N3, N4, Examen1, Examen2)

    def MostrarNotas(self):
        # Código para mostrar las notas
        pass



class Curso:
    def __init__(self, idCurso, nivel, seccion, asignatura):
        self.idCurso = idCurso
        self.nivel = nivel
        self.seccion = seccion
        self.asignatura = asignatura
        self.acta_calificacion = None  # Inicialmente no hay acta de calificación asignada (relación de asociación)
        self.estudiantes = []  # Inicialmente no hay estudiantes asignados (relación de agregación)

    def AgregarNotas(self, materia):
        #instanciar la clase ASIGNATURA
        asignatura = Asignatura(materia)

    def asignarActaCalificacion(self, acta_calificacion):
        # Asignar un acta de calificación al curso (relación de asociación)
        self.acta_calificacion = acta_calificacion

    def agregarEstudiante(self, estudiante):
        # Agregar un estudiante al curso (relación de agregación)
        self.estudiantes.append(estudiante)


# Creación de instancias

# asignatura1 = Asignatura("Material de estudio", "Profesor1", ["Estudiante1", "Estudiante2"])
# curso1 = Curso(1, "A", "Sección 1", "Nivel 1", asignatura1)

# carrera = Carrera("Universidad XYZ", "Facultad de Ciencias", "Ingeniería Informática", "2023")
# carrera.cursos.append(curso1)

# # Mostrar información de la carrera y sus cursos
# carrera.mostrar()

#aplcamos asocioacion 
#instanciasmos la clase carrera
Carr= Carrera("Unemi","FACI","Software","Abril - Agosto")