# MarcaFotos

Script para añadir automáticamente una marca de agua a un conjunto de imágenes.

## Dependencias

He escrito `marcafotos` usando `Python 3.10`, empleando las bibliotecas `matplotlib` y `pillow`.

Instala `Python` siguiendo las instrucciones de la página ofical del proyecto, [Python.org](https://www.python.org).

Instala las dependencias `matplotlib` y `pillow` ejecutando el siguiente comando en tu terminal:

```sh
pip install matplotlib pillow
```

## Instalación y preparativos

1) Descarga el archivo `marcafotos.py` de este repositorio, y guárdalo en una carpeta de tu sistema.
2) En la misma carpeta deberás colocar una foto con la marca de agua, con el nombre `marca.png`.
3) Por último crea también una subcarpeta vacía llamada `fotos_originales`, donde debes colocar todas las fotos que hay que marcar.

## Uso

Abre el terminal de tu sistema y navega hasta la carpeta donde hayas colocado `marcafotos.py`.
Ejecuta el siguiente comando en tu terminal:

```sh
python marcafotos.py
```

Este es el manual completo de uso para el terminal:

```sh
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
```

## Funcionamiento

El script espera encontrar en su misma carpeta lo siguiente:

- `marca.png`: imagen con la marca de agua.
- `fotos_originales`: subcarpeta con todas las fotos pendientes de marcar.

Durante su ejecución, el script recorrerá todos los archivos dentro de `fotos_originales`, y en el caso de que sean imágenes correctas las marcará y las guardará en una nueva carpeta, llamada `fotos_marcadas`.

Una vez el script se haya ejecutado con éxito, encontrarás todas las imágenes marcadas dentro de una nueva carpeta:

- `fotos_marcadas`: contiene todas las imágenes marcadas. Si la carpeta ya existía, será borrada completamente y recreada desde cero.

## Licencia

Proyecto publicado bajo la licencia de software libre `MIT`. Más información en el archivo `LICENSE` de este repositorio.
