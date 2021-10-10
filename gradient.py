import numpy as np
import matplotlib.pyplot as plt

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

size = 100
image = np.zeros((size, size, 3), dtype="uint8")
assert image.shape[0] == image.shape[1]

color1 = [255, 128, 0]
color2 = [0, 128, 255]

middle_color = [(color1[i] + color2[i])/2 for i in range(len(color1))]

r_diff = (color2[0] - color1[0]) / (image.shape[0] * 2)
g_diff = (color2[1] - color1[1]) / (image.shape[0] * 2)
b_diff = (color2[2] - color1[2]) / (image.shape[0] * 2)

for i, v in enumerate(np.linspace(0, 1, image.shape[0])):
    for j in range(image.shape[1]):
        r = lerp(color1[0] + (r_diff * j), middle_color[0] + (r_diff * j), v)
        g = lerp(color1[1] + (g_diff * j), middle_color[1] + (g_diff * j), v)
        b = lerp(color1[2] + (b_diff * j), middle_color[2] + (b_diff * j), v)
        image[i, j, :] = [r, g, b]

plt.figure(1)
plt.imshow(image)
plt.show()