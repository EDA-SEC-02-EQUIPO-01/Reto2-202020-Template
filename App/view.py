"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller as c
assert config
from time import process_time

def imprimir_productoras(productora):
    if productora:
        print('Productora encontrada: ' + productora["nombre"])
        print('Promedio: ' + str(c.promediar(productora)))
        print('Total de peliculas: ' + str(lt.size(productora["peliculas"])))
        
        iterator = it.newIterator(productora["peliculas"])
        while it.hasNext(iterator):
            book = it.next(iterator)
            print('Titulo: ' + book['title'] + '  votacion promedio: ' + book['vote_average'])
    else:
        print('No se encontro la productora')

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""
def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Cargar Catalogo de peliculas")
    print("3- Buscar productoras")
    print("0- Salir")


def main():
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                lstmovies = c.loadlst("themoviesdb\SmallMoviesDetailsCleaned.csv")
                lstcast= c.loadCast("themoviesdb\MoviesCastingRaw-small.csv")
                cont=c.crear_catalogo()
            if int(inputs[0])==2: #opcion 2
                print("Crendo catalogo de peliculas")
                t1_start=process_time()
                c.cargar_productoras(cont)
                print("completado")
                t1_stop=process_time()
                print(f"{t1_stop-t1_start} segundos")
            if int(inputs[0])==3: #opcion 3
                nombre_productora=input("Ingrese la productora que desea investigar\n")
                producer=c.obtener_productoras(cont,nombre_productora)
                imprimir_productoras(producer)

            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________





# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________


# ___________________________________________________
#  Menu principal
# ___________________________________________________
