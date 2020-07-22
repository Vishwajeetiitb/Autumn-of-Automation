class Complex():
	"""docstring for Complex"""
	def __init__(self,m,n):
		super(Complex, self).__init__()
		self.m = m
		self.n = n
	def display(self):
		sign = " + "
		if self.n <0:
			sign = " - "
		print(str(self.m)+ sign +str(abs(self.n))+"i")	
	def add(self,b):
		m1 = self.m
		n1 = self.n
		m2 = b.m
		n2 = b.n
		return(Complex(m1+m2,n1+n2))
	def conjugate(self):
		return(Complex(self.m,-self.n))


	

a = Complex(1,2)
a .display()
b = Complex(2,-3)
c = b.add(a)
c.display()
c.conjugate().display() 