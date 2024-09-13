import pandas as pd

class DatProceso:
    def __init__(self):
        pass
    
    def pro_dats(self, data):
        df = pd.json_normalize(data)
        df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce') # el errors='coerce'es para convertir valores de la columna en datos numéricos 
        return df


    #algoritmo de ordenamiento quicksort
    def quicsort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quicsort(left) + middle + self.quicsort(right)

    #algoritmo de ordenamiento mergesort
    def mergesort(self, arr):
        if len(arr) <= 1:
            return arr
        def merge(left, right):
            result = []
            left_idx = right_idx = 0
            while left_idx < len(left) and right_idx < len(right):
                if left[left_idx] < right[right_idx]:
                    result.append(left[left_idx])
                    left_idx += 1
                else:
                    result.append(right[right_idx])
                    right_idx += 1
            result.extend(left[left_idx:])
            result.extend(right[right_idx:])
            return result

        mid = len(arr) // 2
        left = self.mergesort(arr[:mid])
        right = self.mergesort(arr[mid:])
        return merge(left, right)
