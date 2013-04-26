from graph import Graph
from depthFirstPaths import DepthFirstPaths
g = Graph('test.txt')
g.show()
print g.vertices()
print 'Degree of vertices'
for x in range(1,g.vertices()+1):
    print x,'->',len(g.adj(x))
d = DepthFirstPaths(g,1)
print 'DFS'
for i in range(1,g.vertices()+1):
    print i,'->',d.pathTo(i)
