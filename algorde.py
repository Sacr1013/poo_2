import pandas as pd

class DatProceso:
    def __init__(self):
        pass
    
    def pro_dats(self, data):
        df = pd.json_normalize(data)
        df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce')
        return df

    def quicsort(self, arr, key=lambda x: x):
        if len(arr) <= 1:
            return arr
        pivot = key(arr[len(arr) // 2])
        left = [x for x in arr if key(x) < pivot]
        middle = [x for x in arr if key(x) == pivot]
        right = [x for x in arr if key(x) > pivot]
        return self.quicsort(left, key) + middle + self.quicsort(right, key)

    def mergesort(self, arr, key=lambda x: x):
        if len(arr) <= 1:
            return arr
        def merge(left, right):
            result = []
            left_idx = right_idx = 0
            while left_idx < len(left) and right_idx < len(right):
                if key(left[left_idx]) <= key(right[right_idx]):
                    result.append(left[left_idx])
                    left_idx += 1
                else:
                    result.append(right[right_idx])
                    right_idx += 1
            result.extend(left[left_idx:])
            result.extend(right[right_idx:])
            return result

        mid = len(arr) // 2
        left = self.mergesort(arr[:mid], key)
        right = self.mergesort(arr[mid:], key)
        return merge(left, right)
    

#correcto      