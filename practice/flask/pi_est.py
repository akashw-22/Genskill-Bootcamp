import random

def wallis(n = 10000):
	
	pi = 1
	
	for i in range(1,n+1):
		pi *= 4*i*i/(4*i*i-1)
	
	return pi*2
	
def montecarlo(n = 10000):
	
	c = 0
	
	for _ in range(n+1):
		x = random.random()
		y = random.random()
		
		if x*x + y*y < 1:
			c += 1
	return 4*c/n
