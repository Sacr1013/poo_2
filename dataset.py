
from algorde import DatProceso
class Dataset:

    def __init__(self, dataframe):
        self.df = dataframe
        self.proceso = DatProceso()
    #selecciona la variable
    def seleccionar_variable(self, variable):
        if variable in self.df.columns:
            return self.df[variable]
        else:
            raise ValueError("Variable no encontrada en el DataFrame")
   #sel elige el algoritmo de ordenamiento
    def ordenar_datos(self, variable, algoritmo):
        if variable not in self.df.columns:
            raise ValueError(f"Variable {variable} no encontrada en el DataFrame")
        
        # Ordenar utilizando el algoritmo seleccionado
        if algoritmo == 'quicksort':
            return self.proceso.quicsort(by=variable, kind='quicksort')
        elif algoritmo == 'mergesort':
            return self.proceso.mergesort(by=variable, kind='mergesort')
        else:
            raise ValueError("Algoritmo de ordenamiento no reconocido")
        
    def ordenar_quicksort(self, variable):
        sorted_df = self.df.sort_values(by=variable, kind='quicksort')
        return sorted_df

    def ordenar_mergesort(self, variable):
        sorted_df = self.df.sort_values(by=variable, kind='mergesort')
        return sorted_df

