from edge import Edge
class EdgeWeightedGraph:
	def __init__(self,V):
		self.adjacent = {}
		self.E = 0

		V))[7:-2] == 'int':
			self.V = V
			for v in range(1,V+1):
				self.adjacent[v]=[]


		if str(type(V))[7:-2] == 'str':
			inp = file(V,'r')
			lines = inp.readlines()
			x = eval(lines[0].strip())
			self.V = x
			for v in range(1,x+1):
				self.adjacent[v]=[]
			for line in lines[1:]:
				self.E+=1
				line = line.strip().split()
				v = eval(line[0])
				w = eval(line[1])
				weight = eval(line[2])
				edge = Edge(v,w,weight)
				self.addEdge(edge)

	def addEdge(self,e):
		v = e.either()
		w = e.other(v)
		self.adjacent[v].append(e)
		self.adjacent[w].append(e)

	def adj(self,v):
		return self.adjacent[v]