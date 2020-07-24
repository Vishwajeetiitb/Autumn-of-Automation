import cv2
import matplotlib.pyplot as plt
img = cv2.imread("greyscale.jpg")
img = img[:,:,2]
camera = cv2.VideoCapture(0)
while True:
	ret,img = camera.read()
	edges = cv2.Canny(img,90,171)
	edges = 255 - edges
	cv2.imshow("pencil sketch",edges)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()