from graph import Graph
from depthFirstPaths import DepthFirstPaths
from breadthFirstPaths import BreadthFirstPaths
from cc import CC
g = Graph('anotherTest.txt')
g.show()
print g.vertices()
"""
print 'Degree of vertices'
for x in range(1,g.vertices()+1):
    print x,'->',len(g.adj(x))
"""
print 'DFS'
d = DepthFirstPaths(g,1)
for i in range(1,g.vertices()+1):
	print i,'->',d.pathTo(i)

print 'BFS'
b = BreadthFirstPaths(g,1)
for i in range(1,g.vertices()+1):
    print i,'->',b.pathTo(i)

print 'CC'
cc = CC(g)
for i in range(1,g.vertices()+1):
	print i,'->',cc.id(i)