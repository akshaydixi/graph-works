from digraph import Digraph
from depthFirstOrder import DepthFirstOrder
class SCC:
	def __init__(self,g):
		self.marked = {}
		self.id = {}
		self.count = 0
		for v in range(1,g.vertices()+1):
			self.marked[v]=False
			self.id[v] = -1
		self.dfo = DepthFirstOrder(g.reverse())
		for v in self.dfo.reversePost():
			if  not self.marked[v]:
				self.dfs(g,v)
				self.count+=1

	def dfs(self,g,v):
		self.marked[v] = True
		self.id[v] = self.count
		for w in g.adj(v):
			if not self.marked[w]:
				self.dfs(g,w)

	def stronglyConnected(self,v,w):
		return self.id[v] == self.id[w]