from algorde import DatProceso
import pandas as pd

class Dataset:
    def __init__(self, dataframe):
        self.df = dataframe
        self.proceso = DatProceso()

    def seleccionar_variable(self, variable):
        if variable in self.df.columns:
            return self.df[variable].tolist()
        else:
            raise ValueError("Variable no encontrada en el DataFrame")

    def ordenar_datos(self, variable, algoritmo):
        if variable not in self.df.columns:
            raise ValueError(f"Variable {variable} no encontrada en el DataFrame")
        
        datos_a_ordenar = self.seleccionar_variable(variable)
        
        # Crear un DataFrame auxiliar con índices y valores
        df_aux = pd.DataFrame({'indice': range(len(datos_a_ordenar)), 'valor': datos_a_ordenar})
        
        # Ordenar utilizando el algoritmo seleccionado
        if algoritmo == 'quicksort':
            datos_ordenados = self.proceso.quicsort(df_aux.to_dict('records'), key=lambda x: x['valor'])
        elif algoritmo == 'mergesort':
            datos_ordenados = self.proceso.mergesort(df_aux.to_dict('records'), key=lambda x: x['valor'])
        else:
            raise ValueError("Algoritmo de ordenamiento no reconocido")
        
        # Obtener los índices ordenados
        indices_ordenados = [item['indice'] for item in datos_ordenados]
        
        # Reordenar el DataFrame basado en los índices ordenados
        df_ordenado = self.df.iloc[indices_ordenados].reset_index(drop=True)
        
        return df_ordenado












    '''
        indices_ordenados = sorted(range(len(datos_a_ordenar)), key=lambda k:  datos_ordenados [k])
        # Reordenar el DataFrame según los índices obtenidos
        df_ordenado = self.df.iloc[indices_ordenados].reset_index(drop=True)
        return df_ordenado
    '''
        
     
    '''     
    def ordenar_quicksort(self, variable):
        sorted_df = self.df.sort_values(by=variable, kind='quicksort')
        return sorted_df

    def ordenar_mergesort(self, variable):
        sorted_df = self.df.sort_values(by=variable, kind='mergesort')
        return sorted_df
    '''
    