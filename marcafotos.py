# import all the libraries
from PIL import Image
import matplotlib.pyplot as plt
import os
import shutil

nombre_archivo_marca = "marca.png"

def construyemáscara(tamaño, transparencia):

    tamaño_marca = (150, 150)
    posición_marca = (100, 100)

    # Abro la marca
    try:
        marca_original = Image.open(nombre_archivo_marca)
    except:
        print("ERROR: La marca '" + nombre_archivo_marca + "' no es una imagen válida")
        return

    marca = marca_original.convert("RGBA")

    # Cambio el tamaño de la marca
    marca.thumbnail(tamaño_marca)

    # Creo 2 máscara del tamaño de la foto
    máscara1 = Image.new("RGBA", tamaño)
    máscara2 = Image.new("RGBA", tamaño)

    # Pego la marca sobre la primera máscara
    máscara1.paste(marca, posición_marca)

    # Construyo la máscara final, ajustando transparencia
    máscara = Image.blend(máscara1, máscara2, transparencia)

    return máscara

def marcafoto(nombre_archivo_foto, nombre_archivo_destino):

    # Abro foto
    try:
        foto_original = Image.open(nombre_archivo_foto)
    except:
        print("ERROR: '" + nombre_archivo_foto + "' no es una foto válida")
        return

    foto = foto_original.convert("RGBA")
    
    # Construyo la máscara final, ajustando transparencia
    máscara = construyemáscara(foto.size, 0.25)

    # Pego la máscara sobre la foto
    foto_marcada = Image.alpha_composite(foto, máscara)

    # Muestro el resultado
    plt.imshow(foto_marcada)
    plt.show()

    # Para poder guardar la imagen, tengo que quitar el canal Alfa
    foto_final = foto_marcada.convert("RGB")
    foto_final.save(nombre_archivo_destino)

def recorrecarpeta():
    carpeta_origen = "fotos_originales"
    carpeta_marcas = "fotos_marcadas"

    # Compruebo que dispongo de la imagen con la marca de agua
    try:
        Image.open(nombre_archivo_marca)
    except:
        print("ERROR: No encuentro la imagen con la marca de agua")
        print("Para usar correctamente este programa, pon una imagen llamada 'marca.png' con la marca de agua que prefieras")
        return

    # Abro la carpeta de origen y leo su lista de archivos
    try:
        listaarchivos = os.listdir(carpeta_origen)
    except FileNotFoundError:
        print("ERROR: No encuentro la carpeta './" + carpeta_origen + "'")
        print("Para usar correctamente este programa, pon todas las imágenes originales dentro de una carpeta llamada 'fotos_originales'")
        return

    # Borro la carpeta de destino, si es que existía
    try:
        shutil.rmtree(carpeta_marcas)
        print("INFO: He tenido que borrar './" + carpeta_marcas + "' porque ya existía")
    except FileNotFoundError:
        a = 42
        #print("No he tenido que borrar ./" + carpeta_marcas)
    except:
        print("ERROR: Fallo inesperado al intentar borrar la carpeta './" + carpeta_marcas + "' previa")
        return

    # Creo la nueva carpeta de destino, ./fotos_marcadas, vacía
    try:
        os.mkdir(carpeta_marcas)
    except:
        print("ERROR: No he podido crear una nueva carpeta './" + carpeta_marcas + "' vacía, para guardar las fotos marcadas")
        return

    # Recorro la lista de archivos
    for nombrearchivo in listaarchivos:
        # Construyo la ruta relativa de los archivos original y marcado
        archivo_original = os.path.join(carpeta_origen, nombrearchivo)
        archivo_marcado = os.path.join(carpeta_marcas, nombrearchivo)
        # Compruebo que el archivo original es realmente un archivo, y no una subcarpeta
        if os.path.isfile(archivo_original):
            marcafoto(archivo_original, archivo_marcado)

if __name__ == "__main__":
    recorrecarpeta()