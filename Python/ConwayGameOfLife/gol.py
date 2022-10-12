# creating the grid

# displaying the grid

# every half second, generate updated grid:
# for each cell:
#   die if 0-1 neighbors or 4+ neighbors (overpopulation)
#   live if 2-3 neighbors
#   become alive if dead but has 3 neighbors


# iteration 1: using just print statements on a grid
#□ dead square
#■ live square

import threading
import tkinter as tk
import time
# create table

table = []
# set dimensions
tableSize = 25

# add a new table for each tableSize
for i in range(tableSize):
    table.append([])

#adds tableSize count of dead squares for each row in the table
for i in range(tableSize):
    for j in range(tableSize):
        table[i].append('□')

#iterates every square in the 2d array, in this case printing it
""" for i in range(len(table[i])):
    for j in range(len(table[i])):
        print(table[i][j], end=" ")
    print('\n') """
def swapColor(i, j):
    if(table[i][j] == '□'):
        table[i][j] = '■'
    else:
        table[i][j] = '□'
    
# gui: full size is tableSize*10 x tableSize*10, scaled
# each square should be 1/tableSize of the total window size - in this case tableSize*0.1
window = tk.Tk()
window.grid_rowconfigure(i, minsize=tableSize)
window.grid_columnconfigure(j, minsize=tableSize)
window.geometry(str(tableSize)+'x'+str(tableSize))

for i in range(len(table[i])):
    for j in range(len(table[i])):
        frame=tk.Frame(
        master=window,
        borderwidth=0.5,
        )
        
        #conditional for button color
        if(table[i][j] == '□'):
            bGd="black"
        else:
            bGd="white"
        frame.grid_propagate(False)
        frame.grid(row=i, column=j)
        button = tk.Button(
            master=frame,
            bg = bGd,
            fg = "white",
            relief=tk.FLAT,
            command=swapColor(i,j)
        )
        button.pack()

window.mainloop()
window
waiting = True
lastTime = time.time()

while waiting:
    timeDelta = time.time() - lastTime
    if timeDelta > 1:
        lastTime = time.time()
        print('')