from graph import Graph
class CC:
	def __init__(self,g):
		self.marked = {}
		self.gid = {}
		self.gcount = 0
		for i in range(1,g.vertices()+1):
			self.marked[i] = False
			self.gid[i] = 0
		for v in range(1,g.vertices()+1):
			if not self.marked[v]:
				self.dfs(g,v)
				self.gcount+=1

	def count(self):
		return self.gcount

	def id(self,v):
		return self.gid[v]

	def dfs(self,g,v):
		self.marked[v] = True
		self.gid[v] = self.gcount
		for w in g.adj(v):
			if not self.marked[w]:
				self.dfs(g,w)
