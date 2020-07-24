import cv2
import matplotlib.pyplot as plt
camera = cv2.VideoCapture(0)
while True:
	ret,img = camera.read()
	edges = cv2.Canny(img,90,171)
	edges = 255 - edges
	cv2.imshow("pencil sketch",edges)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
