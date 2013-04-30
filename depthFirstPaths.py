from graph import Graph
from digraph import Digraph
class DepthFirstPaths:
	def __init__(self,g,s):
		self.marked = {}
		self.edgeTo = {}
		self.s = s
		for v in range(1,g.vertices()+1):
			self.marked[v]=False
			self.edgeTo[v]=-1
		self.dfs(g,s)

	def dfs(self,g,v):
		self.marked[v] = True
		for w in g.adj(v):
			if not self.marked[w]:
				self.dfs(g,w)
				self.edgeTo[w]= v

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
