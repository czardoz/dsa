'''
Created on Oct 17, 2012

@author: czardoz
'''

class Vertex:
    
    def __init__(self, label):
        self.label = label
        self.neighbours = []
        self.marked = 0
        
    def __str__(self):
        return str(self.label)
        
    def __repr__(self):
        return str(self.label) + "--->" + str(self.neighbours)

def get_input():
    f = open("undirected_connected")
    l = [map(int,line.split(' ')) for line in f]
    return l

def bfs(graph, v_index):
    queue = []
    queue.insert(0, graph[v_index])
    graph[v_index].marked = 1
    while len(queue) != 0:
        t = queue.pop()
        print t
        for o in t.neighbours:
            if graph[o].marked == 0:
                graph[o].marked = 1
                queue.insert(0, graph[o])
                
def dfs(graph, v_index):
    stack = []
    stack.append(graph[v_index])
    graph[v_index].marked = 1
    while len(stack) != 0:
        t = stack.pop()
        print t
        for o in t.neighbours:
            if graph[o].marked == 0:
                graph[o].marked = 1
                stack.append(graph[o])
    
def clear(graph):
    for v in graph:
        v.marked = 0
                
def main():
    admat = get_input()
    size = len(admat)
    graph = []
    for i in range(0, size):
        temp = Vertex(i)
        graph.append(temp)
    for i in range(0,size):
        for j in range(0,size):
            if admat[i][j] != 0:
                graph[i].neighbours.append(j)
    for vertex in graph:
        print vertex
    print "===============BFS================="
    bfs(graph, 0)
    clear(graph)
    print "===============DFS================="
    dfs(graph, 0)
    
    
if __name__ == "__main__":
    main()