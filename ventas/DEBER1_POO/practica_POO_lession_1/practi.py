# practica hacer 
#agregacion entre dos clases 
class universidad:
    def __init__(self, nom, ubicacion):
        self.nombre = nom
        self.direccion = ubicacion
    def ofrecerCurso(self):
        pass
class profesor:
    def __init__(self,nombre, especialidad, universidad):
        self. nombreprof= nombre
        self.especialidad = especialidad
        self.uni = universidad
    def darclase(self):
        #imprimir la universidad a la que perteneces junto a sus datos 
        print("bienvenido usted pertenece actualmente a:")
        print(self.uni.nombre)
        print("se encuentra en esta direccion ")
        print(self.uni.direccion)
        print(f"nombre profesor: {self.nombreprof}")
        print(f"ESPECIALIDAD: {self.especialidad}")

uni = universidad("unemi", "fracisco de asis")

#instancia la clase que voy agregar
profe = profesor("alberto", "ing", uni)
profe.darclase()



# Definimos la clase Universidad
class Universidad:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
    def ofrecerCurso(self):
        pass

# Definimos la clase Profesor que tiene una relación de agregación con Universidad
class Profesor:
    def __init__(self, nombre, especialidad, universidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.universidad = universidad  # Aquí es donde se establece la relación de agregación
    def darClase(self):
        pass

# Definimos la clase Curso que tiene una relación de agregación con Profesor
class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor  # Aquí es donde se establece la relación de agregación
    def iniciarCurso(self):
        print(f"El curso {self.nombre} está siendo impartido por el profesor {self.profesor.nombre} de la universidad {self.profesor.universidad.nombre}")

# Creamos una instancia de Universidad
uni = Universidad("unemi", "fracisco de asis")

# Creamos una instancia de Profesor y le pasamos la instancia de Universidad
profe = Profesor("alberto", "ing", uni)

# Creamos una instancia de Curso y le pasamos la instancia de Profesor
curso = Curso("Matemáticas", profe)
curso.iniciarCurso()

    