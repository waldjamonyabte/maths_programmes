import rasterio
import matplotlib.pyplot as plt

with rasterio.open("georefenced_raster.tif") as src:
    band = src.read(1)

plt.imshow(band, cmap="gray")
plt.title(" Demo raster")
plt.colorbar()
plt.show()