import random

goal_location = {
    0: (0,0),
    1: (0,1),
    2: (0,2),
    3: (1,0),
    4: (1,1),
    5: (1,2),
    6: (2,0),
    7: (2,1),
    8: (2,2)
}

#creates an empty 3x3 board and fills it with numbers 0-8 in random order
def create_board():
    board = []
    numbers = list(range(0,9))
    for i in range(3):
        row = []
        for j in range(3):
            random_index = random.randrange(len(numbers))
            row.append(numbers[random_index])
            numbers.pop(random_index)
        board.append(row)
    return board

#calculates the manhattan distance each number is from its goal location
def calculate_manhattan_distance(board):
    total_cost = 0
    for row in range(len(board)):
        for val in range(len(board[row])):
            value = board[row][val]
            properLoc = goal_location[value]
            total_cost += abs(properLoc[0] - row) + abs(properLoc[1] - val)
    return total_cost


            

board = create_board()
print(board)
print(calculate_manhattan_distance(board))