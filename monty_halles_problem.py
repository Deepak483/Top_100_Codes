# Import packages
import math
from pomegranate import *

# The door selected by the guest is totally random
guestSelection = DiscreteDistribution({'A': 1./3, 'B': 1./3, 'C': 1./3})

# The door having the prize is also a random process
prizeSelection = DiscreteDistribution({'A': 1./3, 'B': 1./3, 'C': 1./3})

# The door host Monty picks, depends on the choice of the guestSelection and the prizeSelection

montySelection = ConditionalProbabilityTable(
    [['A', 'A', 'A', 0.0],
     ['A', 'A', 'B', 0.5],
        ['A', 'A', 'C', 0.5],
        ['A', 'B', 'A', 0.0],
        ['A', 'B', 'B', 0.0],
        ['A', 'B', 'C', 1.0],
        ['A', 'C', 'A', 0.0],
        ['A', 'C', 'B', 1.0],
        ['A', 'C', 'C', 0.0],
        ['B', 'A', 'A', 0.0],
        ['B', 'A', 'B', 0.0],
        ['B', 'A', 'C', 1.0],
        ['B', 'B', 'A', 0.5],
        ['B', 'B', 'B', 0.0],
        ['B', 'B', 'C', 0.5],
        ['B', 'C', 'A', 1.0],
        ['B', 'C', 'B', 0.0],
        ['B', 'C', 'C', 0.0],
        ['C', 'A', 'A', 0.0],
        ['C', 'A', 'B', 1.0],
        ['C', 'A', 'C', 0.0],
        ['C', 'B', 'A', 1.0],
        ['C', 'B', 'B', 0.0],
        ['C', 'B', 'C', 0.0],
        ['C', 'C', 'A', 0.5],
        ['C', 'C', 'B', 0.5],
        ['C', 'C', 'C', 0.0]], [guestSelection, prizeSelection])

d1 = State(guestSelection, name="guest choice")
d2 = State(prizeSelection, name="prize choice")
d3 = State(montySelection, name="monty choice")

# Lets Building the Bayesian Network
network = BayesianNetwork('Monty Hall Problem With Bayesian Networks')
network.add_states(d1, d2, d3)
network.add_edge(d1, d3)
network.add_edge(d2, d3)
network.bake()

# Here, A, B, C denotes the door picked by the guest, prize containing door, and Monty’s door.

# Let’s make the predictions assuming guest picks A. Monty is going to pick up either B or C as A contains a prize

beliefs = network.predict_proba({'guestSelection': 'A'})
beliefs = map(str, beliefs)
print("n".join("{}t{}".format(state.name, belief)
      for state, belief in zip(network.states, beliefs)))

# guest A
prize = {
    "class": "Distribution",
    "dtype": "str",
    "name": "DiscreteDistribution",
    "parameters": [
        {
            "A": 0.3333333333333333,
            "B": 0.3333333333333333,
            "C": 0.3333333333333333
        }
    ],
}

monty = {
    "class": "Distribution",
    "dtype": "str",
    "name": "DiscreteDistribution",
    "parameters": [
        {
            "C": 0.49999999999999983,
            "A": 0.0,
            "B": 0.49999999999999983
        }
    ],
}


beliefs = network.predict_proba({'guestSelection': 'A', 'montySelection': 'B'})
print("n".join("{}t{}".format(state.name, str(belief))
      for state, belief in zip(network.states, beliefs)))

# guest A
prize = {
    "class": "Distribution",
    "dtype": "str",
    "name": "DiscreteDistribution",
    "parameters": [
        {
            "A": 0.3333333333333334,
            "B": 0.0,
            "C": 0.6666666666666664
        }
    ],
}
# monty B
