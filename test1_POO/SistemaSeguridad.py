class Usuario:
    def __init__(self, nom, ape, email,cell,direc, ):
        self.nombre = nom
        self.apellido = ape
        self.correo = email
        self.telefono = cell
        self.direccion = direc
        #self.rol = rol
        
    def mostrarUser(self):
        print("Bienvenido ")
        print("DATOS PERSONALES DE USUARIO")
        print(f"nombre: {self.nombre} apellido: {self.apellido}")
        print(f"TELEFONO: {self.telefono} direccion: {self.direccion}")
        print()
        
class Rol: 
    def __init__(self,CodigoRol,rol):
        self.IdRol = CodigoRol
        self.asignar_rol= rol
        
    def MostrarRol(self,userNombre,UserApellido):
        print(f"Codigo: {self.IdRol}")
        print(f"sr {userNombre} {UserApellido} Usted se le asigno el rol de {self.asignar_rol}")
        print()

class Permisos:
    def __init__(self, idrol):
        self.idpermiso = idrol
        self.listapermisos = []
        
    def AsignarPermisos(self):
        if self.idpermiso == "001":
            self.listapermisos = ["agregar tarea","ver calificiaciones","ver horarios"]
        elif self.idpermiso == "002":
            self.listapermisos = ["subir material complementario","tutorias","calificar"]
            

    def mostrarpermisos(self):
        print("SUS permisos estan activados ")
        
class Modulo:
    def __init__(self, permisosAsig):
          self.mdl = permisosAsig

    def mostrarModulo(self):
        print("SUS Modulos asignados fueron, considerando su rol")
        for modulos in self.mdl.listapermisos:
            print(f"- {modulos}")
        

#aplicando asociacion 
user1 = Usuario("Freddy","Zambrano","fzambranoq2@gmail.com","0912738247","nueva naranjal")
user1.mostrarUser()
#aplicando asociacion
rol1= Rol( "001","estudiante")
rol1.MostrarRol(user1.nombre,user1.apellido)
#aplicando asociacion
Permiso1 = Permisos(rol1.IdRol)
Permiso1.AsignarPermisos()
Permiso1.mostrarpermisos()

#agregacion  entre permisos y modulos 
modulo1 = Modulo(Permiso1)
modulo1.mostrarModulo()

