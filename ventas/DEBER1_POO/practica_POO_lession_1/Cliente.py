#aplicar concepto de herencia \

#clase padre 

class Cliente:
    def __init__(self, ced, nom, apelli, est):
        self.cedula = ced
        self.nombre = nom
        self.apellido = apelli
        self.estado = est


    def mostrar(self):
        pass

    
class ClienteNormal(Cliente):
    def __init__(self,  ced, nom, apelli, est, promocion=False):
        super().__init__(ced, nom, apelli, est)
        #valores privado
        self.__promocion  = 10 if promocion else 0

    @property
    def promocion(self):
        return self.__promocion
        
    #polimorfismo 
    def mostrar(self):
        print("cliente normal:"+self.nombre)


class ClienteVip(Cliente):
    def __init__(self,  ced, nom, apelli, est, promocion=False):
        super().__init__(ced, nom, apelli, est)
        #valores privado
        self.__promocion  = 50 if promocion else 0

    @property
    def promocion(self):
        return self.__promocion
        
    #polimorfismo 
    def mostrar(self):
        print("cliente vip:"+ self.nombre)

cli = ClienteNormal("093023", "freddy", "zambrano","activo",True)
cli.mostrar()
