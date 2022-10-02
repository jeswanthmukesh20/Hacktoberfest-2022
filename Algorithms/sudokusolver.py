#           AUTOMATIC SUDOKU SOLUTION WITH BACKTACKING ALGO

#board 9x9 for our soduku where 0 is used to represent empty spaces
board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
def solve(bo):
    if Find := find_empty(bo):
        row,col= Find

    else:
        return True
    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col]=i

            if solve(bo):
                return True

            bo[row][col]=0
    return False
#checking values if they are valid or not
def valid(bo,num,pos):
    #checking row
    for i in range(len(bo[0])):
        if bo[pos[0]][i]==num and pos[1] !=i:
            return False

    #checking column
    for i in range(len(bo)):
        if bo[i][pos[1]]==num and pos[1] !=i:
            return False

    #checking small boxes
    box_x= pos[1]//3
    box_y=pos[0]//3 

    for i in range(box_x*3,box_y+3):
        for j in range(box_y*3,box_x+3):
            if bo[i][j]== num and (i,j) !=pos:
                return False
    return True





#printing board and solving it 

def print_board(bo):
    for i in range(len(bo)):
        if i%3 ==0 and i !=0:
            print("----------------------")

        for j in range(len(bo[0])):
            if j%3==0 and j !=0:
                print("|", end=" ")

            if j==8:
                print(bo[i][j])
            else:
                print(f"{str(bo[i][j])} ", end="")
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return(i,j)

print_board(board)
solve(board)
print("____________________________________________________________________")
print_board(board)

#solved using backtracking algoritm in python
