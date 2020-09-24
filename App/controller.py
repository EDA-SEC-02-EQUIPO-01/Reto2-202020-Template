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

import config as cf
from App import model as m
import csv
from DISClib.ADT import list as lt
from DISClib.DataStructures import liststructure as lt 
from DISClib.DataStructures import listiterator as it

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""
def loadlst (file):
    lst = m.loadCSVFile(file,m.compareRecordIds) 
    first=lt.firstElement(lst)
    last=lt.lastElement(lst)
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    print ("Primera película:\n"+ " "*18 + "Título: " + first["original_title"]+ "\n"+ " "*18 + 
    "Fecha de estreno: "+ first["release_date"]+"\n"+ " "*18 + "Promedio de votación: "+ first["vote_average"]+
    "\n"+ " "*18 + "Número de votos: " +first["vote_count"]+"\n"+ " "*18 + "Idioma: "+ first["original_language"])
    print ("última película:\n"+ " "*18 + "Título: " + last["original_title"]+ "\n"+ " "*18 + 
    "Fecha de estreno: "+ last["release_date"]+"\n"+ " "*18 + "Promedio de votación: "+ last["vote_average"]+
    "\n"+ " "*18 + "Número de votos: " + last["vote_count"]+"\n"+ " "*18 + "Idioma: "+ last["original_language"])
    return lst

def loadCast (file):
    lst = m.loadCSVFile("themoviesdb\SmallMoviesDetailsCleaned.csv") 
    return lst

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def crear_catalogo():
    catalogo=m.catalogo_de_peliculas()
    return catalogo



# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def cargar_productoras(catalogo):
    archivo_prod = cf.data_dir + "themoviesdb\SmallMoviesDetailsCleaned.csv"
    dialect = csv.excel()
    dialect.delimiter=";"
    input_file = csv.DictReader(open(archivo_prod,encoding="utf-8"),dialect=dialect)
    for prod in input_file:
        m.agregar_pelicula(catalogo,prod)
        productoras = prod['production_companies'].split(",")  
        for productora in productoras:
            m.agregar_pelicula_productora(catalogo,productora.strip(),prod)

def cargar_genero(catalogo):
    archivo_prod = cf.data_dir + "themoviesdb\SmallMoviesDetailsCleaned.csv"
    dialect = csv.excel()
    dialect.delimiter=";"
    input_file = csv.DictReader(open(archivo_prod,encoding="utf-8"),dialect=dialect)
    for prod in input_file:
        generos = prod['genres'].split(",")  
        for genero in generos:
            lst_genero=genero.split("|")
            for un_genero in lst_genero:
                m.agregar_genero_pelicula(catalogo,un_genero.strip(),prod)

def promediar(productora,caracteristica='vote_average'):
    total=0
    iterator = it.newIterator(productora["peliculas"])
    while it.hasNext(iterator):
        movie = it.next(iterator)
        total+= float(movie[caracteristica])
    total=round((total/lt.size(productora["peliculas"])),1)
    return total

def obtener_productoras(catalogo, productora):
    """ 
        Permite obtener una productora y sus datos respectivos en un catalogo de 
        productoras
        catalogo: El catalogo de productoras donde se buscara la productora elegida
        productora: La productora (str) que se desea buscar en el catalogo
                                                                            """
    la_productora=m.buscar_productora(catalogo,productora)
    return la_productora    

def obtener_genero(catalogo, genero):
    el_genero=m.buscar_genero(catalogo,genero)
    return el_genero  
