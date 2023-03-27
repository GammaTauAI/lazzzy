from queue import PriorityQueue
from typing import Callable, List, TypeVar, Tuple


State = TypeVar('State')
UniqueID = TypeVar('UniqueID')


def ucs(
    start: State, is_goal: Callable[[State], bool],
    expand: Callable[[State], List[Tuple[State, float]]],
    get_unique_id: Callable[[State], UniqueID] = lambda x: x
) -> State | None:
    """Lazy Uniform Cost Search.

    Args:
        start: start node
        is_goal: function to check if a node is the goal node
        expand: function to expand a node, returns a list of (child, cost) pairs
        get_unique_id (optional): function to get a unique id for a node

    Returns:
        The goal node when found. Returns None if no path is found.
        Some implementations off expand will not ever return None.
    """
    # is the start node the goal node?
    if is_goal(start):
        return start

    # start up the queue
    queue = PriorityQueue()
    queue.put((0, start))
    visited: set[UniqueID] = set()

    while not queue.empty():
        cost, node = queue.get()
        visited.add(get_unique_id(node))

        for child, child_cost in expand(node):
            # skip if already visited
            if get_unique_id(child) in visited:
                continue

            # check if it's goal
            if is_goal(child):
                return child

            # add to queue
            queue.put((cost + child_cost, child))

    return None


if __name__ == '__main__':
    # define the graph
    graph = {
        'A': [('B', 1), ('C', 2)],
        'B': [('D', 3), ('A', 0)],
        'C': [('D', 1)],
        'D': [('E', 1)],
        'E': []
    }

    # define the goal
    goal = 'E'

    # define the expand function
    def expand(node: str) -> List[Tuple[str, float]]:
        return graph[node]

    # define the is_goal function
    def is_goal(node: str) -> bool:
        return node == goal

    # run the search
    result = ucs('A', is_goal, expand)
    print(result)
