# class CPU:
#     def __init__(self, modelo, velocidad):
#         self.modelo = modelo
#         self.velocidad = velocidad

#     def procesar(self):
#         print(f"Procesando información a {self.velocidad} con el modelo {self.modelo}.")

# class Computadora:
#     def __init__(self, marca, modelo, cpu_modelo, cpu_velocidad):
#         self.marca = marca
#         self.modelo = modelo
#         self.cpu = CPU(cpu_modelo, cpu_velocidad)  # Aquí es donde se establece la relación de composición

#     def encender(self):
#         print(f"Encendiendo la computadora {self.marca} {self.modelo}.")
#         self.cpu.procesar()

# # Creamos una instancia de Computadora con una CPU
# comp = Computadora("MarcaX", "ModeloY", "ModeloCPUZ", "3.0 GHz")
# comp.encender()


#2 ejemplo 
class coche:
    def __init__(self, marca, modelo,tipo, potencia):
        self.marca = marca
        self.modelo = modelo
        self.mtr = motor(tipo, potencia)

    def encender(self):
        print("en la clase coche acaba de ejecutar el metodo encender")
        self.mtr.arrancar()

class motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    
    def arrancar(self):
        print("estamos arrancando el motor")
        print(f"de tipo {self.tipo} y de potencia {self.potencia}")


coche1 = coche("ferrari", "cawuasaki", "hc55", "wkk")
coche1.encender()



