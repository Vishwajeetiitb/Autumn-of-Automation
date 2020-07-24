import numpy as np
import cv2
from time import sleep
# im = cv2.imread('test_circle.png')
im = cv2.imread('shapes.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,200,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# print(contours)
# im = cv2.drawContours(im, contours, -1, (0,255,0), 3)
i = 0
for cnt in contours:
	area = cv2.contourArea(cnt)
	if area > 10**3:
		episolon = 0.005*cv2.arcLength(cnt,True)
		poly = cv2.approxPolyDP(cnt,episolon,True)
		print(len(poly))
		im = cv2.drawContours(im, [poly],0, (0,255,0), 3)
		# print(poly.shape)
		if len(poly)==3:
			M = cv2.moments(cnt)

			x = int(M['m10']/M['m00'])
			y = int(M['m01']/M['m00'])
			cv2.putText(im,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0))
		if len(poly)==4:
		
			M = cv2.moments(poly)
			x = int(M['m10']/M['m00'])
			y = int(M['m01']/M['m00'])
			x1 = poly.ravel()[0]
			y1 = poly.ravel()[1]
			x2 = poly.ravel()[2]
			y2 = poly.ravel()[3]
			x3 = poly.ravel()[4]
			y3 = poly.ravel()[5]
			x4 = poly.ravel()[6]
			y4 = poly.ravel()[7]
			d1 = ((x1-x2)**2 + (y1-y2)**2)**0.5
			d2 = ((x3-x2)**2 + (y3-y2)**2)**0.5
			d3 = ((x4-x2)**2 + (y4-y2)**2)**0.5
			
			if abs(d1 - d2) < 2:
				if abs(d3 - (d1**2 + d2**2)**0.5) < 2:
					cv2.putText(im,"Square",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0))
				else:
					cv2.putText(im,"Rhombus",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0))

			else:
				cv2.putText(im,"Rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0))


		if len(poly) > 10:
			M = cv2.moments(cnt)
			x = int(M['m10']/M['m00'])
			y = int(M['m01']/M['m00'])
			x1 = poly.ravel()[0]
			y1 = poly.ravel()[1]
			x2 = poly.ravel()[2]
			y2 = poly.ravel()[3]
			d1 = ((x1-x)**2+(y1-y)**2)**0.5
			d2 = ((x2-x)**2+(y2-y)**2)**0.5
			if(abs(d1-d2) <1 ):
				cv2.putText(im,"Circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0))
			else:
				cv2.putText(im,"Oval",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0))



			# cv2.putText(im,"Rectangle"+ str(i),(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0))
			# i+=1


cv2.imshow("test",im)
cv2.waitKey(0)
cv2.destroyAllWindows()