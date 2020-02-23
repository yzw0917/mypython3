from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("logo.png")
plt.imshow(img)
plt.show()
img_L = img.convert("L")
plt.imshow(img_L)
plt.show()
img_1 = img.convert("1")
plt.imshow(img_1)
plt.show()
