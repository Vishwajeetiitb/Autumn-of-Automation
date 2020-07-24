import numpy as np
import cv2
img = cv2.imread("football.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ball_cascade = cv2.CascadeClassifier('ball.xml')
balls = ball_cascade.detectMultiScale(gray,1.1, 5, 8,(16,16))
# print(balls)
for ball in balls:
	print(ball)
	img = cv2.circle(img, (ball[0]+int(0.5*ball[2]),ball[1]+int(ball[3]*0.5)), 5, (0,255,0), 5) 


cv2.imshow("pencil sketch",img)	
cv2.waitKey(0)
cv2.destroyAllWindows()