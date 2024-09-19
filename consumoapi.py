import requests
#consumo la api y miro si quedo bien
def obteApi():
   return  'https://www.datos.gov.co/resource/fs93-tx8v.json'

def consumo(url, timeout=10):
    response = requests.get(url, timeout=timeout) #el timeout es para ...
    if response.status_code == 200:
        #print("consumiendo correctamente")
        data = response.json()
        #print("Datos obtenidos:", data[:5])
        return data
    else:
        print("error al consumir la api")
        return None

#correcto        