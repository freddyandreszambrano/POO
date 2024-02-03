from datetime import datetime,date
class Carrera:
    def __init__(self, NomUni, Facul, Carre, PeriodoLect):
        self.NombreUniversidad = NomUni
        self.Facultad = Facul
        self.Carrera = Carre
        self.PeriodoLectivo = PeriodoLect

    def mostrar(self):
        pass
        # print(f"NombreUniversidad: {self.NombreUniversidad}, Facultad: {self.Facultad}, Carrera: {self.Carrera}, PeriodoLectivo: {self.PeriodoLectivo}")

class Curso:
    def __init__(self, idCurso, nivel, seccion,materia):
        self.idCurso = idCurso
        self.nivel = nivel
        self.seccion = seccion
        self.materia = materia

    def MostroCurso(self):
        pass


class Profesor:

    def __init__(self, IdProfesor, Nombres, Apellidos):
        self.IdProfesor = IdProfesor
        self.Nombres = Nombres
        self.Apellidos = Apellidos

    def mostrar(self):
        pass
class Estudiante:
    def __init__(self, IdEstudiante, Nombres, Apellidos):
        self.IdEstudiante = IdEstudiante
        self.Nombres = Nombres
        self.Apellidos = Apellidos

    def mostrar(self):
        pass
        #return f'IdEstudiante: {self.IdEstudiante}, Nombres: {self.Nombres}, Apellidos: {self.Apellidos}'
class ActaCalificacion:
    def __init__(self, IdCalificacion):
        self.IdCalificacion = IdCalificacion
        self.FechaEmision = date.today()

    def imprimircabecera(self,uni, facu,carrera,periodoLec,curso, jornada, materia):
        print(f"Universidad: {uni}")
        print(f"Facultad: {facu}")
        print(f"Periodo Lectivo: {periodoLec}")
        print(f"Carrera: {carrera}")
        print(f"Nivel: {curso}")
        print(f"Jornada: {jornada}")
        print(f"Materia: {materia}")

    def detalleActa(self,nota1,nota2,nota3,nota4,examen1,examen2,notafinal,estudiante,estado):
        print()
        print(f"estudiante: {estudiante}")
        print(f"N1:{nota1} | N2:{nota2} | Exm1:{examen1} | N3:{nota3} | N4:{nota4} | Exm2:{examen2} | NotaFinal:{notafinal}")
        print(f"{estado}")
        


class Nota:
    def __init__(self,acta):
        self.N1 = 0
        self.N2 = 0
        self.N3 = 0
        self.N4 = 0
        self.Exm1 = 0
        self.Exm2 = 0
        self.notafinal = 0
        self.Estado = ""
        self.NewActa = acta

    def agregarNotas(self,n1,n2,n3,n4,ex1,ex2,profesor,estudiante):
        self.N1 = n1
        self.N2 = n2
        self.N3 = n3
        self.N4 = n4
        self.Exm1 = ex1
        self.Exm2 = ex2
        self.profe = profesor
        self.estudent = estudiante
        


    def calcularNotaFinal(self):
        self.nota_final = (self.N1 + self.N2 + self.N3 + self.N4 + self.Exm1 + self.Exm2) 
        #print(nota_final)
        if self.nota_final >= 70:
            self.Estado = 'Aprobado'
        else:
            self.Estado = 'Reprobado'
       
    def mostarNotas(self):
        self.NewActa.detalleActa(self.N1,self.N2,self.N3,self.N4,self.Exm1,self.Exm2,self.nota_final,self.estudent,self.Estado)




Carrera1 = Carrera("Unemi", "FACI", "Software", "Abril - Agosto")
curso1  = Curso(1,"4 nivel", "matutina", "POO")
actac1 = ActaCalificacion(1)
#aplicando ASOCIACION
actac1.imprimircabecera(Carrera1.NombreUniversidad,Carrera1.Facultad,Carrera1.Carrera,Carrera1.PeriodoLectivo,curso1.nivel,curso1.seccion,curso1.materia )


estudiante1 = Estudiante(1,"freddy andres","zambrano Q")
profesor1 = Profesor('123', 'Juan', 'Perez')

#APLICAMOS AGREGACION 
notas =Nota(actac1)
notas.agregarNotas(10,15,12,11,20,9,profesor1.Apellidos, estudiante1.Apellidos)
notas.calcularNotaFinal()
notas.mostarNotas()
