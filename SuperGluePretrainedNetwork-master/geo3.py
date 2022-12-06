
import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt
import cv2
tiff_path = "remote.tif"
def scale_percentile(matrix):
    w, h, d = matrix.shape
    matrix = np.reshape(matrix, [w * h, d]).astype(np.float64)

    mins = np.percentile(matrix, 1, axis=0)
    maxs = np.percentile(matrix, 99, axis=0) - mins
    matrix = (matrix - mins[None, :]) / maxs[None, :]
    matrix = np.reshape(matrix, [w, h, d])
    matrix = matrix.clip(0, 1)
    return matrix
img = tiff.imread(tiff_path)
plt.imshow(scale_percentile(img[:, :, :3]))
plt.show()