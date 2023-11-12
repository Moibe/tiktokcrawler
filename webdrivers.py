from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
#from webdriver_manager.firefox import GeckoDriverManager
#from undetected_chromedriver import Chrome, ChromeOptions

def createDriver(**kwargs):
    #Establecer valores predeterminados.
    navigator = kwargs.get('navigator', 'chrome')
    headless = kwargs.get('headless', False)
    width = kwargs.get('width', 800)
    height = kwargs.get('height', 600)

    #Funciones para cada navegador
    def createChromiumWD():
        options = webdriver.ChromeOptions()
        options.add_argument('headless') if headless else None
        options.add_argument(f"--window-size={width},{height}")
        webDriver = webdriver.Chrome(options=options) 
        return webDriver
    
    def createUndetectedWD():
        #Lo uso con youtube para que no saque notificaciones.
        options = ChromeOptions()
        options.add_argument('headless') if headless else None
        #options.add_argument("--remote-debugging-port=9222")
        #options.add_experimental_option("detach", True)
        
        #Ésta es la opción para evitar las notificaciones de navegador.
        options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
        })

        webDriver = webdriver.Chrome(options=options) 
        webDriver.set_window_size(width,height)
        return webDriver

    def createFirefoxWD():
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless') if headless else None
        options.add_argument(f"--width={width}")  
        options.add_argument(f"--height={height}") 
        webDriver = webdriver.Firefox(options=options)
        return webDriver

    def createGeckoWD():
        #Revisar, porque después de marcar varios errores, finalmente lo abre.
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless') if headless else None
        options.add_argument(f"--width={width}")  
        options.add_argument(f"--height={height}") 
        
        #webDriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        #return webDriver
 
    options = {
        'chrome': createChromiumWD,
        'undetected': createUndetectedWD,
        'firefox': createFirefoxWD,
        'gecko': createGeckoWD,        
    }

    selected_function = options.get(navigator, lambda: None)
    return selected_function()