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
        self.parcial1 = 0 
        self.nota3 = n3
        self.nota4 = n4
        self.examen2 = exm2
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
        self.estado = "APROBADO" if self.notafinal >= 70 else "REPROBADO"
    def mostrar(self):
        pass
        




def load_data():
    try:
        with open('Studen.json', 'r') as json_file:
            data_studen = json.load(json_file)
            return data_studen
    except FileNotFoundError:
        return {} # si no existe





def validar_entrada(caracter):
    patron_entrada = r"^[A-Za-z\s]+$"
    return re.match(patron_entrada, caracter) is not None

def validar_numero(numero, rango):
    patron_numero = r"^\d*\.?\d*$"
    if re.match(patron_numero, numero) is not None:
        valor = float(numero)
        return True  if rango[0] <= valor <= rango[1] else False
    else:
        return False


def definir_range(id):
    def notas(): 
        return [0,15] 
    def examen():
         return [0,20] 
    return notas() if id == 1  else examen()


def menuNotas():
    student = load_data()

    def ingresar_nota(mensaje, rango):
        while True:
            valor = input(mensaje)
            if validar_numero(valor, rango):
                return float(valor)
            else:
                print(f"Ingrese un valor numérico dentro del rango")
                continue

    while True:
        try:
            print("\nElija algunas de estas opciones:")
            print("1) Ingresar datos al sistema")
            print("2) Buscar datos que se encuentre dentro del registro...")
            print("3) Salir\n")
            lv_resp = int(input("Opción:").strip())
            if lv_resp == 1:
                print("Registre de manera correcta los siguiente datos:\n")
                while True:
                    lv_facultad = input("\nIngrese La facultad: ")
                    if validar_entrada(lv_facultad):
                        Inst_facultad = Facultad(lv_facultad)
                    else:
                        print("Ingrese solo opciones válidas")
                        continue

                    lv_Semestre = input("Ingrese el Semestre: ")
                    Inst_Semestre = Semestre(lv_Semestre)

                    lv_carrera = input("Ingrese el nombre de la carrera: ")
                    if validar_entrada(lv_carrera):
                        Inst_facultad.AgregarCarrera(lv_carrera)
                    else:
                        print("Será redireccionado al formulario inicial")
                        continue

                    lv_asignatura = input("Ingrese el nombre de la Asignatura: ")
                    if validar_entrada(lv_asignatura):
                         Inst_asignatura = Asignatura(lv_asignatura)
                    else:
                        print("sera redireccionado al formulario inicial")
                        continue

                    print("\n---------------- REGISTRO DE DATOS DEL ESTUDIANTE ----------------")
                    Lv_estudentNom = input(f"\nIngrese el nombre del estudiante: ")
                    Lv_estudentApe = input(f"Ingrese el apellido del estudiante: ")
                    Inst_alumno = Alumno(Lv_estudentNom, Lv_estudentApe)
                    
                    print("\n---------------- REGISTRO DE DATOS DEL PROFESOR ----------------")
                    Lv_ProfeNom = input(f"\nIngrese el nombre del profesor: ")
                    Lv_ProfeApe = input(f"Ingrese el apellido del profesor: ")
                    Inst_Profesor = Profesor(Lv_ProfeNom, Lv_ProfeApe)


                    print("\nIngrese las notas del estudiante:")
                    ln_nota1 = ingresar_nota("Nota 1: ", definir_range(1))
                    ln_nota2 = ingresar_nota("Nota 2: ", definir_range(1))
                    ln_examen1 = ingresar_nota("Examen 1: ", definir_range(0))
                    ln_nota3 = ingresar_nota("Nota 3: ", definir_range(1))
                    ln_nota4 = ingresar_nota("Nota 4: ", definir_range(1))
                    ln_examen2 = ingresar_nota("Examen 2: ", definir_range(0))

                    
                    Inst_nota = Notas(Inst_facultad,Inst_Semestre,Inst_facultad.carreras,Inst_asignatura,Inst_alumno,Inst_Profesor,ln_nota1,ln_nota2,ln_examen1,ln_nota3,ln_nota4,ln_examen2)
                    Inst_nota.calcularNota()

        
                    nombre_completo = lambda nombre, apellido: f"{nombre} {apellido}"
                    nombre_completo_alumno = nombre_completo(Lv_estudentNom, Lv_estudentApe)
                    nombre_completo_profe = nombre_completo(Lv_ProfeNom, Lv_ProfeApe)
                    
                    id_data = Inst_nota.id()
                    student[id_data]={
                        "Alumno": nombre_completo_alumno,
                        "carnetEstudiante": Inst_alumno.carnet,
                        "Facultad": lv_facultad,
                        "semestre": lv_Semestre,
                        "carrera": lv_carrera,
                        "asignatura": lv_asignatura,
                        "profesor": nombre_completo_profe,
                        "carnet profesor": Inst_Profesor.carnet,
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
                    print("\nDesea guardar los datos en un archivos json - (S / N)")
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
                print("Ingrese el valor que desee buscar (id, estudiante, carrera,profesor y facultad)")
                lv_buscar = input("=> ").lower()
                with open('Studen.json', 'r') as json_file:
                    data = json.load(json_file)

                    results = []
                    for key, student_info in data.items():
                        if lv_buscar == key.lower() or lv_buscar in student_info["Alumno"].lower() or lv_buscar in student_info["carrera"].lower() or lv_buscar in student_info["profesor"].lower() or lv_buscar in student_info["Facultad"].lower():
                            results.append((key, student_info))

                    if results:
                        print("\nResultados de la búsqueda:")
                        for index, (key, student_info) in enumerate(results, start=1):
                            print(f"\n{index}) Información del dato {key}:")
                            for info_key, info_value in student_info.items():
                                if info_key == "notas":
                                    print("\nDetalle de notas:")
                                    for nt_key, nt_value in info_value.items():
                                        print(f"{nt_key} : {nt_value}")
                                else:
                                    print(f"{info_key}: {info_value}")
                            print("---------------------------")  
                    else:
                        print(f"No se encontraron resultados para '{lv_buscar}'.")
                    
                pass
            elif lv_resp == 3:
                print("\nsaliendo del programa")
                break  
            else:
                print("\nOpción inválida, digite solo opciones disponibles.")
        except ValueError:
            print("\nError: Ingrese un número válido como opción.")
            
menuNotas()