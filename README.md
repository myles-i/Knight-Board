#Knight Board
###This project implements code for checking move validity and computing the shortest path for moves of a knight chess piece on a chess board.
The knight board can be represented in x,y coordinates. The upper left position
is (0,0) and the bottom right is (7,7). The convention is (row, column).

- All moves are defined relative to the previous position. Aka (1,2) means move down one row, and right two columns from where the piece previously was.
- Knight_board.py contains a class that computes all of the game-specific information
- utils.py contains a simple implementation of a Priority Queue, and A* search algorithm and a few heuristics. These are used to determine the least costly path.
- A modified manhattan distance heuristic is used here, but there is certainly room for improvement on this front.

board_2 has the following additional rules:
1) W[ater] squares count as two moves when a piece lands there
2) R[ock] squares cannot be used
3) B[arrier] squares cannot be used AND cannot lie in the path
4) T[eleport] squares instantly move you from one T to the other in
the same move
5) L[ava] squares count as five moves when a piece lands there


## Features:
###Level 1: Check the validity of a sequence of moves
####The following code shows how to check the validity of a sequence of moves
board = knight_board("board_1.txt",(8,8)) ## Import the board
start_pos = (0,0);
move_sequence = ((1,2),(2,1),(2,1),(1,2))
print(board.is_sequence_legal(start_pos,move_sequence,print_board=True))
print(board.get_sequence_cost(start_pos,move_sequence))

###Level 2/3: Determine shortest sequence of moves from one location to another.
#### The following code shows how to compute this sequence:

board = knight_board("board_1.txt",(8,8)) ## Import the board
start_pos = (0,0);
end_pos   = (0,7);
print("Start is:", start_pos)
print("End is:", end_pos)
solution = aStarSearch(board,start_pos, end_pos, )
print(board.is_sequence_legal(start_pos,solution,print_board=True))
print("Solution:")
print(solution)
print("Cost: ")
print(board.get_sequence_cost(start_pos,solution))

### Level 4: Determine shortest sequence of moves with barriers, water, rock, and teleportation:
####The following code shows how to import the board and compute a sequence.The starting and ending position are specifically chosen so that the most efficient way is to use the teleportation:
board = knight_board("board_2.txt",(28,32))
start_pos = (0,24);
end_pos   = (24,29);
print("Start is:", start_pos)
print("End is:", end_pos)
solution = aStarSearch(board,start_pos, end_pos, heuristic=modified_manhattan)
print(board.is_sequence_legal(start_pos,solution,print_board=True))
print("Solution:")
print(solution)
print("Cost: ")
print(board.get_sequence_cost(start_pos,solution))


## Dependencies:
numpy
pandas
