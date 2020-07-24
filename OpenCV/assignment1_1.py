import cv2 
img = cv2.imread("test_image.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale",img)
cv2.imwrite("greyscale.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()