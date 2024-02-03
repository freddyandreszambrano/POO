class Carrera:
    def __init__(self, NomUni, Facul, Carre, PeriodoLect):
        self.NombreUniversidad = NomUni
        self.Facultad = Facul
        self.Carrera = Carre
        self.PeriodoLectivo = PeriodoLect

    def mostrar(self):
        print(f"NombreUniversidad: {self.NombreUniversidad}, Facultad: {self.Facultad}, Carrera: {self.Carrera}, PeriodoLectivo: {self.PeriodoLectivo}")

class Profesor:
    def __init__(self, IdProfesor, Nombres, Apellidos):
        self.IdProfesor = IdProfesor
        self.Nombres = Nombres
        self.Apellidos = Apellidos

    def mostrar(self):
        return f'IdProfesor: {self.IdProfesor}, Nombres: {self.Nombres}, Apellidos: {self.Apellidos}'

class Estudiante:
    def __init__(self, IdEstudiante, Nombres, Apellidos):
        self.IdEstudiante = IdEstudiante
        self.Nombres = Nombres
        self.Apellidos = Apellidos

    def mostrar(self):
        return f'IdEstudiante: {self.IdEstudiante}, Nombres: {self.Nombres}, Apellidos: {self.Apellidos}'

class Nota:
    def __init__(self, N1, N2, N3, N4, Exm1, Exm2):
        self.N1 = N1
        self.N2 = N2
        self.N3 = N3
        self.N4 = N4
        self.Exm1 = Exm1
        self.Exm2 = Exm2
        self.Estado = None

    def calcularNotaFinal(self):
        nota_final = (self.N1 + self.N2 + self.N3 + self.N4 + self.Exm1 + self.Exm2) / 6
        if nota_final >= 70:
            self.Estado = 'Aprobado'
        else:
            self.Estado = 'Reprobado'
        return nota_final

class Asignatura:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

class Curso:
    def __init__(self, idCurso, nivel, seccion, asignatura, profesor):
        self.idCurso = idCurso
        self.nivel = nivel
        self.seccion = seccion
        self.asignatura = asignatura
        self.acta_calificacion = None  # Relación de agregación
        self.profesor = profesor
        self.estudiantes = []
        self.notas = []

    def asignar_carrera(self, carrera):
        self.carrera = carrera

class ActaCalificacion:
    def __init__(self, IdCalificacion, Fecha, ):
        self.IdCalificacion = IdCalificacion
        self.Fecha = Fecha

    def imprimirActa(self, curso, profesor, estudiantes, notas):
        print(f"Universidad: {curso.carrera.NombreUniversidad}")
        print(f"Facultad: {curso.carrera.Facultad}")
        print(f"Periodo Lectivo: {curso.carrera.PeriodoLectivo}")
        print(f"Profesor: {profesor.mostrar()}")
        print(f"Asignatura: {curso.asignatura.nombre}")  # Accedemos al nombre de la asignatura

        for estudiante, nota in zip(estudiantes, notas):
            print(f"Estudiante: {estudiante.mostrar()}")
            print(f"Notas: N1={nota.N1}, N2={nota.N2}, N3={nota.N3}, N4={nota.N4}, Exm1={nota.Exm1}, Exm2={nota.Exm2}")
            nota_final = nota.calcularNotaFinal()
            print(f"Nota Final: {nota_final}")
            print(f"Estado: {nota.Estado}")

# Crear una carrera
Carr = Carrera("Unemi", "FACI", "Software", "Abril - Agosto")
# Crear un profesor
profesor = Profesor('123', 'Juan', 'Perez')

# Crear una asignatura
asignatura = Asignatura("CS101", "Programación")

# Asignar la carrera al curso y asignar el profesor al curso
Curso1 = Curso(1, "1 nivel", "matutina", asignatura, profesor)
Curso1.asignar_carrera(Carr)

# Agregar estudiantes y sus notas
estudiante1 = Estudiante('001', 'Josue', 'Castillo')
nota1 = Nota(90, 85, 88, 92, 95, 90)
Curso1.estudiantes.append(estudiante1)
Curso1.notas.append(nota1)

estudiante2 = Estudiante('002', 'Mikel', 'Villacis')
nota2 = Nota(75, 80, 70, 85, 78, 82)
Curso1.estudiantes.append(estudiante2)
Curso1.notas.append(nota2)

# Crear un acta de calificación para el curso con su respectivo detalle
Acta1 = ActaCalificacion(1, "2023-10-05")

# Imprimir el acta de calificación
Acta1.imprimirActa(Curso1, profesor, Curso1.estudiantes, Curso1.notas)
