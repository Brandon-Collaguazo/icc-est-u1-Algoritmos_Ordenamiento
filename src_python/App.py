import random
from Benchmarking import benchmarking
from SortMethods import SortMethods
import matplotlib.pyplot as pt

def buildArreglo(tamanio):
    array = []
    for i in range(tamanio):
        numero = random.randint(0, 10000)
        array.append(numero)
    return array

if __name__ == "__main__":
    print("Iniciando benchmark...")
    sMethods = SortMethods()
    benchmark = benchmarking()
    
    tamanios = [5000, 10000, 30000, 50000, 100000]
    resultados = []
    
    for tam in tamanios:
        arreglo = buildArreglo(tam)
        metodos = {
            'Burbuja': sMethods.sort_bubble,
            'Burbuja mejorado': sMethods.sort_bubble_optimized,
            'Insercion': sMethods.sort_insertion,
            'Seleccion': sMethods.sort_selection,
            'Shell': sMethods.sort_shell,
        }
        
        for nombre, metodo in metodos.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo.copy())
            tuplaResultado = (tam, nombre, tiempo)
            resultados.append(tuplaResultado)
            print(f'Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos')
    
    tiempo_by_metodo = {
        'Burbuja': [],
        'Burbuja mejorado': [],
        'Insercion': [],
        'Seleccion': [],
        'Shell': [],
    }

    for tam, nombre, tiempo in resultados:
        tiempo_by_metodo[nombre].append(tiempo)

    #FIGURA
    pt.figure(figsize=(10, 6))

    for nombre, tiempo in tiempo_by_metodo.items():
        pt.plot(tamanios, tiempo, label = nombre, marker='o')
    
    pt.title("Comparación de algoritmos de ordenamiento\nBrandon Collaguazo", fontsize=12)
    pt.xlabel("Tamaño")
    pt.ylabel("Tiempo en segundos")
    pt.legend()
    pt.grid()
    pt.show()