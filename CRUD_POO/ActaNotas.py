from persona import Alumno, Profesor
from universidad import Facultad
import json
import re

class Semestre():
    def __init__(self, smtr ):
        self.__IdSmt= 0
        self.semestre = smtr

    def mostrar(self):
        print(f"semestre: {self.semestre}")

class Asignatura():
    def __init__(self, nombreAsg):
        self.__IdAsig = 0 
        self.asignatura = nombreAsg
    def mostrar(self):
         print(f"ASIGNATURA: {self.asignatura}")

class Notas():
    #atrinuto estatico
    _secuencia = 0
    def __init__(self,facul,semestre, carrera, asignatura,estudiante, profe,n1,n2,exm1,n3,n4,exm2):
        Notas._secuencia += 1
        self.__IdNt= Notas._secuencia
        self.facultad = facul
        self.carrera = carrera
        self.asignatura = asignatura
        self.alumno = estudiante
        self.profesor = profe
        self.semestre = semestre
        self.nota1 = n1
        self.nota2 = n2
        self.examen1 = exm1
        self.parcial1 = 0 #este valor se calcula 
        self.nota3 = n3
        self.nota4 = n4
        self.examen2 = exm2
        #estos valores se calculan 
        self.parcial2 = 0  
        self.notafinal = 0 
        self.estado = ""
    
    def id(self):
        #funcioin ternaria
        return -1 if self.__IdNt == 0 else self.__IdNt
    
    def calcularNota(self):
        self.parcial1 = round(self.nota1 + self.nota2 + self.examen1, 2)
        self.parcial2 = round(self.nota3 + self.nota4 + self.examen2, 2)
        self.notafinal  = self.parcial1 + self.parcial2
        
        #cambiamos el estado del alumno segun su nota final 
        # operador ternario
        self.estado = "APROBADO" if self.notafinal >= 70 else "REPROBADO"

    def mostrar(self):
        pass
        




def load_data():
    try:
        with open('Studen.json', 'r') as json_file:
            data_studen = json.load(json_file)
            return data_studen
    except FileNotFoundError:
        # si no existe
        return {}

def validar_entrada(caracter):
    patron = r"^[A-Za-z\s]+$"
    return re.match(patron, caracter) is not None
def validar_numero(numero, rango):
    patron = r"^\d*\.?\d*$"  
    if re.match(patron, numero) is not None:
        valor = float(numero)
        if rango[0] <= valor <= rango[1]:
            return True
        else:
            print(f"El valor debe estar en el rango de {rango[0]} a {rango[1]}.")
    else:
        print("Ingrese un valor numérico válido.")
    return False

def menuNotas():
    #las variables que comience con Inst son consideradas variables de instancias de clases
    student = load_data()
    try:
        while(True):
            print("Elija algunas de estas opciones:")
            print("1) Ingresar datos estudiantes ...")
            print("2) Buscar datos de estudiantes ...")
            print("3) Salir")
            lv_resp = int(input("Opción :").strip())
            if lv_resp == 1:
                print("registre de manera correcta los siguiente datos:")

                while (True):

                    lv_facultad = input("\nIngrese La facultad:")
                    if validar_entrada(lv_facultad):
                        Inst_facultad = Facultad(lv_facultad)
                    else:
                        print("ingrese solo opciones validas")
                        continue

                    
                    
                    lv_Semestre = input("\nIngrese el Semestre:")
                    Inst_Semestre = Semestre(lv_Semestre)


                    lv_carrera = input("Ingrese el nombre de la carrera:")
                    if validar_entrada(lv_carrera):
                         Inst_facultad.AgregarCarrera(lv_carrera)
                    else:
                        print("sera redireccionado al formulario inicial")
                        continue

                    print("************")
                    lv_asignatura = input("\nIngrese el nombre de la Asignatura:")
                    
                    if validar_entrada(lv_asignatura):
                         Inst_asignatura = Asignatura(lv_asignatura)
                    else:
                        print("sera redireccionado al formulario inicial")
                        continue

                    print("************REGISTRE DATOS DEL ESTUDIANTE***********")
                    Lv_estudentNom= input("\nNombre:")
                    Lv_estudentApe= input("Apellido:")
                    Inst_alumno = Alumno(Lv_estudentNom,Lv_estudentApe)
                    
                    print("************REGISTRE DATOS DEL PROFESOR")
                    Lv_ProfeNom= input("\nNombre:")
                    Lv_ProfeApe= input("Apellido:")
                    Inst_Profesor = Profesor(Lv_ProfeNom,Lv_ProfeApe)

                    rango_notas = (0, 15)
                    rango_examenes = (0, 20)

                    print("\nIngrese las notas del estudiante")
                    ln_nota1 = input("Nota 1: ")
                    while not validar_numero(ln_nota1,rango_notas):
                        print("Ingrese un valor numérico válido para la Nota 1.")
                        ln_nota1 = input("Nota 1: ")
                    ln_nota1 = float(ln_nota1)

                    ln_nota2 = input("Nota 2: ")
                    while not validar_numero(ln_nota2,rango_notas):
                        print("Ingrese un valor numérico válido para la Nota 2.")
                        ln_nota2 = input("Nota 2: ")
                    ln_nota2 = float(ln_nota2)

                    ln_examen1 = input("Examen 1: ")
                    while not validar_numero(ln_examen1, rango_examenes):
                        print("Ingrese un valor numérico válido para el Examen 1.")
                        ln_examen1 = input("Examen 1: ")
                    ln_examen1 = float(ln_examen1)

                    ln_nota3 = input("Nota 3: ")
                    while not validar_numero(ln_nota3, rango_notas):
                        print("Ingrese un valor numérico válido para la Nota 3.")
                        ln_nota3 = input("Nota 3: ")
                    ln_nota3 = float(ln_nota3)

                    ln_nota4 = input("Nota 4: ")
                    while not validar_numero(ln_nota4, rango_notas):
                        print("Ingrese un valor numérico válido para la Nota 4.")
                        ln_nota4 = input("Nota 4: ")
                    ln_nota4 = float(ln_nota4)

                    ln_examen2 = input("Examen 2: ")
                    while not validar_numero(ln_examen2, rango_examenes):
                        print("Ingrese un valor numérico válido para el Examen 2.")
                        ln_examen2 = input("Examen 2: ")
                    ln_examen2 = float(ln_examen2)


                    Inst_nota = Notas(Inst_facultad,Inst_Semestre,Inst_facultad.carreras,Inst_asignatura,Inst_alumno,Inst_Profesor,ln_nota1,ln_nota2,ln_examen1,ln_nota3,ln_nota4,ln_examen2)
                    Inst_nota.calcularNota()

                    #funcion lambda
                    nombre_completo = lambda nombre, apellido: f"{nombre} {apellido}"

                    nombre_completo_alumno = nombre_completo(Lv_estudentNom, Lv_estudentApe)
                    nombre_completo_profe = nombre_completo(Lv_ProfeNom, Lv_ProfeApe)

                    student[nombre_completo_alumno] ={
                        "Facultad": lv_facultad,
                        "semestre": lv_Semestre,
                        "carrera": lv_carrera,
                        "asignatura": lv_asignatura,
                        "profesor": nombre_completo_profe,
                        "notas": {
                            "nota1": ln_nota1,
                            "nota2": ln_nota2,
                            "examen1": ln_examen1,
                            "Parcial1": Inst_nota.parcial1,
                            "nota3": ln_nota3,
                            "nota4": ln_nota4,
                            "examen2":ln_examen2,
                            "Parcial2": Inst_nota.parcial2,
                            "Nota_final":Inst_nota.notafinal,
                            "estado": Inst_nota.estado
                        }

                    }
                    
                    print("Desea guardar los datos en un archivos json - (S / N)")
                    lv_confirmacion = input("=>")
                    if lv_confirmacion.upper() == "S":
                        #creamos (o guardamos datos en el archivo 
                        with open('Studen.json', 'w') as json_file:
                            json.dump(student, json_file, indent=4) # ident = sirve para mostrar de forma estrucutra los datos del archivo
                    elif lv_confirmacion.upper() == "N":
                        print("No se guardaron los datos")
                    else:
                        print("No se ingreso ninguna de las opciones")
                    break

            elif lv_resp == 2:
                print("Ingrese nombre y apellido del estudiante que desea buscar")
                lv_buscar = input("=>")
                with open('Studen.json', 'r') as json_file:
                    data = json.load(json_file)
                    student_info = data.get(lv_buscar)
                    if student_info:
                        print("el estudiante esta dentro de nuestro registro")
                        print(f"\nInformacion del alumno: {lv_buscar}")
                        for key, value in student_info.items():
                            if key == "notas":
                                print("Detalle de notas:")
                                for ntkey , ntvalue in value.items():
                                    print(f"{ntkey} : {ntvalue}")
                            else:
                                print(f"{key}: {value}")
                    else:
                        print(f"El estudiante  {lv_buscar} no se encuentra en nuestro registro")

            elif lv_resp == 3:
                print("saliendo del programa")
                break
            else:
                print("opcion invalida digite solo opciones disponibles")
    except ValueError:
        print("Error: Ingrese un número válido como opción.")
    
menuNotas()