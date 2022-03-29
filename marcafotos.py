# import all the libraries
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

tamaño_marca = (500, 100)
posición_marca = (100, 100)

# Abro foto
foto_original = Image.open("imagen.png")
foto = foto_original.convert("RGBA")

# Abro la marca
marca_original = Image.open("marca.png")
marca = marca_original.convert("RGBA")

# Cambio el tamaño de la marca
marca.thumbnail(tamaño_marca)

# Creo una máscara del tamaño de la foto
máscara = Image.new("RGBA", foto.size)

# Pego la marca sobre la máscara
máscara.paste(marca, posición_marca)

# Pego la máscara sobre la foto
foto_final = Image.alpha_composite(foto, máscara)

# Muestro el resultado
plt.imshow(foto_final)
plt.show()