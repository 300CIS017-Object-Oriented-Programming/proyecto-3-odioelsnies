import os
from SNIEScontroller import SNIESController

def main():
    # Verificar el directorio actual
    print("Directorio actual:", os.getcwd())
    print("Archivos en el directorio actual:", os.listdir())

    # Ruta a la carpeta "inputs"
    carpeta_inputs = "inputs"

    # Instanciar el controlador
    controlador = SNIESController(carpeta_inputs)

    # Pedir una palabra clave al usuario
    palabra_clave = input("Ingresa la palabra clave para buscar: ")

    try:
        resultados = controlador.buscarPorPalabra(palabra_clave)
        # Mostrar los resultados
        if resultados:
            print(f"Se encontraron {len(resultados)} resultados:")
            for fila in resultados:
                print(f"- {fila}")  # Imprime la fila completa
        else:
            print("No se encontraron resultados para la palabra clave ingresada.")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar la carpeta '{carpeta_inputs}'. Verifica la ruta y el nombre de la carpeta.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()


