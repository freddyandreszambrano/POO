from empresa import Empresa
from cliente import ClienteNormal,ClienteVip
from datetime import datetime,date
class Articulo:
    _secuencia=0
    def __init__(self,des,pre,sto):
        Articulo._secuencia += 1
        self.__id = Articulo._secuencia
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
        print(self.id,self.descripcion)

class DetalleVenta:
    _linea=0
    def __init__(self,articulo,cantidad):
        DetalleVenta._linea += 1
        self.id = DetalleVenta._linea
        self.articulo = articulo
        self.precio = articulo.precio
        self.cantidad = cantidad
        
class Venta:
    _factura=0
    _iva=0.12
    def __init__(self,cliente):
        Venta._factura = Venta._factura + 1
        self.factura = "F"+str(Venta._factura)
        self.fecha = date.today()
        self.cliente = cliente
        self.subtotal = 0
        self.iva = 0 
        self.total = 0
        self.detalleVenta = []
     
    def agregarDetalle(self,articulo,cantidad):
        # composicion entre detventa y vwnta
        detalle = DetalleVenta(articulo,cantidad)
        self.subtotal += round(detalle.precio*detalle.cantidad,2)
        self.iva = round(self.subtotal*Venta._iva,2)
        self.total = round(self.subtotal+self.iva,2)
        self.detalleVenta.append(detalle)   
    
    def mostrarVenta(self,empNombre,empRuc):
        print("Empresa: {:17} Ruc:{}".format(empNombre,empRuc))    
        print("Factura#:{:13}Fecha:  {}".format(self.factura,self.fecha))
        self.cliente.mostrar()
        print("Linea Articulo     Precio Cantidad Subtotal")
        for det in self.detalleVenta:
            print("{:5} {:15} {} {:6} {:7}".format(det.id,det.articulo.descripcion,det.precio,det.cantidad,det.precio*det.cantidad))  
        print("*"*23,"Subtotal=> ",self.subtotal)
        print("*"*26,"Iva=> ",self.iva)
        print("*"*23,"Total=> ",self.total)  
              
# print("_secuencia: ",Articulo._secuencia)
emp = Empresa("Supermaxi")
cli_normal= ClienteNormal("0914","Daniel","Vera",True,True)
cli_vip= ClienteVip("0913","Yady","Bohorquez",True,True)
art1 = Articulo("Aceite",3,100)
art2 = Articulo("Coca Cola",1,200)


venta = Venta(cli_normal) # agregacion cliente con venta
venta.agregarDetalle(art1,3) # agregacion articulo con detventa
venta.agregarDetalle(art2,2) # agregacion articulo con detventa
venta.mostrarVenta(emp.razon_social,emp.ruc) # asociacion

# print(art1.precio)
# art1.mostrar()
# art2.mostrar()
# print("_secuencia: ",Articulo._secuencia)
# cli_normal= ClienteNormal("0914","Daniel","Vera",True,True)
# cli_vip= ClienteVip("0913","Yady","Bohorquez",True,True)
# cli_normal.mostrar()
# cli_vip.mostrar()


