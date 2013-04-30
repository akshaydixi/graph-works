from digraph import Digraph
class DepthFirstOrder:
	def __init__(self,g):
		self.marked = {}
		self.reversepost = []
		for v in range(1,g.vertices()+1):
			self.marked[v]=False
		for v in range(1,g.vertices()+1):
			if not self.marked[v]:
				self.dfs(g,v)

	def dfs(self,g,v):
		self.marked[v] = True
		for w in g.adj(v):
			if not self.marked[w]:
				self.dfs(g,w)
		self.reversepost.append(v)
				
	def reversePost(self):
		return self.reversepost
