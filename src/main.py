import os
from SNIEScontroller import SNIESController

def main():
    #verificar el directorio actual
    print("Directorio actual:", os.getcwd())
    print("Archivos en el directorio actual:", os.listdir())

    #ruta al archivo CSV
    ruta_csv = "admitidos2023.csv"

    #instanciar el controlador
    controlador = SNIESController(ruta_csv)

    #pedir una palabra clave al usuario
    palabra_clave = input("Ingresa la palabra clave para buscar en el programa académico: ")

    try:
        resultados = controlador.buscarPorPalabra(palabra_clave)
        #mostrar los resultados
        if resultados:
            print(f"Se encontraron {len(resultados)} resultados:")
            for programa in resultados:
                print(f"- {programa.programa_academico} (Código SNIES: {programa.codigo_snies})")
        else:
            print("No se encontraron resultados para la palabra clave ingresada.")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{ruta_csv}'. Verifica la ruta y el nombre del archivo.")

if __name__ == "__main__":
    main()
