class empresa:
    def __init__(self, razon,ruc,est):
        self.__id = 1
        self.razon_social= razon
        self.ruc = ruc
        self.estado = est
    
    def mostar(self):
        print(f"Empresa : {self.razon_social}")


if __name__ == '__main__':
    #instancias clase 
    emp =empresa("comisariato", "23293321", True)
    emp.mostar()