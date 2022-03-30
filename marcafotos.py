# import all the libraries
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

tamaño_marca = (300, 100)
posición_marca = (100, 100)

# Abro foto
foto_original = Image.open("imagen.png")
foto = foto_original.convert("RGBA")

# Abro la marca
marca_original = Image.open("marca.png")
marca = marca_original.convert("RGBA")

# Cambio el tamaño de la marca
marca.thumbnail(tamaño_marca)

# Creo 2 máscara del tamaño de la foto
máscara1 = Image.new("RGBA", foto.size)
máscara2 = Image.new("RGBA", foto.size)

# Pego la marca sobre la primera máscara
máscara1.paste(marca, posición_marca)

# Construyo la máscara final, ajustando transparencia
máscara = Image.blend(máscara1, máscara2, 0.9)

# Pego la máscara sobre la foto
foto_final = Image.alpha_composite(foto, máscara)

# Muestro el resultado
plt.imshow(foto_final)
plt.show()