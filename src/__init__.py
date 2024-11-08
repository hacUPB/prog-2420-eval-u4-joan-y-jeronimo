import mathplotlib.pyplot as plt
import csv


    
   
def Listar_archivos():
        print("Archivos en la ruta actual:")
        print("Archivos1.txt")
        print("Archivos2.csv")
        print("datos.csv")
    
def Procesar_txt():
    archivo = input("Ingrese el nombre del archivo de texto a buscar: ")
    try:
        f = open(archivo, "r")
        texto = f.read()
        f.close()
    except FileNotFoundError:
        print("El archivo no existe")
    
    while True:
        print("Submenú")
        print("1.Contar número de palabras")
        print("2. Reemplazar una palabra")
        print("3. Contar el número de caracteres") 
        print("4. Volver al menú") 

        option = input(int("Seleccione una opción"))
        if option == 1:
            Contar_palabras(texto)
        elif option == 2:
            Reemplazar_Palabras(archivo,texto) 
        elif option == 3:
            Contar_Caracteres(texto)
        elif option == 4:
            False
        else:
            print("Solo puedes elegir opciones del 1 al 4") 

def Contar_palabras(texto):
    print(f"El número de palabras en el archivo es {len(texto.split())}")

def Reemplazar_Palabras(archivo,texto):
    palabra_reemplazar = input("Ingrese la palabra que desea cambiar")
    reemplazo = input("Ingrese la nueva palabra")

    texto_modificado = texto.replace(palabra_reemplazar,reemplazo)

    f = open(archivo, "w")
    f.write(texto_modificado) 
    f.close()
    print(f"La palabra {palabra_reemplazar} fue reemplazada por {reemplazo}")

def Contar_Caracteres(texto):
    Total_texto = len(texto)
    Caracteres_sin_espacio = len(texto.replace("","")) 
    print(f"El numero total de caracteres (contando espacios) {Total_texto}")
    print(f"Número de caractreres (sin espacios): {Caracteres_sin_espacio}")

def Procesar_archivos_csv():
    archivo = input("ingrese el nombre del archivo csv: ")
    try:
        f = open(archivo,newline = "")
        lector_csv = csv.reader(f) 
        encabezado = next(lector_csv)
    except FileNotFoundError:
        print("El archivo no existe")
    finally:
        f.close
    
    while True:

        print(f"Submenu csv")
        print(f"1.Mostrar las primeras 15 líneas")
        print(f"2. Calcular estadísticas de una columna")
        print(f"3.Graficar una columna completa")
        print(f"4.Volver al menú")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_15_lineas(archivo)
        elif opcion == "2":
            Calcular_estadísticas(archivo)
        elif opcion =="3":
            Graficar_Columna(archivo)
        elif opcion =="4":
            print("Saliendo del programa")
            False
        else: 
            print("Opción no válida")

def mostrar_15_lineas(archivo):
    with open(archivo,newline = "") as f:
        lector_csv = csv.DictReader(f)
        for i,fila in enumerate(lector_csv):
            if i >= 15:
                False
            print(fila)

def Calcular_estadísticas(archivo):
    columna = input("Ingrese el nombre de la columna: ")
    with open(archivo, newline="") as f:
        lector_csv = csv.DictReader(f)
        datos = [float(fila[columna]) for fila in lector_csv if fila[columna].replace(".","",1).isdigit()]
    if not datos:
        print("No se encontró la columna seleccionada")

    num_datos = len(datos)
    promedio = sum(datos)/num_datos
    mediana = sorted(datos)[num_datos//2] if num_datos % 2 != 0 else (sorted(datos)[num_datos // 2 -1] + sorted(datos)[num_datos // 2])/2
    valor_max = max(datos)
    valor_min = min(datos)

    print(f"Número de datos: {num_datos}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Máximo: {valor_max}")
    print(f"mínimo: {valor_min}")

def Graficar_Columna(archivo):
    columna = input("Ingrese el nombre de la columna: ")
    with open(archivo,newline="") as f:
        lector_csv = csv.DictReader(f)
        datos = [float(fila[columna]) for fila in lector_csv if fila[columna].replace(".","",1).isdigit()]

    if not datos:
        print("No se encontraron datos")

    plt.plot(datos)
    plt.title(f"Gráfica de columna {columna}")
    plt.xlabel("índice")
    plt.ylabel("Valor")
    plt.show()

    while True:
        print(f"Menú Principal \n 1. Listar archivos presentes en la ruta actual (o añadir una ruta donde buscar los archivos)\n 2.Procesar archivo .txt \n 3. Procesar archivo separado por comas \n 4. Salir")

        opcion = input(int("Seleccione lo que desea realizar: "))
        if opcion == 1:
            Listar_archivos()
        elif opcion == 2:
            Procesar_txt()
        elif opcion == 3:
           Procesar_archivos_csv()
        elif opcion == 4:
            print("Saliste del programa. ¡Hasta pronto!")
        else:
            print("Por favor elija una opción del 1 al 4")


if __name__ == "__main__":
    main()











           


