from Empresa import Empresa
from Cliente import ClienteNormal, ClienteVIP 
from datetime import datetime, date

class articulo():
    #atributo estatico 
    #ESTANDAR  - siempre debe ser declarado incialmente con un "_"
    # premite acceder desde cualquier parte de la clase
    _secuencia = 0 
    def __init__(self, des, pre,sto):
        articulo._secuencia +=1
        self.__id = articulo._secuencia
        self.descripcion = des
        self.precio = pre
        self.stock = sto
    @property
    def id(self):
        if self.__id == 0:
            return -1
        else:
            return self.__id
    def mostrar(self):
        print(self.id, self.descripcion)

class DetalleVenta:
    #atrinuto estatico
    _linea = 0
    #contructor
    def __init__(self, articulo, cantidad):
        DetalleVenta._linea +=1
        self.id = DetalleVenta._linea
        self.articulo = articulo
        self.precio = articulo.precio
        self.cantidad = cantidad

class Venta:
    _factura = 0
    _iva = 12
    def __init__(self, cliente):
        Venta._factura = Venta._factura + 1
        self.factura = f"f {str(Venta._factura)}"
        self.fecha = date.today()
        self.cliente = cliente
        self.subtotal = 0 
        self.iva = 0
        self.total = 0
        self.detalleventa = []

    def agregarDetalle(self):
        #principio de agregacion 
        # || <> ||
        pass
        

#instanciar clases
#art1 = articulo("aceite",3,100)
#art2 = articulo("Coca Cola",5,400)
#art1.mostrar()
#art2.mostrar()


#cli_normal = ClienteNormal("0914","daniel", "ver", True, True)
#cli_Vip = ClienteVIP("0915","yady", "ver", True, True)
#print("estoy en facturacion")