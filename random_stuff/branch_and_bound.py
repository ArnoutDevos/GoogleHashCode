import pybnb
import numpy as np

class Knapsack(pybnb.Problem):
    def __init__(self):
        self.capacity = 10.0

        self.values = np.array([40., 50., 100., 95., 30.], dtype=np.float32)
        self.weights = np.array([2, 3.14, 1.98, 5., 3.], dtype=np.float32)

        # Sort them so the bounds are better
        order = np.argsort(-self.values)
        self.values = self.values[order]
        self.weights = self.weights[order]

        # State
        self.knapsack = np.zeros_like(self.values)
        self.idx = 0

    def sense(self):
        return pybnb.maximize

    def objective(self):
        # Assume all nodes that are registered have an okay weight
        return (self.knapsack * self.values).sum()
        # return self.infeasible_objective()

    def bound(self):
        # A valid bound is: include all the remaining items
        rest = self.values[self.idx:].sum()
        return self.objective() + rest

    def save_state(self, node):
        node.state = (self.knapsack, self.idx)

    def load_state(self, node):
        self.knapsack, self.idx = node.state

    def branch(self):
        weight = (self.knapsack * self.weights).sum()
        if self.idx < len(self.knapsack):
            # Include the nxt item if our knapsack permits
            if weight + self.weights[self.idx] <= self.capacity:
                node = pybnb.Node()
                knapsack = self.knapsack.copy()
                knapsack[self.idx] = 1.0
                node.state = (knapsack, self.idx + 1)
                yield node

            # Exclude
            node = pybnb.Node()
            knapsack = self.knapsack.copy()
            node.state = (knapsack, self.idx + 1)
            yield node


problem = Knapsack()
results = pybnb.solve(problem,
                    #   queue_strategy='depth',
                      best_objective=200, # output of some greedy solver or something, to prune the tree more quickly
                      relative_gap=1e-9,
                      absolute_gap=1e-9)

print(results.best_node, results.best_node.state)
