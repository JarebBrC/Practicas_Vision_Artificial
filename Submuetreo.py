import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#Segmentacion asada en regiones
img_RGB = cv.imread("lena_color.jpg")
img= cv.cvtColor(img_RGB,cv.COLOR_BGR2GRAY)
#Inicializa en ceros
img_seg = np.zeros_like(img,dtype=np.uint8)
#Definir semilla
seed_x, seed_y = 256,256
T=150 #Umbral
#Valor de intensidad de la semilla
seed_value = img[(seed_x,seed_y)]
#Crear ina lista ara almacenar los pixeles
list_pix =[(seed_x,seed_y)]
while(len(list_pix)>0):
    x,y = list_pix.pop()#Extraemos el pixel de la lista

#Condiciones
# si el pixel aun no ha sido procesado y se 
# cumple la condicion de similitud se marca el pixel
# con el valor 255 que es parte de la region
    if img_seg[x,y] == 0 and abs(int(img[x,y])-int(seed_value))<=T:
        img_seg[x,y]=255
        #arriba
        if x>0:
            list_pix.append((x-1,y))
        #abajo  
        if x<img.shape[0]-1:
            list_pix.append((x+1,y))
        #Derecha
        if y<img.shape[1]-1:
            list_pix.append((x,y+1))
        #izquierda
        if y<0:
            list_pix.append((x,y+1)) 

fig,axes = plt.subplots(1,2,figsize=(15,5))
axes[0].imshow(img)
axes[0].set_title("Imagen original")
axes[0].axis("off")

axes[1].imshow(img_seg)
axes[1].set_title("Imagen segmentada")
axes[1].axis("off")

plt.show()