import utileria as ut
import bosque_aleatorio as ba
import os
import random

# use el dataset de los vinos, de la libreta de pandas

url = "https://archive.ics.uci.edu/static/public/186/wine+quality.zip"
archivo = "datos/wine.zip"
archivo_datos = "datos/winequality-red.csv"

if not os.path.exists("datos"):
    os.makedirs("datos")
if not os.path.exists(archivo):
    ut.descarga_datos(url, archivo)
    ut.descomprime_zip(archivo)

datos = ut.lee_csv(
    archivo_datos,
    separador=";"
)

for d in datos:
    for k in d:
        d[k] = float(d[k])
    d['quality'] = 1 if d['quality'] >= 6 else 0

target = 'quality'

random.seed(42)
random.shuffle(datos)

N = int(0.8 * len(datos))
datos_entrenamiento = datos[:N]
datos_validacion = datos[N:]

# prueba con diferentes numeros de arboles, profundidad y variables por nodo:
# primero numero de arboles 

print("\nNUMERO DE ARBOLES")
print('M'.center(10) + 'Ein'.center(15) + 'Eout'.center(15))
print('-' * 40)

for M in [1, 5, 10, 20, 50]:
    bosque = ba.entrena_bosque(
        datos_entrenamiento,
        target,
        M=M,
        max_profundidad=5,
        variables_seleccionadas=5
    )
    
    ein = ba.evalua_bosque(bosque, datos_entrenamiento, target)
    eout = ba.evalua_bosque(bosque, datos_validacion, target)
    
    print(f'{M}'.center(10) + f'{ein:.2f}'.center(15) + f'{eout:.2f}'.center(15))
print('-' * 40)

# profundidad

print("\nPROFUNDIDAD")
print('d'.center(10) + 'Ein'.center(15) + 'Eout'.center(15))
print('-' * 40)

for profundidad in [1, 3, 5, 10, 15]:
    bosque = ba.entrena_bosque(
        datos_entrenamiento,
        target,
        M=10,
        max_profundidad=profundidad,
        variables_seleccionadas=5
    )
    
    ein = ba.evalua_bosque(bosque, datos_entrenamiento, target)
    eout = ba.evalua_bosque(bosque, datos_validacion, target)
    
    print(f'{profundidad}'.center(10) + f'{ein:.2f}'.center(15) + f'{eout:.2f}'.center(15))
print('-' * 40)

# variables por nodo

print("\nVARIABLES POR NODO")
print('k'.center(10) + 'Ein'.center(15) + 'Eout'.center(15))
print('-' * 40)

for k in [1, 3, 5, 10, 20]:
    bosque = ba.entrena_bosque(
        datos_entrenamiento,
        target,
        M=10,
        max_profundidad=5,
        variables_seleccionadas=k
    )
    
    ein = ba.evalua_bosque(bosque, datos_entrenamiento, target)
    eout = ba.evalua_bosque(bosque, datos_validacion, target)
    
    print(f'{k}'.center(10) + f'{ein:.2f}'.center(15) + f'{eout:.2f}'.center(15))
print('-' * 40)