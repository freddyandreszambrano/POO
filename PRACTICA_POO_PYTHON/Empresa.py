class Empresa:
    def __init__(self, razon="melissa", ruc="0943234523552", tel="0939129130", est=True):
        # atributos privados
        self.__id =id
        self.razon_social = razon
        self.ruc = ruc
        self.ratado = est
    def mostrar(self):
        print(f"Empresa: {self.razon_social}")

#print("estoy en empresa.py")
if __name__ =="__main__":
    emp= Empresa("SuperMaxi")
    print("__________________________")
    print("empresa")
    #print(emp.razon_social)
    emp.mostrar()
