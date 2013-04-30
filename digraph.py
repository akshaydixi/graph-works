class Digraph:
	def __init__(self,V):
		self.adjacent={}
		self.E=0

		if str(type(V))[7:-2] == 'int':
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
				self.addEdge(v,w)

	def addEdge(self,v,w):
		self.adjacent[v].append(w);
		self.E+=1

	def adj(self,v):
		return self.adjacent[v]

	def show(self):
		for v in range(1,self.V+1):
			print v,':',self.adj(v)

	def vertices(self):
		return self.V

	def edges(self):
		return self.E

	def reverse(self):
		digraph = Digraph(self.V)
		digraph.E = self.E
		digraph.V = self.V
		for v in self.adjacent.keys():
			for w in self.adjacent[v]:
				digraph.adjacent[w].append(v)
		return digraph


