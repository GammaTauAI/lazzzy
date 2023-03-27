from queue import PriorityQueue
from typing import Callable, List, TypeVar, Tuple


State = TypeVar('State')


def ucs(start: State, is_goal: Callable[[State], bool], expand: Callable[[State], List[Tuple[State, float]]]) -> State:
    """Uniform Cost Search on a tree.

    Args:
        start: start node
        is_goal: function to check if a node is the goal node
        expand: function to expand a node, returns a list of (child, cost) pairs

    Returns:
        The goal node when found.
    """
    raise NotImplementedError
