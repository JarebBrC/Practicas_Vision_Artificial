import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_RGB = cv.imread(r"C:\Users\Jareb\Documents\OpencvApp\Lena_color.jpg")
img_RGB = cv.cvtColor(img_RGB, cv.COLOR_BGR2RGB)

img_noise=img_RGB.copy()
prob = 0.5

pix_noise = int(prob*img_RGB.size)
filas,columnas = img_RGB.shape

for _ in range(pix_noise//2):
    i,j = np.random.randit(0,filas), np.random.randing
    img_noise[i,j] = 0

for _ in range(pix_noise//2):
    i,j = np.random.randit(0,filas), np.random.ra    
    img_noise[i,j] = 255

img_ext = np.pad(img_noise, pad_whit=1, mode ="reflect")

for i in range (filas):
    for j in range(columnas):
        #ventana de 3x3
        suma=0
        for x in range (3):
            for y in range(3):
                suma+=img_ext[i+x,j+y]
        img_filt[i,j]=     xx


filas,columnas = img_RGB.shape[0]//2, img_RGB.shape[1]//2
"""
filas
colunas
"""

#vecino 4 - almacenaren una lista las posiciones
vecino_4=[
    (filas-1,columnas),
    (filas+1,columnas),
    (filas,columnas+1),
    (filas,columnas-1),
    ]

vecino_8=[
    (filas-1,columnas-1),
    (filas-1,columnas+1),
    (filas+1,columnas-1),
    (filas+1,columnas+1),
    ]
img_color_R=img_RGB.copy()
img_color_R[filas,columnas]=[255,0,0] #Color rojo

#posicion i, j central
for i,j in vecino_4:
    img_color_R[i,j]=[255,0,0]

for i,j in vecino_8:
    img_color_R[i,j]=[0,0,255]
    
img_rec = img_color_R[filas-3:filas+3,columnas-3:columnas+3]

fig,axes = plt.subplots(1,2,figsize=(15,6))
axes[0].imshow(img_color_R)
axes[0].set_title("Imagen Original")
axes[0].axis("off")

axes[1].imshow(img_rec)
axes[1].set_title("Imagen Recortada")
axes[1].axis("off")

plt.show()