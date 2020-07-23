import numpy as np

def CalculateTheta(x,y):
	return np.multiply(np.linalg.inv(np.multiply(x,np.transpose(x))),np.multiply(np.transpose(x),y))

x = np.random.normal(size=(20, 20))
y = np.random.randint(low=-2147483647, high=2147483647,dtype=np.int32,size=20)
ans = CalculateTheta(x,y)
print(ans)