### ART GALLERY PROBLEM ###
### SOLUTION VIA GRAPH COLORING ###
### BY: OWEN FOSTER ####

# Class definition for a gallery
# this will hold relevant functions for adding edges and calculating coloring
class gallery:
    # Initialize the class: we need the graph list, the color list, and the number of vertices
    def __init__(self, n):
        self.graph = [[] for i in range(n)]
        self.num_v = n

    # add edge function, input 2 vertex numbers
    # add the edge to vertex one's connections
    # add it to vertex two's connections as well
    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    # determine graph coloring
    def color(self):
        # first, define "result" list, this holds the resultant color for
        # each vertex. Set every vertex to -1 so we know it hasn't been
        # colored yet. Vertex 0 is 0 because we start with a set color
        result = [-1] * self.num_v
        result[0] = 0

        # in order to properly iterate through the graph, we need to keep
        # track of which vertices we've visited
        visited = [False] * self.num_v

        # process through the graph
        for i in range(1,self.num_v):
            # process through each connection in a vertex
            for j in self.graph[i]:
                if (result[j] != -1):
                    # if uncolored, we have now visited it
                    visited[result[j]] = True
            
            color = 0 # first color is 0
            while color < self.num_v: # note, number of colors cannot exceed number of vertices
                if (visited[color] == False):
                    break
                color += 1 # increment color upon finding an uncolored vertex

            result[i] = color # set uncolored vertex to new color

            # reset visited list for the next vertex
            for j in self.graph[i]:
                if (result[j] != -1):
                    visited[result[j]] = False

        # print results for the coloring
        for i in range(self.num_v):
            print(str(i), ": ", result[i])



####################### version 2, not functional, really bad
def valid(graph, color, c, v):
    for i in range(0,len(graph)):
        if color[i] == c:
            return False
    return True
        
def colorv2(graph, color, m, v, V):
    if v == V:
        print(color)
        return
    for i in range(1,m):
        if valid(graph, color, i, v):
            color[v] = i
            colorv2(graph, color, m, v+1, V)
            color[v] = 0;

def add_edge(graph, a, b):
    graph[a].append(b)
    graph[b].append(a)


