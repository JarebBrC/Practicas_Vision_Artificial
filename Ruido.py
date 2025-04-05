import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
img_RGB = cv.imread(r"C:\Users\Jareb\Documents\OpencvApp\Lena_color.jpg")

# Verificar si la imagen se cargó correctamente
if img_RGB is None:
    raise ValueError("No se pudo cargar la imagen. Verifica la ruta.")

# Convertir de BGR a RGB (OpenCV carga las imágenes en BGR por defecto)
img_RGB = cv.cvtColor(img_RGB, cv.COLOR_BGR2RGB)

# Crear una copia para agregar ruido
img_noise = img_RGB.copy()
prob = 0.05  # Probabilidad de ruido (ajustada)

filas, columnas, canales = img_RGB.shape

# Número de píxeles con ruido
pix_noise = int(prob * filas * columnas)    

# Agregar ruido sal y pimienta
for _ in range(pix_noise // 2):
    i, j = np.random.randint(0, filas), np.random.randint(0, columnas)
    img_noise[i, j] = [0, 0, 0]  # Negro (pimienta)

for _ in range(pix_noise // 2):
    i, j = np.random.randint(0, filas), np.random.randint(0, columnas)
    img_noise[i, j] = [255, 255, 255]  # Blanco (sal)

# Aplicar padding en cada canal
img_ext = np.pad(img_noise, pad_width=((1, 1), (1, 1), (0, 0)), mode="reflect")

# Crear la imagen filtrada
img_filt = np.zeros((filas, columnas, 3), dtype=np.uint8)

# Aplicar filtro de promedio (3x3)
for i in range(filas):
    for j in range(columnas):
        for c in range(3):  # Iterar sobre canales R, G, B
            img_filt[i, j, c] = np.mean(img_ext[i:i+3, j:j+3, c])

# Mostrar resultados
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].imshow(img_RGB)
ax[0].set_title("Imagen Original")
ax[0].axis("off")

ax[1].imshow(img_noise)
ax[1].set_title("Imagen con Ruido")
ax[1].axis("off")

ax[2].imshow(img_filt)
ax[2].set_title("Imagen Filtrada")
ax[2].axis("off")

plt.show()
