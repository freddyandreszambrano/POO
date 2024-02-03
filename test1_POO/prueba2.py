class Transaccion_bancaria:
    def __init__(self, cliente, tipo_transaccion, monto, tasa_interes, plazo_meses, aprobacion, garantia, descripcion):
        self.solicitante = cliente
        self.tipo_transaccion = tipo_transaccion
        self.monto = monto
        self.tasa_interes = tasa_interes
        self.plazo_meses = plazo_meses
        self.aprobacion = aprobacion
        self.garantia = garantia
        self.descripcion = descripcion

    def Prestamo(self):
        if self.aprobacion:
            prestamo = PrestamoPersonal(self.monto, self.tasa_interes, self.plazo_meses)
            return f"Prestamo, cuotas mensuales: {prestamo.calcular_cuota()}"
        else: return "Prestamo"

    def hipoteca(self):
        if self.aprobacion:
            hipoteca = Hipoteca(self.monto, self.tasa_interes, self.plazo_meses)
            return f"Hipoteca, cuotas mensuales: {hipoteca.calcular_cuota()}"
        else: return "hipoteca"

    def Seleccion_transaccion(self):
        self.tipo_transaccion = self.tipo_transaccion.lower()
        if self.tipo_transaccion == "prestamo":
            resultado_prestamo = self.Prestamo()
            return resultado_prestamo
        elif self.tipo_transaccion == "hipoteca":
            resultado_hipoteca = self.hipoteca()
            return resultado_hipoteca
        else:
            return "Error: Tipo de transacción no válida"


class PrestamoPersonal:
    def __init__(self, monto, tasa_interes, plazo):
        self.monto = monto
        self.tasa_interes = tasa_interes
        self.plazo_meses = plazo

    def calcular_cuota(self):
        tasa_mensual = self.tasa_interes / 12 / 100
        cuota = (self.monto * tasa_mensual) / (1 - (1 + tasa_mensual) ** -self.plazo_meses)
        return f"{cuota:.2f}"


class Hipoteca:
    def __init__(self, monto, tasa_interes, plazo):
        self.monto = monto
        self.tasa_interes = tasa_interes
        self.plazo_meses = plazo

    def calcular_cuota(self):
        tasa_mensual = self.tasa_interes / 12 / 100
        cuota = (self.monto * tasa_mensual) / (1 - (1 + tasa_mensual) ** -self.plazo_meses)
        return f"{cuota:.2f}"


class Cliente:
    def __init__(self, nombre, identificacion, fecha_nacimiento, direccion, telefono):
        self.nombre = nombre
        self.identificacion = identificacion
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.telefono = telefono


class Banco:
    def __init__(self, nombre_banco):
        self.nombre = nombre_banco
        self.clientes = []
        self.transacciones = []
        self.numero_tranferencias = 0
        self.numero_transferencias_denegadas = 0

    def agregar_solicitantes(self, clientes):
        for cliente in clientes:
            self.clientes.append(cliente)

    def agregar_transacciones(self, transacciones):
        for transaccion in transacciones:
            self.transacciones.append(transaccion)

    def mostrar_solicitantes(self):
        print("Clientes del Banco Vera Pichincha:")
        print("{:<15}{:<20}{:<20}{:<20}{:<20}".format("Nombre", "Identificación", "Fecha Nacimiento", "Dirección", "Teléfono"))
        for cliente in self.clientes:
            print("{:<15}{:<20}{:<20}{:<20}{:<20}".format(cliente.nombre, cliente.identificacion, cliente.fecha_nacimiento, cliente.direccion, cliente.telefono))

    def mostrar_transacciones_aceptadas(self):
        print("Transacciones del Banco Vera Pichincha:")
        print("{:<12}{:<9}{:<19}{:<20}{:<20}{:<30}{:<20}".format("Cliente", "Monto", "Tasa de Interés", "Plazo en Meses", "Garantia", "Tipo de transacciones", "Numero de transaccion"))
        for transaccion in self.transacciones:
            if transaccion.aprobacion:
                self.numero_tranferencias += 1
                cuota = transaccion.Seleccion_transaccion()
                print("{:<12}{:<15}{:<20}{:<13}{:<12}{:<45}{:<20}".format(transaccion.solicitante, transaccion.monto, transaccion.tasa_interes, transaccion.plazo_meses, transaccion.garantia, cuota, self.numero_tranferencias))
    
    def mostrar_tranaciones_denegadas(self):
        print("transacciones denegadas:")
        print("{:<15}{:<9}{:<26}{:<20}".format("Solicitante", "Monto","Tipo de transacciones", "numero")) 
        for transaccion in self.transacciones:
            if transaccion.aprobacion == False:
                self.numero_transferencias_denegadas += 1
                tipo_transaccion = transaccion.Seleccion_transaccion()
                print("{:<15}{:<15}{:<23}{:<20}".format(transaccion.solicitante, transaccion.monto, tipo_transaccion, self.numero_transferencias_denegadas))

        
            
                


cliente1 = Cliente("Kendryd", "0974647475125", "07/02/2001", "Mi_casa", "0998111338")
cliente2 = Cliente("Carlos", "0973647475574", "07/02/2002", "Mi_empresa", "0906485338")
cliente3 = Cliente("Juan", "0974647385575", "07/02/2007", "Mi_carro", "0911485338")

Primer_producto = Transaccion_bancaria(cliente1.nombre, "prestamo", 300, 2, 3, True, "Mi casa", "estoy pobre")
Segundo_producto = Transaccion_bancaria(cliente2.nombre, "prestamo", 360, 1, 2, False, "Mi casa", "estoy con hambre")
tercer_producto = Transaccion_bancaria(cliente3.nombre, "hipoteca", 400, 5, 1, True, "Mi casa", "cansado")

Banco_1 = Banco("Vera_Pichincha")
Banco_1.agregar_solicitantes([cliente1, cliente2, cliente3])
Banco_1.agregar_transacciones([Primer_producto, Segundo_producto, tercer_producto])


if __name__ == "__main__":
    print("")
    print(f"                                          {Banco_1.nombre                                     }")
    Banco_1.mostrar_solicitantes()
    print("----------------------------------------------------------")
    Banco_1.mostrar_transacciones_aceptadas()
    print("----------------------------------------------------------")
    Banco_1.mostrar_tranaciones_denegadas()
    print("")
