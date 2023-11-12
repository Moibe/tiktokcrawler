import time
from webdrivers import createDriver
from workspaces import Google, ManyVids


#Aquí llamas a otras funciones en otros py que realizen el trabajo.
#instagram(obtenerUsuarios)
#tiktok(obtenerusuarios)

#Google(servicio='busqueda', busqueda='Mexico')
#Google(servicio='busqueda', busqueda='Finlandia')
#ManyVids(servicio='signIn')

#Cre un navegador con las características que deseas.
navegador = createDriver(navigator='chrome', width=800, height=600, headless=False)

print("Haciendo SignIn")
ManyVids(navegador, servicio = 'signIn')

time.sleep(4)

print("Haciendo Test")
ManyVids(navegador, servicio = 'test')

