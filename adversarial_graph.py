class AdversarialGraph:
    def __init__(self):
        self.graph = {
            'Addis Ababa': ['Ambo', 'Adama', 'Debre Birhan'],
            'Ambo': ['Addis Ababa', 'Gedo', 'Nekemte'],
            'Adama': ['Addis Ababa', 'Mojo', 'Dire Dawa'],
            'Debre Birhan': ['Addis Ababa'],
            'Gedo': ['Ambo', 'Shambu', 'Fincha'],
            'Nekemte': ['Ambo', 'Gimbi'],
            'Mojo': ['Adama', 'Buta Jirra'],
            'Dire Dawa': ['Adama', 'Harar'],
            'Shambu': [],
            'Fincha': [],
            'Gimbi': [],
            'Buta Jirra': ['Mojo', 'Woliso'],
            'Woliso': ['Buta Jirra', 'Wolkite'],
            'Wolkite': ['Woliso', 'Hossana'],
            'Hossana': ['Wolkite', 'Durame'],
            'Durame': [],
            'Bench Naji': ['Tepi'],
            'Tepi': ['Bench Naji'],
            'Kaffa': [],
            'Limu': [],
            'Dilla': [],
            'Chiro': [],
            'Harar': ['Dire Dawa'],
        }
        self.utilities = {
            'Shambu': 4,
            'Fincha': 5,
            'Gimbi': 8,
            'Limu': 8,
            'Durame': 6,
            'Tepi': 6,
            'Kaffa': 7,
            'Dilla': 9,
            'Chiro': 6,
            'Harar': 10,
        }

    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def get_utility(self, node):
        return self.utilities.get(node, 0)
