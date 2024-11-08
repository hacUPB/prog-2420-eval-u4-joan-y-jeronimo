from funciones import *

def main():
    while True:
        print("1. Listar archivos de la ruta actual o añadir una ruta donde buscar archivos")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Salir")

        dato = input("Seleccione una opción: ")

        if dato == '1':
            print("1. Listar archivos presentes en la ruta actual")
            print("2. Ingresar una ruta donde buscar los archivos")
            seleccion = input("Elija una opción válida: ")

            if seleccion == "1":
                ruta = os.getcwd()
                Listar_Archivos(ruta)
            elif seleccion == "2":
                ruta = input("Digite la ruta de acceso cuyos archivos desea enlistar: ")
                Listar_Archivos(ruta)
            else:
                print("Por favor seleccione una opción válida")

        elif dato == '2':
            ruta = input(
                "Digite la ruta del archivo. "
                "Si quiere permanecer en la ruta actual, digite la palabra ACTUAL: "
            )
            archivo = input("Escriba el nombre del archivo: ")
            ruta_completa = os.path.join(ruta, archivo)

            try:
                if ruta == "ACTUAL":
                    ruta = os.getcwd()
                    ruta_completa = os.path.join(ruta, archivo)
                    print(
                        "¿Qué desea realizar?:\n"
                        "1. Contar número de palabras en archivo\n"
                        "2. Reemplazar una palabra por otra\n"
                        "3. Contar el número de caracteres"
                    )
                    seleccion = input("Seleccione una opción: ")

                    if seleccion == '1':
                        cantidad = Contar_Words(ruta_completa)
                        print(f"El número de palabras es: {cantidad}")

                    elif seleccion == '2':
                        buscador = input("Ingrese la palabra que desea buscar: ")
                        reemplazo = input("Ingrese la palabra que desea reemplazar: ")
                        reemplazar(ruta_completa, buscador, reemplazo)

                    elif seleccion == '3':
                        n_caracteres_sin = Contar_sin_espacios(ruta_completa)
                        n_caracteres = Contar_con_espacios(ruta_completa)
                        print(f"Número total de caracteres (sin espacios): {n_caracteres_sin}")
                        print(f"Número total de caracteres (incluyendo espacios): {n_caracteres}")
                else:
                    print("¿Qué desea realizar?")
                    print("1. Contar número de palabras")
                    print("2. Reemplazar una palabra por otra")
                    print("3. Contar el número de caracteres")
                    eleccion = input("Decida: ")

                    if eleccion == '1':
                        cantidad = Contar_Words(ruta_completa)
                        print(f"El número de palabras es: {cantidad}")

                    elif eleccion == '2':
                        palabra_buscar = input("Ingrese la palabra que desea reemplazar: ")
                        palabra_reemplazar = input("Ingrese la nueva palabra: ")
                        reemplazar(ruta_completa, palabra_buscar, palabra_reemplazar)

                    elif eleccion == '3':
                        sin_espacio = Contar_sin_espacios(ruta_completa)
                        con_espacio = Contar_con_espacios(ruta_completa)
                        print(f"Número total de caracteres (contando espacios): {con_espacio}")
                        print(f"Número total de caracteres (sin espacios): {sin_espacio}")

            except FileNotFoundError:
                print(f"La ruta {ruta} no fue encontrada. Intente de nuevo.")
            except PermissionError:
                print(f"No tienes permisos para acceder a la ruta {ruta}. Intente de nuevo.")

        elif dato == '3':
            ruta = input(
                "Digite la ruta del archivo. Si quiere continuar en la ruta actual, "
                "escriba ACTUAL: "
            )
            archivo = input("Nombre del archivo (por ejemplo, tabla.csv): ")
            ruta_completa = os.path.join(ruta, archivo)

            if ruta == "ACTUAL":
                ruta = os.getcwd()
                ruta_completa = os.path.join(ruta, archivo)
                print("¿Qué desea realizar?")
                print("1. Mostrar las 15 primeras filas")
                print("2. Calcular Estadísticas")
                print("3. Graficar una columna completa con los datos")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    imprimir_filas(ruta_completa)
                elif opcion == "2":
                    columna = input("Escriba el nombre de la columna: ")
                    estadisticas(ruta_completa, columna)
                elif opcion == "3":
                    columna = input("¿Qué columna desea graficar? ")
                    Graficar_Columna(ruta_completa)

            else:
                ruta_completa = os.path.join(ruta, archivo)
                print("¿Qué desea realizar?")
                print("1. Mostrar las 15 primeras filas")
                print("2. Calcular Estadísticas")
                print("3. Graficar una columna completa con los datos")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    imprimir_filas(ruta_completa)
                elif opcion == "2":
                    columna = input("Escriba el nombre de la columna: ")
                    estadisticas(ruta_completa, columna)
                elif opcion == "3":
                    columna = input("¿Qué columna desea graficar? ")
                    Graficar_Columna(ruta_completa)

        elif dato == '4':
            break
        else:
            print("Por favor seleccione una opción válida.")

if __name__ == "__main__":
    main()
