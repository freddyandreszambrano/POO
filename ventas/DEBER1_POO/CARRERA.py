class Carrera:
    def __init__(self, NomUni, Facul, Carre, PeriodoLect):
        self.NombreUniversidad = NomUni
        self.Facultad = Facul
        self.Carrera = Carre
        self.PeriodoLectivo = PeriodoLect

    def mostrar(self):
        print(f"NombreUniversidad: {self.NombreUniversidad}, Facultad: {self.Facultad}, Carrera: {self.Carrera}, PeriodoLectivo: {self.PeriodoLectivo}")
        # for curso in self.cursos:
        #     curso.Mostrar()


