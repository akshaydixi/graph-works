from graph import Graph
from digraph import Digraph
from depthFirstPaths import DepthFirstPaths
from breadthFirstPaths import BreadthFirstPaths
from cc import CC
from scc import SCC
g = Digraph('anotherTest.txt')
g.show()
"""
print 'Degree of vertices'
for x in range(1,g.vertices()+1):
    print x,'->',len(g.adj(x))

print 'DFS'
d = DepthFirstPaths(g,1)
for i in range(1,g.vertices()+1):
	print i,'->',d.pathTo(i)

print 'BFS'
b = BreadthFirstPaths(g,1)
for i in range(1,g.vertices()+1):
    print i,'->',b.pathTo(i)
"""
print 'SCC'

scc = SCC(g)
for i in range(1,g.vertices()+1):
	print i,'->',scc.id[i]