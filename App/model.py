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
               'productoras': None,
               'genero': None,
               'pais': None,
               'fecha de estreno': None}

    catalog['peliculas'] = lt.newList('ARRAY_LIST')
    catalog['director'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4)
    catalog['productoras'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=comparar_productoras_por_nombre)
    catalog['genero'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7
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
 

def nueva_productora(productora):
    productora_llena={"nombre":None,
                "peliculas":None,
                "cantidad de peliculas":None,
                "votacion_promedio":None
                }
    productora_llena["nombre"]=productora
    productora_llena["peliculas"]=lt.newList()

    return productora_llena

def agregar_pelicula(catalogo, pelicula):
    lt.addLast(catalogo['peliculas'],pelicula)
    mp.put(catalogo['pais'],pelicula['production_countries'],pelicula)
    

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



# ==============================
# Funciones de consulta
# ==============================
def buscar_productora(catalogo,productora):
    la_productora=mp.get(catalogo['productoras'],productora)
    if la_productora:
        return me.getValue(la_productora)
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
