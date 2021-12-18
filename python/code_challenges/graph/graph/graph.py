
from collections import deque

class Queue:
  def __init__(self):
    self.dq = deque()

  def enqueue(self, value):
    self.dq.appendleft(value)

  def dequeue(self):
    return self.dq.pop()

  def __len__(self):
    return len(self.dq)

class Stack:
  def __init__(self):
        self.dq = deque()

  def push(self, value):
       self.dq.append(value)

  def pop(self):
        self.dq.pop()

class Vertex:
  """
  Input:Value
  What is doing: Store the value
  Return: None
  """
  def __init__(self, value):
    self.value = value

  def __str__(self):
         return self.value

class Edge:
  """
  Input: Vertex, weight
  What is doing: Store the vertex and the weight
  Return: None
  """
  def __init__(self,vertex, weight = 0):
    self.vertex = vertex
    self.weight = weight

class Graph:
  """
  Input: None
  What is doing: It is creating an empty graph
  Return: None
  """
  def __init__(self):
    self.__adjacency_list = {}

  def __str__(self):
        all_vertex=list(self.__adjacency_list.keys())
        str=""
        for ver in all_vertex:
            str += str(ver) + " -> "

        str += " None"
        return str
  """
  Input : Value
  What is doing : add node to the Graph
  Return : node
  """
  def add_node(self, value):
    node = Vertex(value)
    self.__adjacency_list[node] = []
    return node

  """
  Input: start_vertex, end_vertex ,
  weight:optional
  What is doing: Creat an edge and append the edge to the value of
  start_vertex inside the adj_list
  Return: None
  """
  def add_edge(self, start_vertex, end_vertex, weight=0):
    if start_vertex not in self.__adjacency_list:
      raise KeyError("Start Vertex is not found")

    if end_vertex not in self.__adjacency_list:
      raise KeyError("End Vertex is not found")

    edge = Edge(end_vertex , weight)
    self.__adjacency_list[start_vertex].append(edge)

  """
  Input : Vertex
  What is doing: Get all neighbors for a vertex
  Return: a list of edges
  """
  def get_neighbors(self, vertex):
    return self.__adjacency_list.get(vertex, [])



  """
  Input : None
  What is doing : get all the nodes in the graph as a set or list
  Return : a list or set of the nodes
  """
  def get_nodes(self):
    return self.__adjacency_list.keys()

  """
  Input: None
  What is doing: find the length of the adj_list
  Return: int The size(the length of adj_list)
  """
  def size(self):
    return len(self.__adjacency_list)

  """
  Input: Start_vertex
  What is doing: it will traverse throught all nodes
  Return: A list of nodes
  """
  def bfs(self, start_vertex):
    queue = Queue()
    result = []
    visited = set()

    queue.enqueue(start_vertex)
    visited.add(start_vertex)
    result.append(start_vertex)

    while len(queue):
      current_vertex = queue.dequeu()

      neighbors = self.get_neighbors(current_vertex)

      for edge in neighbors:
        neighbor = edge.vertex

        if neighbor not in visited:
          queue.enqueue(neighbor)
          visited.add(neighbor)
          result.append(neighbor)

    return result

if __name__ == '__main__':

    ver1=Vertex('a')
    ver2=Vertex('c')
    ver3=Vertex('d')
    ver4=Vertex('p')

    graph=Graph()
    graph.add_node(ver1)
    graph.add_node(ver2)
    graph.add_node(ver3)
    graph.add_node(ver4)

    # graph.add_edge(ver1,ver2)
    # graph.add_edge(ver1,ver3)
    # graph.add_edge(ver2,ver4)

    print(len(graph.get_neighbors(ver1)))


    print(graph.size() )


