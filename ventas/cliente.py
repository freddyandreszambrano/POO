class Cliente:
    def __init__(self,ced,nom,ape,estado=True):
         self.cedula = ced
         self.nombres = nom
         self.apellidos = ape
         self.estado = estado
               
    def mostrar(self):
        pass

class ClienteNormal(Cliente):
    def __init__(self,ced,nom,ape,estado,promocion=False):
        super().__init__(ced,nom,ape,estado)
        self.__promocion= 10 if promocion else 0
         
        
    @property
    def promocion(self):  # getter: obtener el valor del atributo privado
        return self.__promocion
           
    def mostrar(self):
       print(f'Cliente Normal: {self.nombres} - {self.apellidos} - Promocion: {self.promocion}')     

class ClienteVip(Cliente):
    def __init__(self,ced,nom,ape,estado,tarjeta,activa=True):
        super().__init__(ced,nom,ape,estado)
        self.__tarjeta=tarjeta
        self.activa=activa
        
    @property
    def tarjeta(self):  # getter: obtener el valor del atributo privado
        return self.__tarjeta
    
    def mostrar(self):
        descuento = 20 if self.activa else 10
        print(f'Cliente Vip: {self.nombres} - {self.apellidos} - Tarjeta: {self.tarjeta} - Descuento: {descuento}')     


if __name__ == "__main__":
    cli_normal= ClienteNormal("0914","Daniel","Vera",True,True)
    cli_normal.mostrar()