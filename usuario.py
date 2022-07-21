from models import Clientes
from utils import limpiarPantalla
from clientes import lista, modificar_dato
from clientes import crearCliente
import time
from clientes import buscar

ruta_archivo = "./archivos/clientes.txt"
def gestionClientes():
    while True:
        print("Sub Menu: GESTION DE USUARIOS")
        print("1. Crear cliente")
        print("2. Mostrar cliente")
        print("3. Modificar cliente")
        print("4. Buscar Usuario")
        print("5. Salir al menu principal") 
        op = input("Ingrese una opcion: ")

        match (op):
            case "1":
                print("-Esta apunto de crear un nuevo usuario")
                print("-Rellena con los que datos que pidan ◉‿◉ ")
                time.sleep(3)
                limpiarPantalla()
                crearCliente()
            case "2":
                limpiarPantalla()
                lista()
            case "3":
                print("Menu de modificar dato")
                print("1. -Dirrecion")
                print("2. -Telefono")
                print("3. -Correo Electronico")
                print("4. -Regresar al sub menu")
                op = input("Ingrese una opcion:")

                match(op):
                    case "1":
                        filas = int(input("-Ingrese la fila: "))
                        columna = int(2)
                        nuevo_dato = input("-Ingrese el nuevo dato: ")
                        fila = modificar(filas, [columna],nuevo_dato)
                        encontrado = fila.split(";")
                        print(encontrado)
                    case "2":
                        filas = int(input("-Ingrese fila del cambio: "))
                        columna = int(3)
                        nuevo_dato = input("-Ingrese el nuevo dato ")
                        fila = str(modificar_dato(ruta_archivo, [filas], columna, nuevo_dato))
                        encontrado = fila.split(";")
                        print(encontrado)
                    case "3":
                        filas = int(input(-"Ingrese la fila: "))
                        columna = int(4)
                        nuevo_dato = input("-Ingrese el nuevo dato: ")
                        fila = modificar(filas, [columna],nuevo_dato)
                        encontrado = fila.split(";")
                        print(encontrado)
                    case "4":
                        time.sleep(2)
                        print("-Regresando al sub menu")
                    case _:
                        print("-Opcion incorrecta") 
            case "4":
                limpiarPantalla()
                Dni = input("-Ingrese el numero de DNI: ")
                fila = str(buscar(Dni))
                encontrado = fila.split(";")
                print(encontrado)                   
            case _:
                print("-Opcion Incorrecta")
                time.sleep(2)
gestionClientes()