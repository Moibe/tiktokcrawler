import time
from webdrivers import createDriver

from selenium.webdriver.common.by import By    
from selenium.common.exceptions import NoSuchElementException

#Función adicional para checar si existe xpath. 
def check_exists_by_xpath(xpath, driver):
    try:
       driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
            return False
    return True

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
        webDriver.maximize_window()

        print("Área de trabajo lista.")
        time.sleep(50)
        return True
    
    options = {
    'busqueda': Busqueda,
    }

    selected_function = options.get(servicio, lambda: None)
    return selected_function()

def ManyVids(navegador, **kwargs):

    #Establecer valores predeterminados.
    #variable = kwargs.get('la variable que buscará', 'el default que usará de no encontrarla')
    servicio = kwargs.get('servicio', 'signIn')
    #navegador = kwargs.get('navegador', 'hola')
        
    def SignIn(): 
        
        xpath_trans = "/html/body/div[1]/div/div/main/div/div/div[4]/div/img"
        url = 'https://manyvids.com/'
        navegador.get(url)              
        navegador.maximize_window()
       
        print("Área de trabajo lista.")
        time.sleep(4)

        if check_exists_by_xpath(xpath_trans, navegador) is True:
                        #Hacemos click en el botón de acepto.
                        seleccion = navegador.find_element(By.XPATH, xpath_trans)
                        seleccion.click()
                        print("Botón Siguiente encontrado y botón clickeado...")
                        
        else:
                print("El elemento 'Siguiente' no existe.")

        time.sleep(3)

        xpath_botonSignIn = "/html/body/div[1]/header/div/div[3]/div[1]/button[2]"

        if check_exists_by_xpath(xpath_botonSignIn, navegador) is True:
                        #Hacemos click en el botón de acepto.
                        boton = navegador.find_element(By.XPATH, xpath_botonSignIn)
                        boton.click()
                        print("Botón SignIn encontrado y botón clickeado...")
                        
        else:
                print("El elemento 'BotonSignIn' no existe.")

        time.sleep(3)
        
        print("Buscando campo de username...")
        navegador.find_element(By.ID, "triggerUsername").send_keys("Ruby_Stars")

        time.sleep(2)

        print("Buscando campo de password...")
        navegador.find_element(By.ID, "triggerPassword").send_keys("Qaonrr_182")

        time.sleep(1)

        navegador.find_element(By.ID, "loginAccountSubmit").click()
              
        print("Proceso finalizado.")
        time.sleep(3)

        return navegador
    
    def test():
           print("Ésto es una prueba:")
           navegador.get("https://www.manyvids.com/MVTrans/")
           time.sleep(10)
           
           return True
    
    options = {
    'signIn': SignIn,
    'test': test
    }

    selected_function = options.get(servicio, lambda: None)
    return selected_function()