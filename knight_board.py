import numpy as np
import pandas as pd
from math import *


class knight_board:
	""" This class represents a board for a game played with only knight_board

	Attributes:
	board: an array representing the board
	"""

	def __init__(self,board_txt_file,board_size):
		# board_txt_file: is the filename containing the board information
		# board_size is the size of the board (row,column)
		board_pd = pd.read_csv(board_txt_file,delimiter= "\n")
		board = board_pd.board.as_matrix()
		self.board = np.resize(board,(board_size[1],board_size[0])).transpose()
		# find teleportation
		teleportation_idx = np.transpose(np.nonzero(self.board=='T'	))
		# assume there are either 0 or 2 teleportation ids
		if teleportation_idx.size !=0:
			self.T0 = tuple(teleportation_idx[0])
			self.T1 = tuple(teleportation_idx[1])
		else:
			self.T0 = (nan,nan)
			self.T1 = (nan,nan)


		# if teleportation_
		return

	def get_knight_moves(self,loc):
		potential_moves = ((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1))
		moves = list()

		for move in potential_moves:
			if self.is_move_legal(loc, move):
				moves.append(move)
		return moves


	def is_move_legal(self,loc, move):
		# check that this is a valid chess move (not considering board size or other features)
		if not((abs(move[0]) ==1 or abs(move[0]) == 2) and (abs(move[1]) ==1 or abs(move[1]) ==2)):
			# print('Move not legal! Does not abide by knight moves')
			return False

		# derive the three intermediate moves (x then y)
		sgn_x = move[0]//abs(move[0])
		sgn_y = move[1]//abs(move[1])
		m1 = (sgn_x,0)
		if abs(move[0]) == 1:
			m2 = (0,sgn_y)
			m3 = (0,sgn_y)
		else:
			m2 = (sgn_x,0)
			m3 = (0,sgn_y)

		# first try x then y, and y then x
		move_xy_legal = self.is_move_legal_helper(loc,(m1,m2,m3))
		move_yx_legal = self.is_move_legal_helper(loc,(m3,m2,m1))
		move_legal = move_xy_legal or move_yx_legal
		# if not(move_legal):
			# print('Move not legal!')
		return move_legal

	def is_move_legal_helper(self,loc,intermediate_moves):
		# checks the intermediate moves of a full move one by one to make sure path is valid
		loc_temp = (loc[0],loc[1])
		for interim_move in intermediate_moves:
			loc_temp = (loc_temp[0] + interim_move[0], loc_temp[1] + interim_move[1])
			# Check for barriers and out of bounds
			if not(self.is_in_bounds(loc_temp)) or self.is_barrier(loc_temp):
				return False

		# Check if final location is a rock (illegal)
		if self.is_rock(loc_temp):
			return False
		else:
			return True


	def is_sequence_legal(self, loc, moves,print_board = False):
		if print_board:
			print("Starting Location:")
			self.print_knight_loc(loc)	

		for move in moves:
			if self.is_move_legal(loc,move):
				loc, cost= self.move_knight(loc,move, print_board)
			else:
				return False
		return True # all moves were valid

	def get_sequence_cost(self,start, moves):
		# assume all moves are legal
		loc = start
		total_cost = 0
		for move in moves:
			loc, move_cost = self.move_knight(loc,move)
			total_cost += move_cost
		return total_cost


	def move_knight(self,loc, move, print_board = False):
		# assume move is legal
		new_loc = (loc[0] + move[0],loc[1] + move[1])
		# Teleport if necessary
		if np.array_equal(self.T0,new_loc):
			# print("T0")
			new_loc = self.T1
		elif np.array_equal(self.T1,new_loc):
			# print("T1")
			new_loc = self.T0	


		if self.is_water(new_loc):
			cost = 2
		elif self.is_lava(new_loc):
			cost = 5
		else:
			cost = 1


		if print_board:
			self.print_knight_loc(new_loc)		
		return new_loc, cost




	def print_knight_loc(self,loc):
		shp = self.board.shape
		for i in range(0,shp[0]):
			for j in range(0,shp[1]):
				if np.array_equal([i,j],loc):
					print_char = 'K '
				else:
					print_char = '. '

				if j == (shp[1]-1):
					print(print_char)
				else:
					print(print_char, end="")
		print('\n\n')	


	def print_board(self):
		shp = self.board.shape
		print(shp)
		for i in range(0,shp[0]):
			for j in range(0,shp[1]):

				if j == (shp[1]-1):
					print(self.board[i][j])
				else:
					print(self.board[i][j], end="")
		print('\n\n')	


	def is_barrier(self,loc):
		return self.board[(loc[0],loc[1])] == 'B'
	def is_lava(self,loc):
		return self.board[(loc[0],loc[1])] == 'L'
	def is_rock(self,loc):
		return self.board[(loc[0],loc[1])] == 'R'
	def is_water(self,loc):
		return self.board[(loc[0],loc[1])] == 'W'
	def is_in_bounds(self,loc):
		shp = self.board.shape
		for i in range(0,2):
			if loc[i]<0  or loc[i]>(shp[i]-1):
				return False
		return True

