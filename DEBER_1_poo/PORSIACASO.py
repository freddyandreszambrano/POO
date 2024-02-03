from datetime import date

class Carrera:
    def __init__(self, NomUni, Facul, Carre, PeriodoLect):
        self.NombreUniversidad = NomUni
        self.Facultad = Facul
        self.Carrera = Carre
        self.PeriodoLectivo = PeriodoLect

class Curso:
    def __init__(self, idCurso, nivel, seccion, materia):
        self.idCurso = idCurso
        self.nivel = nivel
        self.seccion = seccion
        self.materia = materia

class Profesor:
    def __init__(self, IdProfesor, Nombres, Apellidos):
        self.IdProfesor = IdProfesor
        self.Nombres = Nombres
        self.Apellidos = Apellidos

class Estudiante:
    def __init__(self, IdEstudiante, Nombres, Apellidos):
        self.IdEstudiante = IdEstudiante
        self.Nombres = Nombres
        self.Apellidos = Apellidos

class Nota:
    def __init__(self, acta_calificacion):
        self.N1 = 0
        self.N2 = 0
        self.N3 = 0
        self.N4 = 0
        self.Exm1 = 0
        self.Exm2 = 0
        self.notafinal = 0
        self.Estado = ""
        self.acta = acta_calificacion  # Asociación

    def agregarNotas(self, n1, n2, n3, n4, ex1, ex2, profesor, estudiante):
        self.N1 = n1
        self.N2 = n2
        self.N3 = n3
        self.N4 = n4
        self.Exm1 = ex1
        self.Exm2 = ex2
        self.profe = profesor  # Asociación
        self.estudent = estudiante  # Asociación

    def calcularNotaFinal(self):
        self.nota_final = (self.N1 + self.N2 + self.N3 + self.N4 + self.Exm1 + self.Exm2) 
        if self.nota_final >= 70:
            self.Estado = 'Aprobado'
        else:
            self.Estado = 'Reprobado'

class ActaCalificacion:
    def __init__(self, IdCalificacion, carrera, curso):
        self.IdCalificacion = IdCalificacion
        self.FechaEmision = date.today()
        self.notas = []  # Lista de notas (composición)
        self.carrera = carrera  # Asociación
        self.curso = curso  # Asociación

    def agregarNota(self, nota):
        self.notas.append(nota)

    def detalleActa(self):
        for nota in self.notas:
            print()
            print(f"Estudiante: {nota.estudent}")
            print(f"N1: {nota.N1} | N2: {nota.N2} | Exm1: {nota.Exm1} | N3: {nota.N3} | N4: {nota.N4} | Exm2: {nota.Exm2} | NotaFinal: {nota.nota_final} | Estado: {nota.Estado}")

# Crear objetos de las clases
carrera1 = Carrera("Unemi", "FACI", "Software", "Abril - Agosto")
curso1 = Curso(1, "4 nivel", "matutina", "POO")
profesor1 = Profesor('123', 'Juan', 'Perez')
estudiante1 = Estudiante(1, "freddy andres", "zambrano Q")

# Crear objeto ActaCalificacion
acta1 = ActaCalificacion(1, carrera1, curso1)

# Composición: Agregar notas al ActaCalificacion
nota1 = Nota(acta1)
nota1.agregarNotas(10, 15, 12, 11, 20, 9, profesor1.Apellidos, estudiante1.Apellidos)
nota1.calcularNotaFinal()

# Mostrar acta de calificación
acta1.detalleActa()
