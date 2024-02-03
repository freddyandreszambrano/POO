class Semestre():
    def __init__(self, smtr ):
        self.__IdSmt= 0
        self.semestre = smtr

    def mostrar(self):
        print(f"semestre: {self.semestre}")

class Asignatura():
    def __init__(self, nombreAsg):
        self.__IdAsig = 0 
        self.asignatura = nombreAsg
    def mostrar(self):
         print(f"ASIGNATURA: {self.asignatura}")


class Notas():
    def __init__(self,asignatura,semestre,estudiante, profe,n1,n2,exm1,n3,n4,exm2):
        self.__IdNt= 0 
        # self.facultad = facul
        # self.carrera = carrera
        self.asignatura = asignatura
        self.alumno = estudiante
        self.profesor = profe
        self.semestre = semestre
        self.nota1 = n1
        self.nota2 = n2
        self.examen1 = exm1
        self.parcial1 = 0 #este valor se calcula 
        self.nota3 = n3
        self.nota4 = n4
        self.examen2 = exm2
        #estos valores se calculan 
        self.parcial2 = 0  
        self.notafinal = 0 
        self.estado = ""
    
    def calcularNota(self):
        self.parcial1 = round(self.nota1 + self.nota2 + self.examen1, 2)
        self.parcial2 = round(self.nota3 + self.nota4 + self.examen2, 2)
        self.notafinal  = self.parcial1 + self.parcial2
        
        #cambiamos el estado del alumno segun su nota final 
        # operador ternario
        self.estado = "APROBADO" if self.notafinal > 70 else "REPROBADO"
    
