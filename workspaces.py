import time
from webdrivers import createDriver

#Aquí se crean las áreas de trabajo, si son áreas muy usadas puedes concentrarlos en workspaces.py
#Pero si ya es algo muy personalizado, puedes usar su propio py. 

def Google(**kwargs):

    domain = 'https://google.com/'

    #Establecer valores predeterminados.
    #variable = kwargs.get('la variable que buscará', 'el default que usará de no encontrarla')
    servicio = kwargs.get('servicio', 'busqueda')
    #Esto se puede poner en la función que lo requiere si ya tuvieras muchos #kwargs aquí arriba.
    busqueda = kwargs.get('busqueda', 'Mexico')
    
    def Busqueda(): 
        
        param = '/search?q=' + busqueda
        url = domain + param

        #La creación del navegador con las características que deseas.
        #navigator: 'chrome', 'undetected', 'firefox', 'gecko' 
        #width, height con valores numéricos.
        #headless true or false.
        webDriver = createDriver(navigator='firefox', width=800, height=600, headless=False)

        #Aplicas tu url en ese navegador. 
        webDriver.get(url)
        print("Área de trabajo lista.")
        time.sleep(50)
        return True
    
    options = {
    'busqueda': Busqueda,
    }

    selected_function = options.get(servicio, lambda: None)
    return selected_function()