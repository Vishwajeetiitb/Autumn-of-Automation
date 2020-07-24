import cv2 
import numpy as np
img_original = cv2.imread("t_shape.png")
img = img_original
img[:,:,0] = img[:,:,0] + img[:,:,2] 
img[:,:,2] = np.zeros((img.shape[0],img.shape[1]))
print(img.shape)
cv2.imshow("converted",img)
cv2.imshow("original",img_original)
cv2.waitKey(0)
cv2.destroyAllWindows()