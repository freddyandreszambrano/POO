class Empresa:
    def __init__(self,razon="Melissa",ruc="0943213456001",est=True):
        self.__id=1
        self.razon_social=razon
        self.ruc=ruc
        self.estado=est
        
    def mostrar(self):
        print(f"Empresa: {self.razon_social}")
        
if __name__ == '__main__':
    print("estoy en el archivo empresa.py")
    emp = Empresa("Supermaxi")
    print("__________________________")
    emp.mostrar()
