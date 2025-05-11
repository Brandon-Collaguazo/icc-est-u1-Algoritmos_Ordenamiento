class SortMethods:

    def sort_bubble(self, array: list[int]):
        array = array.copy()
        n = len(array)
        for i in range(n):
            for j in range(i + 1, n):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
        return array
    
    def sort_bubble_optimized(self, array: list[int]):
        array = array.copy()
        n = len(array)
        for i in range (n):
            swapp = False
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapp = True
            if not swapp:
                break
        return array

    def sort_insertion(self, array: list[int]):
        array = array.copy()
        n = len(array)
        for i in range(n):
            aux = array[i]
            j = i - 1
            while j >= 0 and array[j] > aux:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = aux
        return array
    
    def sort_selection(self, array: list[int]):
        array = array.copy()
        n = len(array)
        for i in range(n):
            indexMen = i
            for j in range(i + 1, n):
                if array[j] < array[indexMen]:
                    indexMen = j
            array[i] = array[indexMen] = array[indexMen] = array[i]
        return array
    
    def sort_shell(self, array : list[int]):
        array = array.copy()
        n = len(array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                aux = array[i]
                j = i
                while j >= gap and array[j - gap] > aux:
                    array[j] = array[j - gap]
                    j -= gap
            gap //= 2
        return array