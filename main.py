from collections import defaultdict


def make_undirected_graph(edge_list):
  """ Makes an undirected graph from a list of edge tuples. """
  graph = defaultdict(set)
  for e in edge_list:
    graph[e[0]].add(e[1])
    graph[e[1]].add(e[0])
  return graph


def reachable(graph, start_node):
  visited = [start_node]
  frontier = set(graph[start_node])
  while len(frontier) != 0:
    temp = frontier.pop()
    if temp not in visited:
      visited.append(temp)
      frontier.update(graph[temp])
  return visited


"""
    Returns:
      the set of nodes reachable from start_node
    """


def connected(graph):
  visited = reachable(graph, list(graph.keys())[0])
  if len(graph) == len(visited):
    return True
  return False


def n_components(graph):
  visited = set()  # A set to keep track of all visited nodes
  count = 0
  for node in graph:
    if node not in visited:
      current_visited = reachable(graph, node)
      visited.update(current_visited)
      count += 1  
  return count
"""
    Returns:
      the number of connected components in an undirected graph
    """


test_graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'),
                                    ('D', 'B'), ('E', 'F'), ('F', 'G')])
print(connected(test_graph))



test_set = set()
test_set.update(['A','B','C'])
test_set.update(['A','E','F'])
print(test_set)