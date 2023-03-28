# Python Library for Lazy UCS

This library provides a Python implementation of
[Uniform-cost search](https://en.wikipedia.org/?title=Uniform-cost_search&redirect=no)
(a variant of [Dijkstra's algorithm](https://en.wikipedia.org/?title=Dijkstra%27s_algorithm&redirect=no))
that is lazily evaluated. This means that the algorithm is able to generate
the graph that is being searched in a lazy fashion, given only:

- the starting node
- a function that generates the neighbors of a node
- a function that determines if the given node is the goal node
