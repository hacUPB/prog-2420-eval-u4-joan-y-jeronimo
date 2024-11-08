import os
import csv

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
    
def Contar_Words(ruta_completa): #Si estoy en una ruta distinata a la actual no me lo coge
    with open(ruta_completa,"r") as texto:
        cantidad =len(texto.read().split())
    return cantidad

def reemplazar(ruta_completa,palabra,reemplazo):
    with open(ruta_completa,"r") as leido:
        leer = leido.read()
    print(leer)
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

import csv

def imprimir_filas(ruta_completa):
    with open(ruta_completa, 'r') as archivo:
        lineas = archivo.readlines()
        for i in range(15):
            print(i)

def estadisticas(ruta_completa,columna:str):
    try:
        with open(ruta_completa,"r") as file:
            leer = csv.DictReader(file)
            data = []
            for filas in leer:
                data.append(float(filas[columna]))
        num_data = len(data)
        prom = sum(data)/num_data
        ordenados = data.sorted()
    except ValueError:
        print("La columna "{columna}" no tiene valores numéricos")
    #mediana
        if num_data % 2 == 0:
            indice_1 = num_data/2 
            indice_2 = num_data/2 + 1
            mediana = (ordenados[indice_1]+ordenados[indice_2])/2
        else: 
            indice = num_data/2 + 0.5
            mediana = ordenados[indice]
    #maximo
        maximo = max(data)
    #minimo:
        minimo = min(data)

        print(f"El número de datos de la columna {columna} es {num_data}")
        print(f"El promedio es {prom}  la mediana: {mediana}")
        print(f"El valor máximo es {maximo} y el mínimo es {minimo}")
        
          
    
    
#la función calcula el número de datos, el promedio, la mediana, el valor máximo y el mínimo de dicha columna