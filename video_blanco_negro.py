# Visión Computacional : 696014 : Cristina Ceccoli
"""
Captura video desde una cámara y convierte cada frame a blanco y negro.
Primero convierte la imagen a escala de grises y después aplica un umbral (threshold) para clasificar cada píxel como negro o blanco.

Usage:
    video_blanco_negro.py [--camid=N] [--umbral=U]

Options:
    -c --camid=N      Número de la cámara [default: 0]
    -u --umbral=U     Valor de umbral para convertir la imagen a blanco y negro [default: 127]
"""

from docopt import docopt
import cv2

# Captura y procesa video desde una cámara en tiempo real
def main(cam_id, umbral):

    # Verificar que el valor del umbral esté entre 0 y 255
    if umbral < 0 or umbral > 255:
        print("Error: el umbral debe estar entre 0 y 255.")
        return 1

    # Abrir la cámara seleccionada
    cap = cv2.VideoCapture(cam_id)

    if not cap.isOpened():
        print(f"Error: no se pudo acceder a la cámara {cam_id}.")
        return 1

    print(f"Cámara seleccionada: {cam_id}")
    print(f"Umbral seleccionado: {umbral}")
    print("Presiona 'q' para salir.")

    while True:
        # Capturar un nuevo frame de la cámara
        ret, frame = cap.read()

        if not ret:
            print("Error: no se pudo leer el frame de la cámara.")
            break

        # Convertir el frame a escala de grises
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Crear una copia de la imagen para guardar el resultado
        blanco_negro = gris.copy()

        # Obtener las dimensiones de la imagen
        alto, ancho = gris.shape

        # Convertir cada píxel a negro o blanco según el umbral
        for i in range(alto):
            for j in range(ancho):
                if gris[i, j] > umbral:
                    blanco_negro[i, j] = 255
                else:
                    blanco_negro[i, j] = 0

        # Mostrar el video original
        cv2.imshow("Webcam original", frame)

        # Mostrar el video en blanco y negro
        cv2.imshow("Webcam blanco y negro", blanco_negro)

        # Salir con 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    return 0


if __name__ == "__main__":
    args = docopt(__doc__)
    cam_id = int(args["--camid"])
    umbral = int(args["--umbral"])

    main(cam_id, umbral)