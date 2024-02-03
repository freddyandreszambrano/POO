# Creando dos clases que servirán como mixins 
class Clase1:
    def test1(self):
        return "Test 1"

class Clase2:
    def test2(self):
        return "Test 2"

# Creando una clase que hereda de los dos mixins
class MiClase(Clase1, Clase2):
     def test3(self):
        return "Test 3"

# Creando una instancia de MiClase y llamando a los métodos de los mixins
mi_objeto = MiClase()
print(mi_objeto.test1())
print(mi_objeto.test2())
print(mi_objeto.test3())
