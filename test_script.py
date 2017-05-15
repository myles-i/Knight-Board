exec(open("./knight_board.py").read())
exec(open("./util.py").read())
import numpy as numpy

################################
# Test Level 1
################################
# board = knight_board("board_1.txt",(8,8))
# start_pos = (0,0);
# move_sequence = ((1,2),(2,1),(2,1),(1,2))
# print(board.is_sequence_legal(start_pos,move_sequence,print_board=True))
# print(board.get_sequence_cost(start_pos,move_sequence))
################################
# Test Level 2/3
################################
# board = knight_board("board_1.txt",(8,8))
# start_pos = (0,0);
# end_pos   = (0,7);
# print("Start is:", start_pos)
# print("End is:", end_pos)
# solution = aStarSearch(board,start_pos, end_pos)
# print(board.is_sequence_legal(start_pos,solution,print_board=True))
# print(solution)

# ################################
# # Test Level 4
# ################################
board = knight_board("board_2.txt",(28,32))
print(board.T0)
print(board.T1)
start_pos = (0,24);
end_pos   = (24,29);
print("Start is:", start_pos)
print("End is:", end_pos)
print(solution)
solution = aStarSearch(board,start_pos, end_pos)
print(board.is_sequence_legal(start_pos,solution,print_board=True))
print(solution)