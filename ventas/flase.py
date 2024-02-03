class Nota:
    def __init__(self, valor):
        self.valor = valor

class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

class Facultad:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = Carrera(carrera)

    def agregar_carrera(self, carrera):
        self.carrera = Carrera(carrera)

# Crear una instancia de Facultad con una Carrera
facultad = Facultad("Facultad de Ciencias", "Ciencias de la Computación")

# Agregar una Nota a la Carrera de la Facultad
nota = Nota(95)
facultad.carrera.agregar_nota(nota)
