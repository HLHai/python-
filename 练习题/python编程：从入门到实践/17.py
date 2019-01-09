class Fish(object):
	def __init__(self):
		print "I am fish"

class FlyFish(Fish):
	def __init__(self):
		super(FlyFish,self).__init__()
		print "I also am FlyFish"

FlyFish()
