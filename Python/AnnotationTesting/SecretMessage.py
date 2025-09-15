# imports
import requests
from bs4 import BeautifulSoup as bs
#-------------------------------------------
# data structure: list of objects with three parameters: x value integer, unicode character/string, y value integer
class puzzle_piece:
    def __init__(self, x: int, y: int, text: str) -> None:
        self.x = x
        self.y = y
        self.text = text

    def __str__(self) -> str:
        return self.text+" at ("+str(self.x)+", "+ str(self.y)+")"
# create an array to contain all of our puzzle_pieces
puzzle_list = []

# main function to decode message
def decode_message(url:str) -> None:
    r = requests.get(url)
    # now r.text is the HTML of the webpage. we'll use BeautifulSoup to read this and find the table we're looking for
    soupPage = bs(r.text, 'html.parser')

    #! the table row classes change every couple minutes! and for what!?
    for row in soupPage.find_all('tr'):
        # we save the current row as text to manipulate it
        trim_row = str(row)
        # gutting the row of all HTML tags
        # while a tag opener exists, find the closing tag and remove everything in between
        # repeat until no tags exist in the string
        while trim_row.find("<") != -1:
            # print(trim_row)
            openIndex = trim_row.find("<")
            closeIndex = trim_row.find(">")
            trim_row = trim_row[:openIndex]+trim_row[closeIndex+1:]

        # condition to check if the current trim row is the header. skip it if so.
        if(trim_row[0].isalpha()):
            pass
        else:
            # here's where we have a number, character, number pattern
            # something like [#####]""[#####] in terms of data format
            i = 0
            while trim_row[i].isdigit():
                i = i+1
            # this loop breaks when the character is found, meaning that at index i is the character
            # this also means that trim_row[0:i] is the x value
            # then, trim_row[i] is the character
            # finally, trim_row[i+1:] is the y value
            puzzle_list.append(puzzle_piece(int(trim_row[0:i]), int(trim_row[i+1:]), trim_row[i]))

    # gotta find the maximum bounds of the x and y values so we know how far we will iterate in both directions
    maximumX:int = 0
    maximumY:int = 0
    for item in puzzle_list:
        # if current item has a larger x or y, update the respective counter
        if item.x > maximumX:
            maximumX = item.x

        if item.y > maximumY:
            maximumY = item.y

    print("full image dimensions are "+str(maximumX)+" width by "+str(maximumY)+" height")

    # now we have those, we know how long the loops will iterate
    # we will go row by row, beginning with x0, y0 and going to maximumX,y0
    # then increment the y by 1, do the same for x from 0 to maximumX
    # end point will be maximumX, maximumY
    final_message:str = ''

    for current_y in range(maximumY+1):
        for current_x in range(maximumX+1):
            # try to find an entry in the puzzle_list data for the current cell
            # once found, add it to the final message string
            print("searching for piece with x="+str(current_x)+",y="+str(current_y))
            pieceFound = False
            for piece in puzzle_list:
                if current_x == piece.x and current_y == piece.y:
                    final_message = final_message+piece.text
                    # then remove it from our set of puzzle pieces
                    puzzle_list.remove(piece)
                    pieceFound = True

            # checkpoint: here is where we have checked every puzzle piece
            # if no piece was found for the current cell, enter a space
            if(not pieceFound):
                final_message = final_message+" "
            # increment the current x value after we either find a piece or not
            current_x = current_x+1
        print("found the end of this row")
        # add a newline and continue with the next row
        final_message = final_message + "\n"


    print(final_message)

# here is the url we need to get info from
url = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"

# call the function that does it all
decode_message(url)