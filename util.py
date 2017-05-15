import heapq
import itertools
class PriorityQueue:
   ## Implements a priority queue data structure. Each inserted item
    def  __init__(self):
        self.heap = []
        self.counter = itertools.count()     # unique sequence count

    def push(self, item, priority):
        count = next(self.counter)
        entry = (priority, count, item)
        heapq.heappush(self.heap, entry)

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        #  (_, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0



def nullHeuristic(start, end):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(knight_board,start,end, heuristic=nullHeuristic):
    # note: inputs are lists, but they need to be numpy arrays for use with knight_board
    "Search the node that has the lowest combined cost and heuristic first."
    closed=set()
    fringe=PriorityQueue() 
    fringe.push((start,list(),0) , heuristic(start,end))
    while True:
        if fringe.isEmpty():
            return 'failure'
        currentNode=fringe.pop()
        currentLocation=currentNode[0];


        if np.array_equal(currentLocation,end):
            return currentNode[1]
        if (currentLocation not in closed):
            closed.add(currentLocation)
            moves=knight_board.get_knight_moves(currentLocation)
            for move in moves:
                newLocation, cost = knight_board.move_knight(currentLocation,move)
                # print("newLocation:", newLocation)
                newSequence = currentNode[1].copy()
                newSequence.append(move)
                sequence_cost = knight_board.get_sequence_cost(start,newSequence)
                fringe.push((newLocation,newSequence) , sequence_cost+heuristic(newLocation,end))