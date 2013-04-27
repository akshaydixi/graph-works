from Queue import LifoQueue
from graph import Graph
class breadthFirstPaths:
	def __init__(self,g,s):
		queue = LifoQueue()
		self.marked = {}
		self.edgeTo = {}
		self.s = s
		for v in range(1,g.vertices()+1):
			self.marked[v]=False
			self.edgeTo[v]=-1
		self.marked[s] = True
		queue.put(s)
		while not queue.empty():
			v = queue.get()
			for w in g.adj(v):
				if not self.marked[w]:
					queue.put(w)
					self.marked[w] = True
					self.edgeTo[w] = v

	def hasPathTo(self,v):
		return self.marked[v]

	def pathTo(self,v):
		if not self.hasPathTo(v): return None
		path = []
		x = v
		while x != self.s :
			path.append(x)
			x=self.edgeTo[x]
		path.append(self.s)
		path.reverse()
		return path