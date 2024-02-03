class Carrera():
    #atrinuto estatico
    _secuencia = 0
    def __init__(self,nombre):
        self.__IdCr = 0
        self.nombreCarrera = nombre
    def mostrar(self):
        print(f"Carrera : {self.nombreCarrera}")

class Facultad():
    def __init__(self, nombre):
        self.__Idfacu = 0
        self.nombreFacu = nombre
        self.carreras = []

    def mostrar(self):
        print("estamos en la clase FACULTAD")
        print(f"nombre de la facultad : {self.nombreFacu}")

    def AgregarCarrera(self, nomCarrera):
        #aqui aplicacmos COMPOSICION de la clase 
        # CARRERA Y FACULTAD
        career = Carrera(nomCarrera)
        self.carreras.append(career.nombreCarrera)


if __name__ == '__main__':
    facultad = Facultad('Facultad de Ciencias')
    facultad.AgregarCarrera('Matematicas')
    facultad.AgregarCarrera('Fisica')

    facultad.mostrar()
    #aqui escojo mi lista carreras
    for carrera in facultad.carreras:
        carrera.mostrar()

