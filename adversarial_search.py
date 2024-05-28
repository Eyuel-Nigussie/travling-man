from adversarial_graph import AdversarialGraph

class AdversarialSearchGraph:
    def __init__(self, graph):
        self.graph = graph

    def minimax(self, node, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or self.is_terminal(node):
            return self.utility(node)
        
        if maximizingPlayer:
            max_eval = float('-inf')
            for neighbor in self.graph.get_neighbors(node):
                eval = self.minimax(neighbor, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for neighbor in self.graph.get_neighbors(node):
                eval = self.minimax(neighbor, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def utility(self, node):
        return self.graph.get_utility(node)

    def is_terminal(self, node):
        return node in self.graph.utilities

    def find_best_move(self, start, depth):
        best_value = float('-inf')
        best_move = None
        alpha = float('-inf')
        beta = float('inf')
        
        for neighbor in self.graph.get_neighbors(start):
            move_value = self.minimax(neighbor, depth - 1, alpha, beta, False)
            if move_value > best_value:
                best_value = move_value
                best_move = neighbor
            alpha = max(alpha, best_value)
        
        return best_move

if __name__ == "__main__":
    g = AdversarialGraph()
    adversarial_search_graph = AdversarialSearchGraph(g)
    start = 'Addis Ababa'
    depth = 3
    
    best_move = adversarial_search_graph.find_best_move(start, depth)
    print(f"Best move from {start} with depth {depth}: {best_move}")
