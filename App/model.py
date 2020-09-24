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
import sys
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import listiterator as it
from DISClib.DataStructures import liststructure as lt

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""
    
def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1
    
def loadCSVFile (file, cmpfunction=None):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def catalogo_de_peliculas():
    catalog = {'peliculas': None,
               'director': None,
               'actores':None,
               'productoras': None,
               'genero': None,
               'pais': None,
               'fecha de estreno': None}

    catalog['peliculas'] = lt.newList('ARRAY_LIST')
    catalog['director'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=comparar_director)
    catalog['actores'] = mp.newMap(1000,
                                   maptype='CHAINING',
                                   loadfactor=0.7,
                                   comparefunction=compareActorsByName)
    catalog['productoras'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=comparar_productoras_por_nombre)
    catalog['genero'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=comparar_generos
                                )
    catalog['pais'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=comparar_paises)
    catalog['fecha de estreno'] = mp.newMap(500,
                                 maptype='PROBING',
                                 loadfactor=0.5)

    return catalog

# Funciones para agregar informacion al catalogo
 
def newActor(name):
    """Designed by: Juliana Andrea Galeano Caicedo"""
    actor = {"nombre": None,
            "peliculas":None,
            "cantidad de peliculas":None,
            "votacion_promedio":None}
    actor['nombre'] = name
    actor["peliculas"] = lt.newList()
    return actor
   
def nuevo_pais(pais):
    pais_lleno={"pais":None,
                "peliculas":None
                }
    pais_lleno["pais"]=pais
    pais_lleno["peliculas"]=lt.newList()
    
    return pais_lleno   
   
def nueva_productora(productora):
    productora_llena={"nombre":None,
                "peliculas":None,
                "cantidad de peliculas":None,
                "votacion_promedio":None
                }
    productora_llena["nombre"]=productora
    productora_llena["peliculas"]=lt.newList()

    return productora_llena

def nuevo_genero(genero):
    """Designed by: Diego Alejandro Camelo Giraldo"""
    genero_lleno={"genero":None,
                "peliculas":None
                }
    genero_lleno["genero"]=genero
    genero_lleno["peliculas"]=lt.newList()

    return genero_lleno
def nuevo_director(director):
    "Designed by: Nicolas Godoy"
    dic_lleno={"director":None,
                "peliculas":None
                }
    dic_lleno["director"]=director
    dic_lleno["peliculas"]=lt.newList()
    return dic_lleno
   
def agregar_genero_pelicula(catalogo,genero,pelicula):
    """Designed by: Diego Alejandro Camelo Giraldo"""
    genero_completo=catalogo["genero"]
    comprobante=mp.contains(genero_completo,genero)
    if comprobante:
        entry=mp.get(genero_completo,genero)
        valor=me.getValue(entry)
    else:
        valor=nuevo_genero(genero)
        mp.put(genero_completo,genero,valor)
    lt.addLast(valor["peliculas"],pelicula)

def agregar_pelicula(catalogo, pelicula):
    lt.addLast(catalogo['peliculas'],pelicula)
    
def agregar_pelicula_pais(catalogo,pais,pelicula):
    productora_completa=catalogo["pais"]
    comprobante=mp.contains(productora_completa,pais)
    if comprobante:
        entry=mp.get(productora_completa,pais)
        valor=me.getValue(entry)
    else:
        valor=nuevo_pais(pais)
        mp.put(productora_completa,pais,valor)
    lt.addLast(valor["peliculas"],pelicula)

def agregar_pelicula_director(catalogo,director,pelicula):
    "Designed by: Nicolas Godoy"
    productora_completa=catalogo["director"]
    comprobante=mp.contains(productora_completa,director)
    if comprobante:
        entry=mp.get(productora_completa,director)
        valor=me.getValue(entry)
    else:
        valor=nuevo_director(director)
        mp.put(productora_completa,director,valor)
    lt.addLast(valor["peliculas"],pelicula)
    
def agregar_pelicula_productora(catalogo,productora,pelicula):
    productora_completa=catalogo["productoras"]
    comprobante=mp.contains(productora_completa,productora)
    if comprobante:
        entry=mp.get(productora_completa,productora)
        valor=me.getValue(entry)
    else:
        valor=nueva_productora(productora)
        mp.put(productora_completa,productora,valor)
    lt.addLast(valor["peliculas"],pelicula)

def addmovie(catalog, movie):
    """Designed by: Juliana Andrea Galeano Caicedo"""
    lt.addLast(catalog['peliculas'], movie)

def addmovieactor(catalog, actorname, movie):
    """Designed by: Juliana Andrea Galeano Caicedo"""
    actors = catalog['actores']
    existactor = mp.contains(actors, actorname)
    if existactor:
        entry = mp.get(actors, actorname)
        actor = me.getValue(entry)
    else:
        actor = newActor(actorname)
        mp.put(actors, actorname, actor)
    lt.addLast(actor['peliculas'], movie)

def addmovieactor(catalog, actorname, movie):
    """Designed by: Juliana Andrea Galeano Caicedo"""
    actors = catalog['actores']
    existactor = mp.contains(actors, actorname)
    if existactor:
        entry = mp.get(actors, actorname)
        actor = me.getValue(entry)
    else:
        actor = newActor(actorname)
        mp.put(actors, actorname, actor)
    lt.addLast(actor['peliculas'], movie)

def conversor_entre_cvs_Juli(id_movie,iterador):
    """Designed by: Juliana Andrea Galeano Caicedo"""
    while it.hasNext(iterador):
        counter=it.next(iterador)
        if counter['id']==id_movie:
            return counter
       
# ==============================
# Funciones de consulta
# ==============================
def buscar_productora(catalogo,productora):
    la_productora=mp.get(catalogo['productoras'],productora)
    if la_productora:
        return me.getValue(la_productora)
    return None

def buscar_genero(catalogo,genero):
    """Designed by: Diego Alejandro Camelo Giraldo"""
    el_genero=mp.get(catalogo['genero'],genero)
    if el_genero:
        return me.getValue(el_genero)
    return None
   
def buscar_pais(catalogo,pais):
    el_pais=mp.get(catalogo['pais'],pais)
    if el_pais:
        return me.getValue(el_pais)
    return None

def buscar_director(catalogo,director):
    "Designed by: Nicolas Godoy"
    el_director=mp.get(catalogo['director'],director)
    if el_director:
        return me.getValue(el_director)
    return None 
   
def getMoviesByActor(catalog, actorname):
    """Designed by: Juliana Andrea Galeano Caicedo"""
    actor = mp.get(catalog['actores'], actorname)
    if actor:
        return me.getValue(actor)
    return None
# ==============================
# Funciones de Comparacion
# ==============================
def comparar_productoras_por_nombre(keyname, productora):
    """
    Compara dos nombres de productores. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(productora)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def comparar_paises(keyname, pais):
    """
    Compara dos nombres de productores. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(pais)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def comparar_generos(keyname,genero):
    """
    Compara dos generos, el primero es una cadena. 
    El segundo es entry de un map
    """
    genre=me.getKey(genero)
    if (keyname == genre):
        return 0
    elif (keyname > genre):
        return 1
    else:
        return -1
     
def compareActorsByName(keyname, actor):
    """Designed by: Juliana Andrea Galeano Caicedo"""
    authentry = me.getKey(actor)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1
def comparar_director(keyname,genero):
    """
    Compara dos generos, el primero es una cadena. 
    El segundo es entry de un map
    """
    "Designed by: Nicolas Godoy"
    genre=me.getKey(genero)
    if (keyname == genre):
        return 0
    elif (keyname > genre):
        return 1
    else:
        return -1

     
