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

Para que la herramienta funcione correctamente, el script `marcafotos.py` debe estar en la misma carpeta que otros 2 archivos:

- `marca.png`, imagen de la marca de agua.
- `imagen.png`, imagen que modificar.
