# Video blanco y negro

Este programa usa la cámara del computador y muestra el video en blanco y negro.

Primero convierte la imagen a escala de grises y después usamos un umbral para decidir si cada pixel es negro o blanco.

Se puede elegir la cámara con `--camid` y también cambiar el valor del umbral con `--umbral`.

Por defecto usamos:

- camara 0
- umbral 127

Ejemplo:

```bash
python video_blanco_negro.py --camid=0 --umbral=127
