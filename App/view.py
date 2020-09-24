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

def imprimir_pais(productora,lst_alterna):
    if productora:
        print('Pais encontrado: ' + productora["pais"])
        print('Promedio: ' + str(c.promediar(productora)))
        print('Total de peliculas: ' + str(lt.size(productora["peliculas"])))
        
        iterator = it.newIterator(productora["peliculas"])
        while it.hasNext(iterator):
            book = it.next(iterator)
            old_id=book['id']
            iterador_director=it.newIterator(lst_alterna)
            director=c.conversor_entre_cvs(old_id,iterador_director)
            print('Titulo: ' + book['title'] + '  votacion promedio: ' + book['vote_average'] + '  Dirigido por: '+director['director_name'])
    else:
        print('No se encontro la productora')

def imprimir_director(genero):
    """Designed by: Nicolas Godoy"""
    if genero:
        print('Director encontrado: ' + genero["director"])
        print('Promedio: ' + str(c.promediar(genero,'vote_average')))
        print('Total de peliculas: ' + str(lt.size(genero["peliculas"])))
        
        iterator = it.newIterator(genero["peliculas"])
        while it.hasNext(iterator):
            book = it.next(iterator)
            print('Titulo: ' + book['title'] + '  votacion promedio: ' + book['vote_average'])
    else:
        print('No se encontro el director')
      
      
def imprimir_genero(genero):
    """Designed by: Diego Alejandro Camelo Giraldo"""
    if genero:
        print('Genero entendido: ' + genero["genero"])
        print('Promedio: ' + str(c.promediar(genero,'vote_count')))
        print('Total de peliculas: ' + str(lt.size(genero["peliculas"])))
        
        iterator = it.newIterator(genero["peliculas"])
        while it.hasNext(iterator):
            book = it.next(iterator)
            print('Titulo: ' + book['title'] + '  votacion promedio: ' + book['vote_count'])
    else:
        print('No se encontro el genero')
      
def printActorData(actor,lista):
    """Designed by: Juliana Andrea Galeano Caicedo"""
    if actor:
        directores={}
        votacion= lt.newList()
        print('Actor encontrado: ' + actor['nombre'])
        print('Total de peliculas: ' + str(lt.size(actor['peliculas'])))
        iterator = it.newIterator(actor['peliculas'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            if movie["director_name"] in directores:
                directores[movie["director_name"]]+=1
            else:
                directores[movie["director_name"]]=1
            iterador_pelicula=it.newIterator(lista)
            peli=c.conversor(movie['id'],iterador_pelicula)
            lt.addLast(votacion,peli)
            print('Titulo: ' + peli['original_title'])
        promedio=c.promediar_Juli(votacion)
        mascolab=c.Colaboraciones(directores)
        print("Votación promedio: ",promedio)
        print("Director con más colaboraciones: ",mascolab)
    else:
        print('No se encontro el actor')

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
    print("4- Conocer a un actor")
    print("5- Buscar Director")
    print("6- Entender genero")
    print("7- Buscar Pais")
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
            elif int(inputs[0])==2: #opcion 2
                print("Creando catalogo de peliculas")
                t1_start=process_time()
                c.cargar_productoras(cont)
                c.cargar_genero(cont)
                c.loadMoviesByActor(cont)
                c.cargar_directores(cont,lstmovies)
                c.cargar_pais(cont)
                print("completado")
                t1_stop=process_time()
                print(f"{t1_stop-t1_start} segundos")
            elif int(inputs[0])==3: #opcion 3
                nombre_productora=input("Ingrese la productora que desea investigar\n")
                producer=c.obtener_productoras(cont,nombre_productora)
                imprimir_productoras(producer)
            elif int(inputs[0])==4: #opcion 3
                actorname=input("Ingrese el actor que desea conocer\n")
                actor=c.MoviesByActor(cont,actorname)
                printActorData(actor,lstmovies)
            elif int(inputs[0])==5: 
                nombre_director=input("Ingrese el director que desea revisar\n")
                producer=c.obtener_director(cont,nombre_director)
                imprimir_director(producer)
            elif int(inputs[0])==6: #opcion 3
                nombre_genero=input("Ingrese el genero que desea entender\n")
                genre=c.obtener_genero(cont,nombre_genero)
                imprimir_genero(genre)
            elif int(inputs[0])==7:
                nombre_pais=input("ingrese el pais que desea buscar\n")
                country=c.obtener_pais(cont,nombre_pais)
                imprimir_pais(country,lstcast)    
   

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

def conversor_entre_cvs(id_movie,iterador):
    while it.hasNext(iterador):
        counter=it.next(iterador)
        if counter['id']==id_movie:
            return counter
# ___________________________________________________
#  Menu principal
# ___________________________________________________
