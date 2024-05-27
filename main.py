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
    
    def search(self, start, goal, strategy):
        if strategy == 'BFS':
            return self.bfs(start, goal)
        elif strategy == 'DFS':
            return self.dfs(start, goal)
        else:
            return "Invalid strategy"

if __name__ == "__main__":
    g = Graph()
    search_graph = SearchGraph(g)
    start = 'Addis Ababa'
    goal = 'Dodola'
    strategy = 'BFS'
    
    path = search_graph.search(start, goal, strategy)
    print(f"Path using {strategy}: {path}")
    
    strategy = 'DFS'
    path = search_graph.search(start, goal, strategy)
    print(f"Path using {strategy}: {path}")
