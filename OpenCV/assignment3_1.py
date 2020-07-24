import cv2
import matplotlib.pyplot as plt
img = cv2.imread("greyscale.jpg")
img = img[:,:,2]
edges = cv2.Canny(img,90,171)
edges = 255 - edges
cv2.imshow("pencil sketch",edges)	
cv2.waitKey(0)
cv2.destroyAllWindows()
