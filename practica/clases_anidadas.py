# puedes crear un ejemplo de clases anidadas y probarlas
class Exterior:
    def __init__(self):
        self.nombre = "Clase Exterior"

    class Interior:
        def __init__(self):
            self.nombre = "Interior"

# Crear una instancia de la clase exterior
exterior = Exterior()
print(exterior.nombre)
# # Crear una instancia de la clase interior
interior = exterior.Interior()
print(interior.nombre)