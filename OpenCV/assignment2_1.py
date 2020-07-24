import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("t_shape.png")
rows,coloums,channels = img.shape
M1 = np.float32([[1,0,50],[0,1,50]])
trans1 = cv2.warpAffine(img,M1,(coloums,rows))
M2 = np.float32([[1,0,0],[0,1,100]])
trans2 = cv2.warpAffine(img,M2,(coloums,rows))
M3 = np.float32([[1,0,50],[0,1,-50]])
trans3 = cv2.warpAffine(img,M3,(coloums,rows))
M4 = np.float32([[1,0,-50],[0,1,-50]])
trans4 = cv2.warpAffine(img,M4,(coloums,rows))


M5 = cv2.getRotationMatrix2D((coloums/2,rows/2),45,1)
rot1 = cv2.warpAffine(img,M5,(coloums,rows))
M6 = cv2.getRotationMatrix2D((coloums/2,rows/2),90,1)
rot2 = cv2.warpAffine(img,M6,(coloums,rows))
M7 = cv2.getRotationMatrix2D((coloums/2,rows/2),180,1)
rot3 = cv2.warpAffine(img,M7,(coloums,rows))
M8 = cv2.getRotationMatrix2D((coloums/2,rows/2),135,1)
rot4 = cv2.warpAffine(img,M8,(coloums,rows))


blur1 = cv2.blur(img,(3,3))
blur2 = cv2.GaussianBlur(img,(3,3),0)


fig, axs = plt.subplots(2, 5)
axs[0,0].imshow(cv2.cvtColor(trans1,cv2.COLOR_BGR2RGB))
axs[0,1].imshow(cv2.cvtColor(trans2,cv2.COLOR_BGR2RGB))
axs[0,2].imshow(cv2.cvtColor(trans3,cv2.COLOR_BGR2RGB))
axs[0,3].imshow(cv2.cvtColor(trans4,cv2.COLOR_BGR2RGB))
axs[0,4].imshow(cv2.cvtColor(rot1,cv2.COLOR_BGR2RGB))
axs[1,0].imshow(cv2.cvtColor(rot2,cv2.COLOR_BGR2RGB))
axs[1,1].imshow(cv2.cvtColor(rot3,cv2.COLOR_BGR2RGB))
axs[1,2].imshow(cv2.cvtColor(rot4,cv2.COLOR_BGR2RGB))
axs[1,3].imshow(cv2.cvtColor(blur1,cv2.COLOR_BGR2RGB))
axs[1,4].imshow(cv2.cvtColor(blur2,cv2.COLOR_BGR2RGB))
plt.show()