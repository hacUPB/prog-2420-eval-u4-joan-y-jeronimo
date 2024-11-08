from funciones import *

def main():
    while True:
       print(f"1.Listar archivos presentes en la ruta actual o ingresar una ruta donde buscar los archivos.\n 2.Procesar archivo de texto (.txt).\n 3.Procesar archivo separado por comas (.csv).\n 4.Salir")
       dato=input("Opción a seleccionar: ")
       if dato=='1':
           print(f"1. listar archivos presentes en la ruta actual\n2.ingresar una ruta donde buscar los archivos.")
           lst=input("dato a selecionar: ")
           if lst=="1":
               ruta=os.getcwd()# ruta acutual de archivos de la pc
               Listar_Archivos(ruta)
           elif lst=="2":
               ruta=input("digite la ruta de acceso que desea enlistar: ")
               Listar_Archivos(ruta)
           else:
               print("usted esta seleccionando datos no validos por favor seleccione de nuevo el proceso a realizar")

       elif dato=='2':
           ruta=input("digite la ruta del archivo que desea(si desea continuar en ruta agrege *): ")
           archivo=input ("digite el archivo que desea editar (ejm: 1.txt)")
           try:
                if ruta=="*":
                    ruta=os.getcwd()
                    ruta_completa=os.path.join(ruta,archivo)
                    print(f"Que accion dese arealizar:\n 1.Contar número de palabras \n 2.Reemplazar una palabra por otra \n 3.Contar el número de caracteres")
                    lst=input("dato a selecionar: ")
                    if lst=='1':
                        conteo = Contar_Words(ruta_completa)
                        print(f"El número de palabras es:{conteo}")
                    if lst=='2':
                        palabra_buscar=input("ingrese la palabra que desea buscar")
                        palabra_remplazar=input("ingrese la palabra que desea remplazar")
                        reemplazar(ruta_completa, palabra_buscar, palabra_remplazar)
                    if lst=='3':
                        N_caracteres_sin=Contar_sin_espacios(ruta_completa)
                        N_caracteres=Contar_con_espacios(ruta_completa)
                        print(f"Número total de caracteres (incluyendo espacios): {N_caracteres_sin}") 
                        print(f"Número total de caracteres (sin espacios): {N_caracteres}")

                else:
                    print(f"Que accion dese arealizar:\n 1.Contar número de palabras \n 2.Reemplazar una palabra por otra \n 3.Contar el número de caracteres")
                    lst=input("dato a selecionar: ")
                    if lst=='1':
                        conteo = Contar_Words(ruta_completa)
                        print(f"El número de palabras es:{conteo}")
                    if lst=='2':
                        palabra_buscar=input("ingrese la palabra que desea buscar")
                        palabra_remplazar=input("ingrese la palabra que desea remplazar")
                        (ruta_completa, palabra_buscar, palabra_remplazar)
                    if lst=='3':
                        N_caracteres_sin=Contar_sin_espacios(ruta_completa)
                        N_caracteres=Contar_con_espacios(ruta_completa)
                        print(f"Número total de caracteres (incluyendo espacios): {N_caracteres_sin}") 
                        print(f"Número total de caracteres (sin espacios): {N_caracteres}")
           except FileNotFoundError: #excepción en Python que se produce cuando intentas acceder a un archivo o directorio que no existe
                print(f"Error: La ruta '{ruta}' no existe.")
           except PermissionError: #exepcion cuando no se cuenta con los permisos adecuados
                print(f"Error: No tienes permisos para acceder a la ruta '{ruta}'.")
       elif dato=='3':
            rute=input("digite la ruta del archivo que desea(si desea continuar en ruta agrege +): ")
            csvalue= input ("digite el archivo que desea editar (ejm: 1.csv)")
            try:
                if rute == "+":
                        print(f"Que accion dese arealizar:\n 1.Mostrar las 15 primeras filas \n 2.Calcular Estadísticas \n 3.Graficar una columna completa con los datos")
                        lst=input("dato a selecionar: ")
                        primerasFilas = primeras_filas(ruta_completa)
                        print(f" Las primeras 15 filas son: {primerasFilas}")
                else: 
                    print(f"Que accion dese arealizar:\n 1.Mostrar las 15 primeras filas \n 2.Calcular Estadísticas \n 3.Graficar una columna completa con los datos")
                    lst=input("dato a selecionar: ")
                    primerasFilas = primeras_filas(ruta_completa)
                    print(f" Las primeras 15 filas son: {primerasFilas}")
                    

       elif dato=='4':
           break
       else:
           print("usted esta seleccionando datos no validos por favor seleccione de nuevo el proceso a realizar")



if __name__ == "__main__":
        main()
