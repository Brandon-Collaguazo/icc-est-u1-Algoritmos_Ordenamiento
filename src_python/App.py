import random
from Benchmarking import benchmarking
from SortMethods import SortMethods
import matplotlib.pyplot as pt

def buildArreglo(tamanio, arreglo_base=None):
    if arreglo_base is None:
        arreglo_base = []
    
    faltante = tamanio - len(arreglo_base)
    for _ in range(faltante):
        arreglo_base.append(random.randint(0, 10000))
    return arreglo_base

if __name__ == "__main__":
    print("Iniciando benchmark...")
    sMethods = SortMethods()
    benchmark = benchmarking()
    
    tamanios = [5000, 10000, 30000, 50000, 100000]
    resultados = []
    arreglo_anterior = None
    
    for tam in tamanios:
        arreglo_actual = buildArreglo(tam, arreglo_anterior)
        arreglo_anterior = arreglo_actual.copy()
        metodos = {
            'Burbuja': sMethods.sort_bubble,
            'Insercion': sMethods.sort_insertion,
            'Seleccion': sMethods.sort_selection
        }
        
        for nombre, metodo in metodos.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo_actual)
            tuplaResultado = (tam, nombre, tiempo)
            resultados.append(tuplaResultado)
            print(f'Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos')
    
    tiempo_by_metodo = {
        'Burbuja': [],
        'Insercion': [],
        'Seleccion': [],
    }

    for tam, nombre, tiempo in resultados:
        tiempo_by_metodo[nombre].append(tiempo)

    #FIGURA
    pt.figure(figsize=(10, 6))

    for nombre, tiempo in tiempo_by_metodo.items():
        pt.plot(tamanios, tiempo, label = nombre, marker='0')
    
    pt.title("Análisis de Métodos de Ordenamieto\nBrandon Collaguazo", fontsize=12)
    pt.xlabel("Tamaño")
    pt.ylabel("Método")
    pt.grid()
    pt.show()