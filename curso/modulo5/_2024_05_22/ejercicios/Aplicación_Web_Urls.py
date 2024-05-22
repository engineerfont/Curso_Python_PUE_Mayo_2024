# Definir una aplicación en Python que dada una determinada dirección web o url
# se pueda extraer la siguiente información:

# Para la extracción de los enlaces dentro del documento HTML es obligatorio
# el uso de recursividad.

# - El documento HTML de la dirección web o url
# - Todas las 'urls' que se encuentren en la etiqueta '<a>'
#   <a href='https://www.pue.es'>PUE</a>
# - Todas las 'urls' que se encuentren en la etiqueta '<img>'
#   <img src='https://www.pue.es/resources/images/logos/logo-pue-white.png' />
# - Todas las 'urls' que se encuentren en la etiqueta '<link>'
#   <link rel="stylesheet" href="https://www.pue.es/css/menu.css">
# - Todas las 'urls' que se encuentren en la etiqueta '<video>'
#   <video src="/resources/videos/videofile.avi"></video>
# - Todas las 'urls' que se encuentren en la etiqueta '<audio>'
#   <audio src="/resources/videos/audio.mp3"></video>

# Parte 2 de la aplicación
# Agregar una nueva función que permita guardar los enlaces en un archivo, por tipo de
# enlaces o todos los enlaces encontrados
