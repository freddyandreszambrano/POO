class Estudiante:
    estado=True # atributos de clases
    def __init__(self,nom,notas):
        # atributos de instancia
        self.nombre=nom
        self.nota=notas
        
    def mostrar(self):
        print(f"nombre={self.nombre} nota:{self.nota}")
        
# melani = Estudiante("melani",50)
# steven = Estudiante("steven",40)
# melani.mostrar()    
# steven.mostrar()    
print(Estudiante.estado)