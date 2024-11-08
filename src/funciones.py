import os
import csv
import matplotlib.pyplot as plt

def Listar_Archivos(ruta_acceso):
    archivos = []
    carpetas = []

    elementos = os.listdir(ruta_acceso)
    for i in elementos:
        ruta_completa = os.path.join(ruta_acceso,i)
        verifier = os.path.isfile(ruta_completa)
        if verifier == True:
            archivos.append(i)
        else:
            carpetas.append(i)
    print("Los archivos son los siguientes: ")
    for j in archivos:  
        print(j)
    print("Las carpetas son estas: ")
    for x in carpetas:
        print(x)
    
def Contar_Words(ruta_completa):
    
    with open(ruta_completa,"r") as texto:
        cantidad =len(texto.read().split())
    return cantidad

def reemplazar(ruta_completa,palabra,reemplazo):
    with open(ruta_completa,"r") as leido:
        leer = leido.read()
    modified = leer.replace(palabra,reemplazo)
    with open(ruta_completa,"w") as escribir:
        escribir.write(modified)
    print(modified)
def Contar_sin_espacios(ruta_completa):
    with open(ruta_completa, "r") as archivo:
        leer = archivo.read()
        contador = 0
        for i in leer:
            if i != " ":
                contador+=1
    return contador

def Contar_con_espacios(ruta_completa):
    with open(ruta_completa, "r") as archivo:
        leer = archivo.read()
        contador = 0
        for i in leer:
            contador+=1
    return contador

def imprimir_filas(ruta_completa):
    try:
        with open(ruta_completa, "r") as archivo:
            lineas = archivo.readlines()
            cantidad = len(lineas)
            if cantidad < 15:
                print("Como el archivo no tiene más de 15 filas, se imprimirán todas.")
            contador = 0
            for linea in lineas: 
                print(linea)
                contador += 1
                if contador == 15:
                    break
    except FileNotFoundError:
        print(f"El archivo '{ruta_completa}' no fue encontrado.")
    except PermissionError:
        print(f"No tienes permisos para leer el archivo '{ruta_completa}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def estadisticas(ruta_completa, columna: str):
    try:
        with open(ruta_completa, "r") as file:
            leer = csv.DictReader(file)
            data = []
            for filas in leer:
                data.append(float(filas[columna]))
        
        num_data = len(data)
        if num_data == 0:
            print(f"No hay datos en la columna {columna}")
            return
        
        prom = sum(data) / num_data
        ordenados = sorted(data)

        # Cálculo de la mediana
        if num_data % 2 == 0:
            indice_1 = (num_data // 2 )- 1
            indice_2 = num_data // 2
            mediana = (ordenados[indice_1] + ordenados[indice_2]) / 2
        else:
            indice = num_data // 2
            mediana = ordenados[indice]

        # Máximo y mínimo
        maximo = max(data)
        minimo = min(data)

        print(f"El número de datos de la columna {columna} es {num_data}")
        print(f"El promedio es {prom}, la mediana: {mediana}")
        print(f"El valor máximo es {maximo} y el mínimo es {minimo}")
        
    except ValueError:
        print(f"La columna '{columna}' no tiene valores numéricos")

def Graficar_Columna(ruta_completa):
    columna = input("Ingrese el nombre de la columna: ")
    datos = []

    # Intentar abrir el archivo CSV y leer la columna
    try:
        with open(ruta_completa, newline="") as f:
            lector_csv = csv.DictReader(f)
            
            # Iterar sobre cada fila en el archivo
            for fila in lector_csv:
                valor = fila.get(columna)
                if valor is not None:  # Verifica que la columna existe
                    try:
                        # Intentar convertir el valor a float si es numérico
                        datos.append(float(valor))
                    except ValueError:
                        # Si no es numérico, simplemente lo ignora
                        pass
            # Verificar si se encontraron datos numéricos
            if not datos:
                print("No se encontraron datos numéricos en la columna.")
                return
    except KeyError:
        print(f"La columna '{columna}' no existe en el archivo.")
        return
    except FileNotFoundError:
        print(f"El archivo '{ruta_completa}' no fue encontrado.")
        return

    # Graficar los datos
    plt.plot(datos)
    plt.title(f"Gráfica de columna {columna}")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.show()

          
    
    
