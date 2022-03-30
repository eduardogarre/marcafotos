# MarcaFotos

Script para añadir automáticamente una marca de agua a un conjunto de imágenes.

## Dependencias

He escrito `marcafotos` usando la versión 3 de `python`, empleando las bibliotecas `matplotlib` y `pillow`.

Puedes instalar `python` siguiendo las instrucciones de la página ofical del proyecto, [Python.org](https://www.python.org).

Instala las dependencias `matplotlib` y `pillow` ejecutando el siguiente comando en tu terminal:
```
pip install matplotlib pillow
```

## Uso

Ejecuta el siguiente comando en tu terminal:
```
python ./marcafotos.py
```

## Funcionamiento

El script espera encontrar en su misma carpeta lo siguiente:

- `marca.png`: imagen con la marca de agua.
- `fotos_originales`: subcarpeta con todas las fotos pendientes de marcar.

Durante su ejecución, el script recorrerá todos los archivos dentro de `fotos_originales`, y en el caso de que sean imágenes correctas las marcará y las guardará en una nueva carpeta, llamada `fotos_marcadas`.

Una vez el script se haya ejecutado con éxito, encontrarás todas las imágenes marcadas dentro de una nueva carpeta:

- `fotos_marcadas`: contiene todas las imágenes marcadas. Si la carpeta ya existía, será borrada completamente y recreada desde cero.
