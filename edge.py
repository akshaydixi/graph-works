class Edge:
	def __init__(self,v,w,weight):
		self.v = v
		self.w = w
		self.weight = weight

	def either(self):
		return self.v

	def other(self,v):
		if v == self.v:
			return self.w
		else:
			return self.v

	def compareTo(self,otherEdge):
		if self.weight < otherEdge.weight:
			return -1
		elif self.weight > otherEdge.weight:
			return +1
		else:
			return 0
