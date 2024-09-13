import customtkinter as ctk
from tkinter import ttk
from consumoapi import consumo, obteApi
from customtkinter import CTkFont 
from algorde import DatProceso
from dataset import Dataset


# Configuración de la API y procesamiento inicial de los datos
#API_URL = 'https://www.datos.gov.co/resource/fs93-tx8v.json'
API_URL = obteApi()
datos = consumo(API_URL)
#df = pro_dats(datos)
processor_data = DatProceso()
df = processor_data.pro_dats(datos)
processor = Dataset(df)  
# Clase para la interfaz gráfica
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("api Dataset")
        self.geometry("800x500")

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("green")

        custom_font = CTkFont(family="Verdana", size=14)

        self.label_variable = ctk.CTkLabel(self, text="Seleccione una variable:", font=custom_font)
        self.label_variable.pack(pady=10)

        self.variable_selector = ctk.CTkComboBox(self, values=["cantidad", "id_municipio", "anio"], font=custom_font)
        self.variable_selector.pack(pady=10)

        self.label_algoritmo = ctk.CTkLabel(self, text="Seleccione un algoritmo de ordenamiento:", font=custom_font)
        self.label_algoritmo.pack(pady=10)

        self.algoritmo_selector = ctk.CTkComboBox(self, values=["quicksort", "mergesort"], font=custom_font)
        self.algoritmo_selector.pack(pady=10)

        self.boton_ordenar = ctk.CTkButton(self, text="Ordenar", command=self.ordenar_datos,
                                          font=custom_font, width=150, height=40)  # Ajusta el tamaño aquí
        self.boton_ordenar.pack(pady=20)

        # para mostrar los resultados
        self.tree = ttk.Treeview(self, columns=("anio", "id_municipio", "municipio", "subregion", "cantidad"), show="headings")
        self.tree.heading("anio", text="Año")
        self.tree.heading("id_municipio", text="ID Municipio")
        self.tree.heading("municipio", text="Municipio")
        self.tree.heading("subregion", text="Subregión")
        self.tree.heading("cantidad", text="Cantidad")
      
        self.style = ttk.Style()
        
        # Configuración del Treeview
        self.style.configure("Treeview",
                            background="#272626",  # Color de fondo
                            foreground="white",  # Color del texto
                            fieldbackground="#000000")  # Color del fondo de los campos

        self.style.configure("Treeview.Heading",
                            background ="black",  # Color de fondo del encabezado
                            foreground="#00FF80",
                            relief="flat")  # Color del texto del encabezado
        self.style.map("Treeview",
                       background=[('selected', '#00FF80')],  # Color de fondo cuando está seleccionado
                       foreground=[('selected', '#000000')])
        self.tree.pack(pady=10, fill="both", expand=True)
        
        self.mostrar_datos(df)



    def mostrar_datos(self, dataframe):
        # Limpiar el Treeview
        self.tree.delete(*self.tree.get_children())
     
        # Insertar los datos en el Treeview
        for _, row in dataframe.iterrows():
            self.tree.insert("", "end", values=list(row))

    def ordenar_datos(self):
        # Obtener los valores seleccionados por usuario
        variable = self.variable_selector.get()
        algoritmo = self.algoritmo_selector.get()

        # Ejecutar el ordenamiento según la selección
        try:
            df_ordenado = processor.ordenar_datos(variable, algoritmo)
            # Mostrar los primeros 5 resultados del DataFrame ordenado en la caja de texto
            self.mostrar_datos(df_ordenado) # Insertar los resultados
        except ValueError as e:
            print(f"Error: {str(e)}")