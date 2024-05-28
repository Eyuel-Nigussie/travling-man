import heapq

class SearchGraphWithCosts:
    def __init__(self, graph):
        self.graph = graph
    
    def ucs(self, start, goal):
        # Priority queue: stores (cost, path) tuples
        queue = [(0, [start])]
        visited = set()
        
        while queue:
            cost, path = heapq.heappop(queue)
            node = path[-1]
            
            if node in visited:
                continue
            
            visited.add(node)
            
            if node == goal:
                return path, cost
            
            for neighbor, edge_cost in self.graph[node]:
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    new_path = list(path)
                    new_path.append(neighbor)
                    heapq.heappush(queue, (new_cost, new_path))
        
        return "No path found", float('inf')

# Example usage:
graph_with_costs = {
    'Addis Ababa': [('Ambo', 1), ('Adama', 2), ('Debre Birhan', 3), ('Debre Markos', 4)],
    'Adama': [('Assela', 2), ('Ambo', 2), ('Batu', 1), ('Bishoftu', 1), ('Dodola', 5)],
    'Ambo': [('Addis Ababa', 1), ('Adama', 2), ('Nekemte', 3), ('Wolkite', 2)],
    'Assela': [('Adama', 2), ('Dodola', 3), ('Batu', 2)],
    'Batu': [('Adama', 1), ('Assela', 2), ('Wolkite', 1), ('Butajira', 2)],
    'Bishoftu': [('Adama', 1), ('Dukem', 1)],
    'Debre Birhan': [('Addis Ababa', 3), ('Debre Sina', 2)],
    'Debre Markos': [('Addis Ababa', 4), ('Finote Selam', 3), ('Bahir Dar', 5)],
    # Continue this for all nodes...
}

search_graph_with_costs = SearchGraphWithCosts(graph_with_costs)
print(search_graph_with_costs.ucs('Addis Ababa', 'Lalibela'))
