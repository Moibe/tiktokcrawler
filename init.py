import time
from webdrivers import createDriver
#from workspaces import Google
from manyvids import ManyVids


#Aquí llamas a otras funciones en otros py que realizen el trabajo.
#instagram(obtenerUsuarios)
#tiktok(obtenerusuarios)

#Google(servicio='busqueda', busqueda='Mexico')
#Google(servicio='busqueda', busqueda='Finlandia')
#ManyVids(servicio='signIn')

#Crea un navegador con las características que deseas.
navegador = createDriver(navigator='chrome', width=800, height=600, headless=False)

#Creo que para muchas funciones no se necesita hacer signIn!
#print("Haciendo SignIn")
#ManyVids(navegador, servicio = 'signIn')

time.sleep(1)

#Para ésto sirve hacerlo modularmente, podemos saltarnos procesos que ya hicimos. 
print("Listando creadores...")
ManyVids(navegador, servicio = 'listCreators')

#Y partir hacia otros caminos después del signIn.

