from digraph import Digraph
from depthFirstPaths import DepthFirstPaths
class SCC:
	def __init__(self,g):
		self.marked = {}
		self.id = {}
		self.count = 0
		self.dfp = DepthFirstPaths(g.reverse())
		for v in self.dfp.reversePost():
			if  not self.marked[v]:
				self.dfs(g,v)
				self.count+=1

	def dfs(self,g,v):
		self.marked[v] = True
		self.id[v] = self.count
		for w in g.adj(v):
			if not self.marked[w]:
				self.dfs(g,v)

	def stronglyConnected(self,v,w):
		return self.id[v] == self.id[w]