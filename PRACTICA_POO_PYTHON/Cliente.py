class Cliente:
    def __init__(self,ced,nom,ape,estado=True):
        self.cedula = ced
        self.nomnbre = nom
        self.apellidos = ape
        self.estado = estado
        
    def mostrarCliente(self):
        pass



class ClienteNormal(Cliente):
    def __init__(self,ced,nom,ape,estado=True, promocion=False):
        super().__init__(ced,nom,ape,estado)
        # Atributo privado
        self.__promocion = 0.10 if promocion else 0
        
    @property #metodo getter: obtner el valor del atributo privado
    def promocion(self):
        return self.__promocion

    def mostrar(self):
        print(f"Cliente normal: {self.nomnbre} - {self.apellidos} - {self.promocion}")


# Herencia de clases
class ClienteVIP(Cliente):
    def __init__(self,ced,nom,ape,estado,tarjeta):
        super().__init__()

    
    def mostrar(self):
        print(f"")


