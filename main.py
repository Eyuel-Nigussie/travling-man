import heapq
from graph import Graph

class SearchGraph:
    def __init__(self, graph):
        self.graph = graph
    
    def bfs(self, start, goal):
        visited = set()
        queue = [[start]]
        
        if start == goal:
            return [start]
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if node not in visited:
                neighbors = self.graph.get_neighbors(node)
                
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    
                    if neighbor == goal:
                        return new_path
                
                visited.add(node)
        
        return "No path found"
    
    def dfs(self, start, goal):
        visited = set()
        stack = [[start]]
        
        if start == goal:
            return [start]
        
        while stack:
            path = stack.pop()
            node = path[-1]
            
            if node not in visited:
                neighbors = self.graph.get_neighbors(node)
                
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)
                    
                    if neighbor == goal:
                        return new_path
                
                visited.add(node)
        
        return "No path found"
    
    def ucs(self, start, goal):
        visited = set()
        queue = [(0, [start])]
        
        while queue:
            cost, path = heapq.heappop(queue)
            node = path[-1]
            
            if node == goal:
                return path, cost
            
            if node not in visited:
                visited.add(node)
                
                for neighbor, weight in self.graph.get_neighbors(node).items():
                    if neighbor not in visited:
                        new_cost = cost + weight
                        new_path = path + [neighbor]
                        heapq.heappush(queue, (new_cost, new_path))
        
        return "No path found"
    
    def astar(self, start, goal):
        visited = set()
        queue = [(0, [start])]
        
        while queue:
            cost, path = heapq.heappop(queue)
            node = path[-1]
            
            if node == goal:
                return path, cost
            
            if node not in visited:
                visited.add(node)
                
                for neighbor, weight in self.graph.get_neighbors(node).items():
                    if neighbor not in visited:
                        new_cost = cost + weight
                        heuristic = self.graph.get_heuristic(neighbor, goal)
                        total_cost = new_cost + heuristic
                        new_path = path + [neighbor]
                        heapq.heappush(queue, (total_cost, new_path))
        
        return "No path found"
    
    def search(self, start, goal, strategy):
        if strategy == 'BFS':
            return self.bfs(start, goal)
        elif strategy == 'DFS':
            return self.dfs(start, goal)
        elif strategy == 'UCS':
            return self.ucs(start, goal)
        elif strategy == 'A*':
            return self.astar(start, goal)
        else:
            return "Invalid strategy"

if __name__ == "__main__":
    g = Graph()
    search_graph = SearchGraph(g)
    start = 'Addis Ababa'
    goal = 'Moyale'
    
    # Test BFS
    strategy = 'BFS'
    result = search_graph.search(start, goal, strategy)
    print(f"Path found using {strategy}: {result}")
    
    # Test DFS
    strategy = 'DFS'
    result = search_graph.search(start, goal, strategy)
    print(f"Path found using {strategy}: {result}")
    
    # Test UCS
    strategy = 'UCS'
    result = search_graph.search(start, goal, strategy)
    print(f"Path found using {strategy}: {result}")
    
    # Test A*
    strategy = 'A*'
    result = search_graph.search(start, goal, strategy)
    print(f"Path found using {strategy}: {result}")
