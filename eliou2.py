import random 

#Battleship Board and Ship sizes 
size_board = 10 
num_ships = 5

#This will create the board itself 
def setup_board():
    board = [ ['.' for _ in range(size_board)] for _ in range(size_board)]

#Places the ships on the board RANDOMLY!
    for _ in range(num_ships):
        while True: 
                row = random.randint(0, size_board - 1)
                column = random.randint(0, size_board - 1)
                if board [row][column] == '.':
                     board[row][column] = 'S'
                     break
    return board
        

#formatting the column by printing 

def draw_board(board):
     print("    " + " ".join(str(i) for i in range(size_board)))
     print("   +" + "---+" * size_board)

     #format the rows by printing 
     for row in range(size_board):
        row_header = f"{row}  |"

          #Adding the cells in the row
        for column in range(size_board):
            row_header += f" {board[row][column]} |"
            # Constructs the grid lines
        print(row_header)
     
# Separate the rows horizontally 
        print("   +" + "---+" * size_board)

# Check to see if ships have been hit (No 'S' left)

def is_game_over(board):
    for row in board:
         if 'S' in row:
              return False
         return True
    
#Function that checks to see if the square has a ship or not 

def hit_or_miss(board, row, column):
     if board[row][column] == 'S':
          board[row][column] = 'X' #Hit
          return "HIT!"
     elif board[row][column] == 'X':
          return "HIT!" #Signifies that ship is still hit 
     else:
          board[row][column] = 'O' #miss
          return "MISS!"
     
#Main funct. of the game

def main():
     board = setup_board()
     
     while True:
          draw_board(board)

          try:
               column = int(input("Enter a column from 0-9: ")) #prompts user to enter column.
               if column < 0 or column >= size_board:
                    print("Invalid column! Enter a column from 0-9.")
                    continue
          except ValueError:
               print("Invalid input! Please enter a number between 0-9.")
               continue
          
          try:
               row = int(input("Enter a row from 0-9: "))
               if row < 0 or row >= size_board:
                    print("Invalid row! Please enter a row from 0-9.")
          except ValueError:
               print("Invalid row! Please enter a number between 0 and 9.")
               continue
          # is it a hit or miss?
          result = hit_or_miss(board, row, column)
          print(result)
          # is game over?
          if is_game_over(board):
               draw_board(board)
               print("GAME OVER!")
               break
          
#Run game

main()
          
    