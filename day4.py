filename = 'puzzle_input/day4.txt'
my_input = []

part_one = False    # True to do part 1. False to do part 2.

with open(filename) as file:
    for line in file:
        my_input.append(line.strip())
        
bingo_cage = (my_input.pop(0)).split(',')

my_input.pop(0)    # Get rid of the first blank line

bingo_boards = []
this_board = {}
row, col = 0, 0
final_ball = None
bingo_count = 0    # Only for Part 2
bingo = False      # In this context, the bingo var will just tell us
                   # when we're done. So for Part 2 we only set this to
                   # true when each board has had a bingo
        
for line in my_input:
    if line == '':
        this_board['rows'] = [0,0,0,0,0]
        this_board['cols'] = [0,0,0,0,0]
        this_board['bingo'] = False
        bingo_boards.append(this_board)
        this_board = {}
        row, col = 0, 0
    else:
        this_line = line.split()
        col = 0
        for this_square in this_line:
            this_board[this_square] = [row, col, False]
            col += 1
        row += 1

total_boards = len(bingo_boards)

for bingo_ball in bingo_cage:
    for this_board in bingo_boards:
        # For Part 2 we only care about boards that have no bingo
        # (and for part 1 it doesn't matter)
        if not this_board['bingo']:
            if bingo_ball in this_board:
                # Get the row and column that this number is in
                this_row = this_board[bingo_ball][0]
                this_col = this_board[bingo_ball][1]
                
                # Mark this number as selected
                # Then increment the number of selected squares
                # in the row and column
                this_board[bingo_ball][2] = True
                this_board['rows'][this_row] += 1
                this_board['cols'][this_col] += 1
                
                # Check for bingo
                if this_board['rows'][this_row] == 5 or this_board['cols'][this_col] == 5:
                    this_board['bingo'] = True
    
                    if part_one:
                        bingo = True
                        final_ball = int(bingo_ball)
                        break
                        
                    if not part_one:
                        bingo_count += 1
                        if bingo_count == total_boards:
                            final_ball = int(bingo_ball)
                            bingo = True
                            break
    
    if bingo:
        unmarked_ball_sum = 0
        for this_key in this_board:
            if this_key == 'rows' or this_key == 'cols' or this_key == 'bingo':
                pass
            else:
                if this_board[this_key][2] is False:
                    unmarked_ball_sum += int(this_key)
        if part_one:
            print("Part 1:", unmarked_ball_sum * final_ball)
        else: 
            print("Part 2:", unmarked_ball_sum * final_ball)
        break
        
