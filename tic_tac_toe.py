

#instructions
#2 players should be able to play the game 
#(both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position 
#and then place a symbol on the board



#board is a 3 x 3 grid starting empty
board = [['.','.','.'],['.','.','.'],['.','.','.']]

def print_board(matrix):
	for row in matrix:
		print row
		#print '\n'


def player_move(move_counter):

	while True:

		if move_counter %2 == 0:
			print 'Player 2, it is your turn'
		else:
			print 'Player 1, it is your turn'

		
		#player move needs to be an integer
		try:
			row_choice = int(raw_input('which row would you like to place your move? (1, 2, or 3?)'))
			#col_choice = int(raw_input('which column would you like to place your move? (1, 2, or 3?)'))
		#I cannot figure out the right error to catch here
		except ValueError():
			print 'This is not a number'
			continue



		#print 'This is not a 1, 2, or 3. Please try again. '

		#need a verification step to make sure that the input is correct
		if row_choice not in range (1,4):
			print 'This row choice is not a 1, 2, or 3. Please try again. '
			continue
		if col_choice not in range (1,4):
			print 'This col choice is not a 1, 2, or 3. Please try again. '
			continue

		#print ('here is the board tuple choice', row_choice-1,col_choice-1 )
		#print ('here is what is at that spot', board[row_choice-1][col_choice-1])

		#verification step to make sure board square is empty
		if board[row_choice-1][col_choice-1] == '.':
			#assign proper symbol
			symbol = ''

			if move_counter %2 == 0:
				symbol = 'O'
			else:
				symbol = 'X'

			#put symbol on board
			board[row_choice-1][col_choice-1] = symbol

			move_counter += 1

			return board
		else:
			print 'That space is not open. Pick a different space'
			continue

def is_board_full(board):

	#check to see if board is full
	for row in board:
		for space in row:
			if space == '.':
				return False

	return True

def referee(game_result):
    result = ''

    #the checking function
    def check_it(matrix):
        for row in matrix:
            #print (row)
            if row == ['X','X','X']:
            	return 'X'
            elif row == ['O','O','O']:
                return 'O'
    
    # check rows
    result = check_it(game_result)
    
    if not result:
        #check columns
        game_cols = [['.','.','.'],['.','.','.'],['.','.','.']]
        i = 0
        for row in game_result:
            game_cols[0][i] = row[0]
            game_cols[1][i] = row[1]
            game_cols[2][i] = row[2]
            i += 1
        #print ('cols ')
        #print_board(game_cols)
        result = check_it(game_cols)
    
    if not result:
        #check diagonal
        game_diag = [[game_result[0][0],game_result[1][1],game_result[2][2]],
        			 [game_result[2][0],game_result[1][1],game_result[0][2]]]
        #print('diag ', game_diag)
        result = check_it(game_diag)
    
    if not result:
        return 'D'
    else:
        return result

def cycle_of_play(board):
	keep_going = True
	move_counter = 1

	while keep_going:

		#player move
		player_move(move_counter)

		print_board(board)

		winner = referee(board)

		#check for a winner
		if winner == 'X':
			print 'player 1 wins!'
			keep_going = False
		elif winner == 'O':
			print 'player 2 wins!'
			keep_going = False
		elif winner == 'D' and is_board_full(board):
			print 'a draw! no winner'
			keep_going = False
		else:
			print 'no winner yet, keep going!'
			keep_going = True

		move_counter +=1


def welcome():
	print 'Welcome to Tic Tac Toe!'
	print 'Here is the board'
	print_board(board)	
	print 'Let\'s play'



if __name__== "__main__":
    welcome()
    cycle_of_play(board)



