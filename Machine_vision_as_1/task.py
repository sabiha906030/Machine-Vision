import cv2
import matplotlib.pyplot as plt

img = cv2.imread("colourimage/colorful-pictures-image-hd.jpg")

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

channels = cv2.split(img)

fig, grid = plt.subplots(2, 2, figsize=(9, 9))

grid[0, 0].imshow(rgb)
grid[0, 0].set_title("Original RGB – Sabiha binte Nizam")
grid[0, 0].axis("off")

grid[0, 1].imshow(channels[2], cmap="gray")
grid[0, 1].set_title("Red Channel")
grid[0, 1].axis("off")

grid[1, 0].imshow(channels[1], cmap="gray")
grid[1, 0].set_title("Green Channel")
grid[1, 0].axis("off")

grid[1, 1].imshow(channels[0], cmap="gray")
grid[1, 1].set_title("Blue Channel")
grid[1, 1].axis("off")

plt.tight_layout()
plt.savefig("task-a-result.png")
plt.show()
