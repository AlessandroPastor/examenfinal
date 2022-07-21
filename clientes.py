from shutil import which
from time import time
from models import Clientes
from utils import limpiarPantalla
import time

ruta_archivo = "./archivos/clientes.txt"

#modificar usuario

def crearCliente():
    Dni = input("Identificacion: ")
    nombres_apellidos = input("Nombres y Apellidos: ")
    direccion = input("Dirección: ")
    telefono = input("Telefono: ")
    email = input("Correo Electronico: ")

    Cliente = Clientes(Dni, nombres_apellidos, direccion, telefono, email)

    archivoCliente = open(ruta_archivo, "a")
    archivoCliente.write(str(Cliente))
    archivoCliente.close()

def lista():
    with open("./archivos/clientes.txt","r") as d:
        for linea in d:
            lista = linea
            print(f'{lista}\n')


def modificar_dato(ruta_archivo, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta_archivo, "r+") as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila - 1].split(";")
            columnas[columna] = nuevo_dato
            contenido[fila - 1] = ";".join(columnas) + "\n"
    with open(ruta_archivo, "w") as archivo:
        archivo.writelines(contenido)

def buscar(Dni):
    busquedadni = None 
    buscarcliente = open(ruta_archivo, "r")
    for linea in buscarcliente.readlines():
        atributos = linea.split(";")
        if Dni == atributos[0]:
            busquedadni =Clientes(atributos[0],atributos[1],atributos[2],atributos[3],atributos[4])        
            break
    print("Es lo que buscas..")
    time.sleep(2)
    buscarcliente.close()
    return busquedadni

