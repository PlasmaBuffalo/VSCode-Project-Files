# objective: create a program that solves the knight's tour problem

# method that reads and returns user input for board size (n*n), starting position (x,y), and "closed" or "open" tour
def knightTourInput() -> tuple[int, int, int, str]:
    # get board size
    n: int = int(input("Enter the size of the board (n*n): "))
    #if n is less than 5, then the board is too small to solve the knight's tour problem
    # check if n < 5. if so, set n = 5
    if n < 5:
        n = 5
    # get starting position
    x: int = int(input("Enter the starting position x: "))
    y: int = int(input("Enter the starting position y: "))
    # get tour type
    tourType = input(
        "Enter 'closed' for closed tour or 'open' for open tour: ")
    # return the input values
    return n, x, y, tourType
