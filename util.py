import heapq
import itertools
class PriorityQueue:
	 ## Implements a priority queue data structure. Each inserted item
		def  __init__(self):
				self.heap = []
				self.counter = itertools.count()     # unique sequence count

		def push(self, item, priority):
				count = next(self.counter)
				entry = (priority, count, item) # count used as tie-breaker
				heapq.heappush(self.heap, entry)

		def pop(self):
				(_, _, item) = heapq.heappop(self.heap)
				return item

		def isEmpty(self):
				return len(self.heap) == 0



def nullHeuristic(start, end):
 # This heuristic is trivial and does not help find the solution faster.
		return 0

def modified_manhattan(start, end):
	# each  knight chess move has a manhattan distance of 3, so this a permissible heuristic
	# - start and end are the staring and ending positions
	return (abs(start[0] - end[0]) + abs(start[1] - end[1]))//3

def aStarSearch(knight_board,start,end, heuristic=nullHeuristic):
		# Performs A* search with a specified heuristic
		# Inputs:
		# - board: is of class "knight_board" and contains the game information
		# - start: is the starting position
		# - end: is the ending position
		# - heuristic: is the function to be used to compute the heuristic for A* search
		"Search the node that has the lowest combined cost and heuristic first."
		closed=set()
		fringe=PriorityQueue() 
		# Elements of fringe contain ( (position, list of moves), cost + heuristic
		fringe.push((start,list()) , heuristic(start,end))
		i = 0; # count number of iterations needed to compute solution
		while True:
				i +=1;
				if fringe.isEmpty():
						return 'failure'  
				# grab the least costly node
				currentNode=fringe.pop()
				currentLocation=currentNode[0];
				if np.array_equal(currentLocation,end):
						print("Number of iterations: ",i)
						return currentNode[1]
				if (currentLocation not in closed): # no need to re-visit nodes we have already seen
						closed.add(currentLocation)
						moves=knight_board.get_knight_moves(currentLocation)
						for move in moves: # add all to fringe
								newLocation, cost = knight_board.move_knight(currentLocation,move)

								newSequence = currentNode[1].copy()
								newSequence.append(move)
								sequence_cost = knight_board.get_sequence_cost(start,newSequence)

								fringe.push((newLocation,newSequence) , sequence_cost+heuristic(newLocation,end))