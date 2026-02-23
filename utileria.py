"""
Este archivo contiene funciones que se utilizan en el miniproyecto.

Como leer archivos de datos y formatearlos para que sean utilizados en los algoritmos.
"""

from urllib3 import request
import urllib.request
import zipfile

def descarga_datos(url, archivo):
    """
    Descarga un archivo de datos de una URL.
    
    Parámetros
    ----------
    url : str
        URL de donde se descargará el archivo.
    archivo : str
        Nombre del archivo donde se guardará la descarga.
    """
    urllib.request.urlretrieve(url, archivo)
    return None

def descomprime_zip(archivo, directorio='datos'):
    """
    Descomprime un archivo zip.
    
    Parámetros
    ----------
    archivo : str
        Nombre del archivo zip.
    directorio : str
        Directorio donde se descomprimirá el archivo.
    """
    with zipfile.ZipFile(archivo, 'r') as zip_ref:
        zip_ref.extractall(directorio)
    return None

# cambie la funcion esta porque no me funcionaba para el dataset de los vinos
# trate de no cambiar mucho de este archivo
def lee_csv(archivo, atributos=None, separador=','):
    with open(archivo, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        
    if atributos is None:   
        columnas = [
            c.strip().replace('"', '') 
            for c in lineas[0].strip().split(separador)
        ]
    else:
        columnas = atributos
        
    datos = []
    for l in lineas[1:]:
        valores = l.strip().split(separador)
        datos.append({
            c: v for c, v in zip(columnas, valores)
        })
        
    return datos