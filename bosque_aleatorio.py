from arboles_numericos import entrena_arbol
from collections import Counter 
import random

def entrena_bosque(datos, target, M, 
                   max_profundidad=None, acc_nodo=1.0, min_ejemplos=0,
                   variables_seleccionadas=None):
    """
    Entrena un bosque aleatorio
    
    Parámetros:
    -----------
    datos: list(dict)
    target: str
    M: número de árboles
    variables_seleccionadas: int (número de atributos por nodo)
    
    Regresa:
    --------
    bosque: list(NodoN)
    """
    
    bosque = []
    
    for _ in range(M):
        
        muestra = bootstrap(datos)
        
        arbol = entrena_arbol(
            muestra,
            target,
            clase_default=None,
            max_profundidad=max_profundidad,
            acc_nodo=acc_nodo,
            min_ejemplos=min_ejemplos,
            variables_seleccionadas=variables_seleccionadas
        )
        
        bosque.append(arbol)
    
    return bosque

def bootstrap(datos):
    return [random.choice(datos) for _ in range(len(datos))]

def predice_bosque(bosque, instancia):
    predicciones = [arbol.predice(instancia) for arbol in bosque]
    conteo = Counter(predicciones)
    return conteo.most_common(1)[0][0]


def evalua_bosque(bosque, datos, target):
    predicciones = predice_bosque_dataset(bosque, datos)
    correctos = sum(1 for p, d in zip(predicciones, datos) if p == d[target])
    return correctos / len(datos)

def predice_bosque_dataset(bosque, datos):
    return [predice_bosque(bosque, d) for d in datos]