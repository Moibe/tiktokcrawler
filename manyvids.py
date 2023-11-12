import time
#from webdrivers import createDriver
import csv 

from selenium.webdriver.common.by import By    
from selenium.common.exceptions import NoSuchElementException

#Función adicional para checar si existe xpath. 
def check_exists_by_xpath(xpath, driver):
    try:
       driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
            return False
    return True


def ManyVids(navegador, **kwargs):

    #Establecer valores predeterminados.
    #variable = kwargs.get('la variable que buscará', 'el default que usará de no encontrarla')
    servicio = kwargs.get('servicio', 'signIn')
    #navegador = kwargs.get('navegador', 'hola')
        
    def signIn(): 
        
        xpath_trans = "/html/body/div[1]/div/div/main/div/div/div[4]/div/img"
        url = 'https://manyvids.com/'
        navegador.get(url)              
        navegador.maximize_window()
       
        print("Área de trabajo lista.")
        time.sleep(1)

        if check_exists_by_xpath(xpath_trans, navegador) is True:
                        #Hacemos click en el botón de acepto.
                        seleccion = navegador.find_element(By.XPATH, xpath_trans)
                        seleccion.click()
                        print("Botón Siguiente encontrado y botón clickeado...")
                        
        else:
                print("El elemento 'Siguiente' no existe.")

        time.sleep(1)

        xpath_botonSignIn = "/html/body/div[1]/header/div/div[3]/div[1]/button[2]"

        if check_exists_by_xpath(xpath_botonSignIn, navegador) is True:
                        #Hacemos click en el botón de acepto.
                        boton = navegador.find_element(By.XPATH, xpath_botonSignIn)
                        boton.click()
                        print("Botón SignIn encontrado y botón clickeado...")
                        
        else:
                print("El elemento 'BotonSignIn' no existe.")

        time.sleep(2)
        
        print("Buscando campo de username...")
        navegador.find_element(By.ID, "triggerUsername").send_keys("Ruby_Stars")

        time.sleep(1)
        print("Buscando campo de password...")
        navegador.find_element(By.ID, "triggerPassword").send_keys("Qaonrr_182")

        time.sleep(1)

        navegador.find_element(By.ID, "loginAccountSubmit").click()
              
        print("Proceso finalizado.")
        time.sleep(1)

        return navegador
    
    def follow():
           #Esto va a repasar las 41  páginas de creadores.
           for i in range(1, 42):

            url = "https://www.manyvids.com/MVTrans/?page=" + i
            print("La url que estamos repasando es:")
            print(url)
            navegador.get(url)
            time.sleep(1)

            #Crear archivo de csv
            with open("archivo.csv", "a", newline="") as archivo:

                #Crea un escritor CSV
                escritor = csv.writer(archivo, delimiter=",")
                    
                #Cantidad de creadores que despliega la página donde 1 es el inicial y 3 es n+1 del total que hay.
                for i in range(1, 3):
                    print(f"Estoy en el número {i}")
                    primera_parte = "/html/body/div[6]/div/div[3]/div[4]/div["
                    segunda_parte = "]/div/h4/a"
                    xpath_nombre = primera_parte + str(i) + segunda_parte

                            
                    print(xpath_nombre)

                    if check_exists_by_xpath(xpath_nombre, navegador) is True:
                                nombre = navegador.find_element(By.XPATH, xpath_nombre)
                                print("Imprimiendo elemento nombre")
                                print(nombre)
                                #Obtener Nombre
                                nombre_texto = nombre.text
                                print("El nombre es: ", nombre_texto)
                                #Obtener Link
                                link = nombre.get_attribute("href")
                                print(link)
                                escritor.writerow([nombre_texto, link])
                            
                                
                                #escritor.writerow(["Juan", 25, "Ingeniero"])
                                print("Línea de excel impresa...")
                                #Darle Click al Nombre
                                nombre.click()
                                time.sleep(2)
                                navegador.get("https://www.manyvids.com/MVTrans/")
                                time.sleep(3)
                    else:
                            print("El elemento 'nombre' no existe.")
                
                return True
    
    options = {
    'signIn': signIn,
    'follow': follow
    }

    selected_function = options.get(servicio, lambda: None)
    return selected_function()