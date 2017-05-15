#Knight Board
###This project implements code for checking move validity and computing the shortest path for moves of a knight chess piece on a chess board.

## Features:
###Level1: Check the validity of a sequence of moves
####The following code shows how to check the validity of a sequence of moves
board = knight_board("board_1.txt",(8,8))
start_pos = (0,0);
move_sequence = ((1,2),(2,1),(2,1),(1,2))
print(board.is_sequence_legal(start_pos,move_sequence,print_board=True))
print(board.get_sequence_cost(start_pos,move_sequence))

###Level2/3: Determine shorts sequence of moves from one location to another.
#### The follownig code shows how to compute this sequence:
start_pos = (0,0);
end_pos   = (7,7);
print("Start is:", start_pos)
print("End is:", end_pos)
solution = aStarSearch(board,start_pos, end_pos)
print(board.is_sequence_legal(start_pos,solution,print_board=True))
print(solution)


## Dependencies:
numpy
pandas
