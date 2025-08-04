from graph import Graph


"""g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edge("A", "B", 1)
g.add_edge("B", "C", 2)
g.add_edge("C", "D", 3)
g.add_edge("A", "D", 4)
g.add_edge("D", "A", 4)

print(g)

print("BFS from A:")
g.bfs("A")
print("-"*60)
print("DFS from A:")
g.dfs("A")
print("-"*60)
print("DFS Post Order from A:")
g.dfs_post_order("A")

print("-"*60)
print("BFS from C:")
g.bfs("C")
print("-"*60)
print("DFS from C:")
g.dfs("C")
print("-"*60)
print("DFS Post Order from C:")
g.dfs_post_order("C")"""



graph = Graph()
graph.add_vertex("Hospital")
graph.add_vertex("School")
graph.add_vertex("Store")
graph.add_vertex("Library")
graph.add_vertex("Park")
graph.add_vertex("Mall")


graph.add_edge("Hospital", "School", 5)
graph.add_edge("School", "Library", 3)
graph.add_edge("Library", "Park", 4)
graph.add_edge("Park", "Mall", 6)
graph.add_edge("Mall", "Store", 2)
graph.add_edge("Store", "Hospital", 7)
graph.add_edge("Hospital", "Mall", 10)
graph.add_edge("School", "Store", 9)
graph.add_edge("Library", "Store", 1)
graph.add_edge("Park", "Hospital", 8)
print(graph)

path, total = graph.dijkstra("Hospital", "Mall")
print("Shortest path:", path)
print("Total time:", total)


path1, total1 = graph.dijkstra("Hospital", 'Store')
print("Shortest path:", path1)
print("Total time:", total1)