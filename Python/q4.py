import numpy as np

def CalculateTheta(x,y):
	return np.multiply(np.linalg.inv(np.multiply(x,np.transpose(x))),np.multiply(np.transpose(x),y))

x = np.random.normal(size=(20, 20))
y =  np.random.normal(size=(1,10))
print(y)
y.dtype = 'int16'
print(y.shape)
# ans = CalculateTheta(x,y)
print(y)