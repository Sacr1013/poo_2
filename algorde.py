import pandas as pd

def pro_dats(data):
    df = pd.json_normalize(data)
    df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce') # el errors='coerce' ...
    return df


#coso de ordenamiento 1
def quicsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicsort(left) + middle + quicsort(right)

#coso de ordenamiento 2
def mergesort(arr):
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
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)
