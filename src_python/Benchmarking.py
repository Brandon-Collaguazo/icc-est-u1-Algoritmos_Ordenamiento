import time

class benchmarking:
    def __init__(self):
        print('Benchmarking inicializado')
    
    def medir_tiempo(self, func, array):
        inicio = time.perf_counter()
        func(array.copy())
        fin = time.perf_counter()
        return fin - inicio
    
    def contar_con_curren_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return fin - inicio
    
    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio) / 1_000_000_000.0