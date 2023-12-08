#/usr/bin/python3
# Autor: Walter  Villanueva 
# Año: 2023
import sys,os
import signal, time
import re
from tabulate import tabulate
from colorama import Fore, Back, Style
# Colores
RED = Fore.RED
AZUL = Fore.BLUE
NEGRO = Fore.BLACK
CYAN = Fore.CYAN
VERDE = Fore.GREEN
AMARRILLO = Fore.YELLOW
LIGHTCYAN = Fore.LIGHTCYAN_EX
LIGHTBLUE = Fore.LIGHTBLUE_EX
BORRAR = Style.RESET_ALL

# Controlar la señal ctrl_C
def terminar(signal,frame):
    print(f"\n\n{RED}[¡] Saliendo...{BORRAR}\n")
    sys.exit(0)
signal.signal(signal.SIGINT,terminar)

#Varibles glboales
validar_nombre = r'^[a-zA-ZÁ-ñ ]+$'
validar_numero = r'^[0-9]{9}$'
validar_edad = r'^[0-9]{2}$'
validar_correo = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(?:com|pe)$'  
class Archivo():
     def __init__(self):
         self.archivo = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingrese el nombre del archivo:{BORRAR} ")

class añadir_registro(Archivo):
    
    def validar_archivo(self):
        if self.archivo.lower().endswith('.txt'):
            if os.path.exists(self.archivo):
                print(f"{AMARRILLO}[+]{LIGHTCYAN}El archivo si existe{BORRAR}")
                print(f"{AZUL}+------------------------------+")
                print(f"| Comenzado a añadir registros |")
                print(f"+------------------------------+{BORRAR}\n")
                with open(self.archivo,'a',encoding='utf-8') as file:
                    seguir = True
                    while seguir:
                        nombre = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingrese el nombre de la persona: {BORRAR}")
                        numero = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingresa el número de la persona: {BORRAR}")
                        edad = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingrese la edad: {BORRAR}")
                        correo = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingrese el email: {BORRAR}")
                        direccion = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingresa la dirección: {BORRAR}")

                        if re.match(validar_nombre,nombre) and re.match(validar_numero,numero) and re.match(validar_edad,edad) and re.match(validar_correo,correo):
                        

                            registro = f"{nombre};{numero};{edad};{correo};{direccion}"

                            file.writelines([registro, "\n"])
                            op = 3
                            while op == 3:
                                    try:
                                        print(f"{AMARRILLO}[+]{LIGHTCYAN} Desea seguir ingresando registros:")
                                        print(f"{VERDE}[1].{LIGHTCYAN}SI")
                                        print(f"{RED}[2].{LIGHTCYAN}NO{BORRAR}")

                                        op = int(input(f"{AMARRILLO}[+]{LIGHTCYAN}Eliga una Opción [1 , 2]: {BORRAR}"))
                                        if op == 1:
                                            op = 1
                                            break
                                        elif op == 2:
                                            # Garantizar que los doatos han sido escritos
                                            file.flush()
                                            # Cerrar el archivo
                                            file.close()
                                            print(f"{AMARRILLO}[+]{LIGHTCYAN}Datos ingresados correctamente.{BORRAR}")
                                            op = 2
                                            seguir = False
                                    
                                    
                                        else:
                                            print(f"{RED}[¡]Opción no disponible{BORRAR}")
                                            op = 3
                                    except Exception as e:
                                        print(f"{RED}[¡] Opción no valida{BORRAR}")
                                        op = 3
                        else:
                            print(f"{Fore.LIGHTRED_EX}[!] Datos no correctos{Style.RESET_ALL}")
                            print(f"{AMARRILLO}[+]{VERDE}Solo: Números de 9 dígitos, Edades(0-100),Email(.com,.pe){BORRAR}")

            else:
                print(f"{RED}[+]El archivo no existe{BORRAR}")
                print(f"{LIGHTCYAN}[+]Creando el archivo{BORRAR}")
                with open(self.archivo,'a',encoding='utf-8') as file:
                    seguir = True
                    while seguir:
                            nombre = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingrese el nombre: {BORRAR}")
                            numero = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingresa el número: {BORRAR}")
                            edad = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingrese la edad: {BORRAR}")
                            correo = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingrese el email: {BORRAR}")
                            direccion = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingresa la dirección: {BORRAR}")

                            if re.match(validar_nombre,nombre) and re.match(validar_numero,numero) and re.match(validar_edad,edad) and re.match(validar_correo,correo):
                        

                                registro = f"{nombre};{numero};{edad};{correo};{direccion}"

                                file.writelines([registro, "\n"])
                                op = 3
                                while op == 3:
                                    try:
                                        print(f"{AMARRILLO}[+]{LIGHTCYAN} Desea seguir ingresando registros:")
                                        print(f"{VERDE}[1].{LIGHTCYAN}SI")
                                        print(f"{RED}[2].{LIGHTCYAN}NO{BORRAR}")

                                        op = int(input(f"{AMARRILLO}[+]{LIGHTCYAN}Eliga una Opción [1 , 2]: {BORRAR}"))
                                        if op == 1:
                                            op = 1
                                            break
                                        elif op == 2:
                                            # Garantizar que los doatos han sido escritos
                                            file.flush()
                                        # Cerrar el archivo
                                            file.close()
                                            print(f"{AMARRILLO}[+]{LIGHTCYAN}Datos ingresados correctamente.{BORRAR}")
                                            op = 2
                                            seguir = False
                                    
                                        else:
                                            print(f"{RED}[¡]Opción no disponible{BORRAR}")
                                            op = 3
                                    except Exception as e:
                                        print(f"{RED}[¡] Opción no valida{BORRAR}")
                                        op = 3
                            else:   
                                print(f"{Fore.LIGHTRED_EX}[!] Datos no correctos{Style.RESET_ALL}")
                                print(f"{AMARRILLO}[+]{VERDE}Solo: Números de 9 digitos, Edades(0-100), Email(.com,.pe){BORRAR}")
   
        else:
            print(f"{RED}[!] No es un archivo .txt{BORRAR}")
   
class listar_registros(Archivo):
   
    def listar(self):
        if self.archivo.lower().endswith('.txt'):
            if os.path.exists(self.archivo):
                print(f"{AMARRILLO}[+]{LIGHTCYAN}El archivo si existe{BORRAR}")
                print(f"{AZUL}+-------------------+")
                print(f"| Listando registros|")
                print(f"+-------------------+{BORRAR}\n")
                
                with open(self.archivo,'r',encoding='utf-8') as file:
                    # Leemos el archivo
                    registros = file.readlines()
                    
                    header = [f"{AZUL}Nombre", "Número", "Edad","Correo",f"Dirección{BORRAR}"]
                    data = []
                    
                    for registro in registros:
                        
                        if len(registro.strip()) > 0:
                        
                            valores = registro.strip().split(';')
                            # añadimos a data para que se pueda mostrar en la tabla
                            if valores:
                                data.append(valores)
     
                    if data:
                        table = tabulate(data, headers=header, tablefmt="fancy_grid")
                        print(table)
                    else:
                        print(f"{RED}[¡] No hay registros.{BORRAR}\n")
                    
            else:
                print(f"{RED}[¡]El archivo no existe{BORRAR}")
        else:
            print(f"{RED}[!] No es un archivo .txt{BORRAR}")

class modificar_registro(Archivo):
    def modificar(self):
        if self.archivo.lower().endswith('.txt'):
            if os.path.exists(self.archivo):
                print(f"{AMARRILLO}[+]{LIGHTCYAN}El archivo si existe{BORRAR}")
                print(f"{AZUL}+-----------------------+")
                print(f"| Modificando registros |")
                print(f"+-----------------------+{BORRAR}\n")
        
                registro_buscado =input(f"{AMARRILLO}[+]{LIGHTBLUE}Ingresa el registro que desea buscar( por campo nombre,número,edad,correo, o dirección):{BORRAR}  ")
                registro_encontrado = False
                with open(self.archivo,'r',encoding="utf-8")as file:
                    # Leemos el archivo
                    registros = file.readlines()
                   
                    for i,registro in enumerate(registros):
                        
                        if len(registro.strip()) > 0:
                            registro2 = registro.strip().split(';')
                            
                        
                            registro_completo = registro2
                            
                        
                            if registro_buscado in registro_completo:
                                print(f"{VERDE}[+]Registro encontrado{BORRAR}")
                                registro_encontrado = True
                                datos_nuevos = True
                            if registro_encontrado:
                                while datos_nuevos == True:
                                    print(f"{AMARRILLO}[+]{LIGHTBLUE}Ingresa los nuevos datos del registro (nombre, número,edad,correo, dirección){BORRAR} ")
                                    nombre = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingrese el nombre: {BORRAR}")
                                    numero = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingresa el número: {BORRAR}")
                                    edad = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingrese la edad: {BORRAR}")
                                    correo = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingrese el correo: {BORRAR}")
                                    direccion = input(f"{AMARRILLO}[+]{LIGHTCYAN}Ingresa la dirección: {BORRAR}")

                                    nuevos_datos = f"{nombre};{numero};{edad};{correo};{direccion}"
                                
                                
                    
                                    if re.match(validar_nombre,nombre) and re.match(validar_numero,numero) and re.match(validar_edad,edad) and re.match(validar_correo,correo) :
                                        print(f"{AMARRILLO}[+]Datos válidos.{BORRAR}")
                                        registros[i] = nuevos_datos + "\n"
                                

                                        with open(self.archivo, 'w', encoding="utf-8") as file:
                                            file.writelines(registros)

                                            print(f"{AMARRILLO}[+]{VERDE}Registro modificado exitosamente.{BORRAR}")
                                            datos_nuevos = False
                                            registro_encontrado = True
                                            break
                                    else:
                                        print(f"{RED}[¡] Datos no correctos{BORRAR}")
                                        print(f"{AMARRILLO}[+]{VERDE}Solo: Números de 9 digitos, Edades(0-100), Email(.com,.pe){BORRAR}")
                                        datos_nuevos = True

                if not registro_encontrado:
                    print(f"{AMARRILLO}[+]{RED}Registro no encontrado.{BORRAR}")

            
            else:
                print(f"{RED}[¡]El archivo no existe{BORRAR}")

        else:
            print(f"{RED}[!] No es un archivo .txt{BORRAR}")

class borrar_registro(Archivo):
    def borrar(self):
        if self.archivo.lower().endswith('.txt'):
            if os.path.isfile(self.archivo):
                print(f"{AMARRILLO}[+]{LIGHTCYAN}El archivo si existe{BORRAR}")
                print(f"{AZUL}+--------------------+")
                print(f"| Borrando registros |")
                print(f"+--------------------+{BORRAR}\n")

                registro_buscado =input(f"{AMARRILLO}[+]{LIGHTBLUE}Ingresa el registro que desea eliminar (por campo nombre,número,edad,correo o direccion):{BORRAR}  ")

                registro_encontrado = False
                with open(self.archivo,'r',encoding="utf-8")as file:
                    # Leemos el archivo
                    registros = file.readlines()
                    for i,registro in enumerate(registros):
                        
                        if len(registro.strip()) > 0:
                            registro_completo = registro.strip().split(';')
                          
                            if registro_buscado in registro_completo:

                                registro_encontrado = True
                       
                            if registro_encontrado:
                                print(f"{Fore.YELLOW}[+]{Style.RESET_ALL}{Fore.BLUE}Eliminando el registro{Style.RESET_ALL}")
                                time.sleep(2)
                                nuevos_datos = ""
                                registros[i] = nuevos_datos + "\n"

                                with open(self.archivo, 'w', encoding="utf-8") as file:
                                    file.writelines(registros)

                                    print(f"{AMARRILLO}[+]{VERDE}Registro eliminado exitosamente.{Style.RESET_ALL}")
                                    break
                if not registro_encontrado:
                    print(f"{RED}[¡] Registro a eliminar no encontrado{BORRAR}")
                        

                
            else:
                print(f"{RED}[¡]El archivo no existe{BORRAR}")
        else:
             print(f"{RED}[!] No es un archivo .txt{BORRAR}")

class Menu:
    @classmethod
    def mostrar_menu(self):
        while True:
            try:
                print(f"{AMARRILLO}+-------------------------+")
                print(f"| 1.Añadir un registro    |")
                print(f"| 2.Listar los registros  |")
                print(f"| 3.Modificar un registro |")
                print(f"| 4.Borrar un registro    |")
                print(f"| 5.Finalizar             |")
                print(f"+-------------------------+")
                print(f"+ Agenda de Personas      +")
                print(f"+-------------------------+{BORRAR}")
                op = int(input(f"{AMARRILLO}[+]{LIGHTCYAN}Eliga una opción que desea realizar(1,2,3,4,5): {BORRAR}"))
                
                if op == 1:
                    añadir = añadir_registro()
                    añadir.validar_archivo()
                elif op == 2:
                    listar = listar_registros()
                    listar.listar()
                elif op == 3:
                    modificar = modificar_registro()
                    modificar.modificar()
                elif op == 4:
                    eliminar = borrar_registro()
                    eliminar.borrar()
                elif op == 5:
                    print(f"{AMARRILLO}[+]Programa Finalizado.{BORRAR}")
                    break
                    sys.exit(0)
                elif op == 6:
                    print(f"{RED}[¡] Opción no disponinble{BORRAR}")
               
            
            except Exception as e:
                print(f"{RED}[!]Parámetro no encontrado...{BORRAR}")
     

if __name__ == '__main__':
    Menu.mostrar_menu()
