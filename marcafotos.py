#!/usr/bin/env python
from PIL import Image
import matplotlib.pyplot as plt
import os
import shutil
import sys

uso = """
Uso:
    python marcafotos.py [DISEÑO]

Opciones:
    DISEÑO  Opcional. Escoge el diseño con el que sobreimpresionar la marca de
            agua. Sustituye 'DISEÑO' por una palabra de entre las 3 siguientes:
            - alpie: Una marca abajo a la derecha.
            - alpie2: Una marca con texto azul abajo a la derecha.
            - centrado: Una marca grande y centrada.
            - diagonal: Múltiples hileras de marcas en diagonal.
            Si no se define ningún diseño, de forma predeterminada se escogerá
            el diseño 'diagonal'.

Ejemplos:
    python marcafotos.py
    python marcafotos.py alpie
    python marcafotos.py alpie2
    python marcafotos.py centrado
    python marcafotos.py diagonal
"""

diseño_marca = "diagonal"
nombre_archivo_marca = "marca.png"

def marcaalpie(tamaño, marca):
    # Obtengo tamaño máximo de la marca de agua
    tamaño_marca = (int(tamaño[0]/4), int(tamaño[1]/9))
    # Cambio el tamaño de la marca
    marca.thumbnail(tamaño_marca)
    # Calculo posición de la marca
    posición_marca = (int(tamaño[0] - marca.size[0]*1.33), int(tamaño[1] - marca.size[1]*1.75))
    # Creo máscara del tamaño de la foto
    máscara = Image.new("RGBA", tamaño)
    # Pego la marca sobre la primera máscara
    máscara.paste(marca, posición_marca)
    return máscara

def marcaalpie2(tamaño, marca):
    # Obtengo tamaño máximo de la marca de agua
    tamaño_marca = (int(tamaño[0]/2.5), int(tamaño[1]/9))
    # Cambio el tamaño de la marca
    marca.thumbnail(tamaño_marca)
    # Calculo posición de la marca
    posición_marca = (int(tamaño[0] - marca.size[0]*1.33), int(tamaño[1] - marca.size[1]*1.75))
    # Creo máscara del tamaño de la foto
    máscara = Image.new("RGBA", tamaño)
    # Pego la marca sobre la primera máscara
    máscara.paste(marca, posición_marca)
    return máscara

def marcasdiagonales(tamaño, marca):
    separación = 2.0
    # Obtengo tamaño máximo de la marca de agua
    tamaño_marca = (int(tamaño[0]/8), int(tamaño[1]/20))
    # Cambio el tamaño de la marca
    marca.thumbnail(tamaño_marca)
    # Creo máscara del tamaño de la foto
    máscara = Image.new("RGBA", tamaño)
    # Creo máscara intermedia, el doble del tamaño
    máscaratmp = Image.new("RGBA", (int(tamaño[0]*1.5), int(tamaño[1]*1.5)))

    for i in range(11):
        for j in range(11):
            # Calculo posición de la marca
            posición_marca = (int(tamaño[0]*(-0.125) + marca.size[0]*(separación+0.5)*j - marca.size[0]*separación*i), int(marca.size[0]*separación*i))
            # Pego la marca sobre la primera máscara
            máscaratmp.paste(marca, posición_marca)

    máscara45 = máscaratmp.rotate(45, expand=True)
    
    máscara.paste(máscara45, (int(-tamaño[1]/2), int(-tamaño[1]/1)))
    return máscara

def marcacentrada(tamaño, marca):
    # Obtengo tamaño máximo de la marca de agua
    tamaño_marca = (int(tamaño[0]*0.666), int(tamaño[1]*0.333))
    # Cambio el tamaño de la marca
    marca.thumbnail(tamaño_marca)
    # Calculo posición de la marca
    posición_marca = (int(tamaño[0]*0.5 - marca.size[0]*0.5), int(tamaño[1]*0.55 - marca.size[1]*0.5))
    # Creo máscara del tamaño de la foto
    máscara = Image.new("RGBA", tamaño)
    # Pego la marca sobre la primera máscara
    máscara.paste(marca, posición_marca)
    return máscara

def construyemáscara(tamaño):
    # Abro la marca
    try:
        marca_original = Image.open(nombre_archivo_marca)
    except:
        print("ERROR: La marca '" + nombre_archivo_marca + "' no es una imagen válida")
        return

    marca = marca_original.convert("RGBA")

    # Creo máscara del tamaño de la foto
    máscara1 = Image.new("RGBA", tamaño)
    transparencia = 0.6

    # Escojo qué tipo de máscara usar
    match diseño_marca:
        case "alpie":
            máscara2 = marcaalpie(tamaño, marca)
            transparencia = 0.5
        case "alpie2":
            máscara2 = marcaalpie2(tamaño, marca)
            transparencia = 1
        case "centrado":
            máscara2 = marcacentrada(tamaño, marca)
            transparencia = 0.25
        case "diagonal":
            máscara2 = marcasdiagonales(tamaño, marca)
            transparencia = 0.3666

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
    máscara = construyemáscara(foto.size)

    # Pego la máscara sobre la foto
    foto_marcada = Image.alpha_composite(foto, máscara)

    # Muestro el resultado
    #plt.imshow(foto_marcada)
    #plt.show()

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
        #print("INFO: He tenido que borrar './" + carpeta_marcas + "' porque ya existía")
    except FileNotFoundError:
        #print("No he tenido que borrar ./" + carpeta_marcas)
        pass
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
    if len(sys.argv) == 1:
        diseño_marca = "diagonal"
    elif len(sys.argv) == 2:
        match sys.argv[1]:
            case "alpie":
                diseño_marca = "alpie"
            case "alpie2":
                diseño_marca = "alpie2"
                nombre_archivo_marca = "marca2.png"
            case "centrado":
                diseño_marca = "centrado"
            case "diagonal":
                diseño_marca = "diagonal"
            case _:
                print("ERROR: No reconozco el diseño '" + sys.argv[1] + "'")
                print(uso)
                exit()
    else:
        print("ERROR: Intentas ejecutar el script con demasiados argumentos")
        print(uso)
        exit()
        
    recorrecarpeta()