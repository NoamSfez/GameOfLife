#main function that initialize the game and depending on the grid’s state, will stop when there are no more living cells
def main(height,width,lifesList):
    #initialization of the game with grid size and living cells
    grid = init(height,width,lifesList)
    #calculation of a grid corresponding to the number of neighbors for each cell
    neighborsGrid = createNeighborsGrid(grid)
    #as long as there are still living cells we play a turn
    while isLivingCells(grid):
        neighborsGrid =turn(grid,neighborsGrid)

#return True if there is at least one live cell
def isLivingCells(grid):
    bool = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                bool=True

    # last print with only zeros
    if (bool==False):
        result = ""
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                result += str(grid[i][j])
            result += "\n"
        print(result)
    return bool

#create a binary grid of size (height * width) with zero for dead cell and one for live cell
def init(height,width,livesList):

    # create a grid of size height * width with only zeros
    def initEmptyGrid(height, width):
        grid = []
        for i in range(height):
            line = []
            for j in range(width):
                line.append(0)
            grid.append(line)
        return grid

    # add one for all lives cells received from livesList
    def initLifesCellules(grid, livesList):
        for coordinate in livesList:
            x = coordinate[0]
            y = coordinate[1]
            grid[x][y] = 1
        return grid

    zerosGrid = initEmptyGrid(height, width)
    return initLifesCellules(zerosGrid,livesList)

#receive a grid and return his neighbors' grid
def createNeighborsGrid(grid):

    # return a list of lives cells in a specific grid
    def fromGridToLivesList(grid):
        livesList = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 1):
                    livesList.append([i, j]) #add the pair of coordinate [i, j]
        return livesList

    # return a zero neighbors' grid in the same size of grid
    def initEmptyNeighborsGrid(grid):
        neighborsGrid = []
        for i in range(len(grid)):
            line = []
            for j in range(len(grid[i])):
                line.append(0) #add only zeros on a specific line
            neighborsGrid.append(line) #add all zeros lines
        return neighborsGrid

    # receive an empty neighbors' grid and return the specific number of neighbor for each cell
    def addNeighbors(neighborsGrid, livesList):
        for coordinate in livesList:
            x = coordinate[0]
            y = coordinate[1]

            #we are passing on all lives cells to add it on his neighbors' cells, according to his position in the grid
            if ((len(neighborsGrid) == 1) & (len(neighborsGrid[0]) == 1)): # if the grid is on the forms [[x]]
                break

            elif (len(neighborsGrid) == 1):  # if the grid is on the forms [[x,x,x,x,x,x,x,x,x,x]]
                if ((y == 0)):  # left corner
                    neighborsGrid[x][y + 1] += 1  # right cell
                elif (y == len(grid[0])):  # right corner
                    neighborsGrid[x][y - 1] += 1  # left cell
                else:  # between the two corners
                    neighborsGrid[x][y + 1] += 1  # right cell
                    neighborsGrid[x][y - 1] += 1  # left cell

            elif (len(neighborsGrid[0]) == 1):  # if the grid is on the forms [[x][x][x][x][x][x][x]]
                if ((x == 0)):  # top corner
                    neighborsGrid[x + 1][y] += 1 # bottom cell
                elif (x == len(grid[0])):  # bottom corner
                    neighborsGrid[x - 1][y] += 1 # up cell
                else:  # between the two corners
                    neighborsGrid[x + 1][y] += 1 # bottom cell
                    neighborsGrid[x - 1][y] += 1 # up cell

            elif (x == 0):  # grid top row
                if (y == 0):  # top left corner
                    neighborsGrid[x][y + 1] += 1 # right cell
                    neighborsGrid[x + 1][y] += 1 # bottom cell
                    neighborsGrid[x + 1][y + 1] += 1# bottom right cell
                elif (y == len(grid[0])):  # top right corner
                    neighborsGrid[x][y - 1] += 1 # left cell
                    neighborsGrid[x + 1][y] += 1 # bottom cell
                    neighborsGrid[x + 1][y - 1] += 1 # bottom left cell
                else:  # between the top two corners
                    neighborsGrid[x][y - 1] += 1  # left cell
                    neighborsGrid[x][y + 1] += 1  # right cell
                    neighborsGrid[x + 1][y - 1] += 1  # bottom left cell
                    neighborsGrid[x + 1][y] += 1  # bottom cell
                    neighborsGrid[x + 1][y + 1] += 1  # bottom right cell

            elif (x == len(grid) - 1):  # grid bottom row
                if (y == 0):  # bottom left corner
                    neighborsGrid[x - 1][y] += 1  # up cell
                    neighborsGrid[x][y + 1] += 1  # right cell
                    neighborsGrid[x - 1][y + 1] += 1  # up right cell
                elif (y == len(grid[0])):  # bottom right corner
                    neighborsGrid[x - 1][y] += 1  # up cell
                    neighborsGrid[x][y - 1] += 1  # left cell
                    neighborsGrid[x - 1][y - 1] += 1  # up left cell
                else:  # between the bottom two corners
                    neighborsGrid[x][y - 1] += 1  # left cell
                    neighborsGrid[x][y + 1] += 1  # right cell
                    neighborsGrid[x - 1][y - 1] += 1  # up left cell
                    neighborsGrid[x - 1][y] += 1  # up cell
                    neighborsGrid[x - 1][y + 1] += 1  # up right cell

            elif (y == 0):  # grid left column
                neighborsGrid[x - 1][y] += 1  # up cell
                neighborsGrid[x + 1][y] += 1  # bottom cell
                neighborsGrid[x][y + 1] += 1  # right cell
                neighborsGrid[x - 1][y + 1] += 1  # up right cell
                neighborsGrid[x + 1][y + 1] += 1  # bottom right cell

            elif (y == 0):  # grid right column
                neighborsGrid[x - 1][y] += 1  # up cell
                neighborsGrid[x + 1][y] += 1  # bottom cell
                neighborsGrid[x][y - 1] += 1  # left cell
                neighborsGrid[x - 1][y - 1] += 1  # up left cell
                neighborsGrid[x + 1][y - 1] += 1  # bottom left cell

            else:  # center of the grid
                neighborsGrid[x - 1][y] += 1  # up cell
                neighborsGrid[x + 1][y] += 1  # bottom cell
                neighborsGrid[x][y - 1] += 1  # left cell
                neighborsGrid[x][y + 1] += 1  # right cell
                neighborsGrid[x - 1][y - 1] += 1  # up left cell
                neighborsGrid[x - 1][y + 1] += 1  # up right cell
                neighborsGrid[x + 1][y - 1] += 1  # bottom left cell
                neighborsGrid[x + 1][y + 1] += 1  # bottom right cell

        return neighborsGrid

    livesList = fromGridToLivesList(grid)
    emptyNeighborsGrid = initEmptyNeighborsGrid(grid)
    return addNeighbors(emptyNeighborsGrid, livesList)

#first print the current grid, then apply the game's rules and refresh the Neighbors' grid
def turn(grid,neighborsGrid):

    #print the grid like a matrix
    def printGrid(grid):
        result = ""
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                result += str(grid[i][j])
            result += "\n"
        print(result)

    # apply game's rules:
        # if I'm dead, I must to have specific 3 neighbors to reborn
        # if I'm alive, I must to have 2 or 3 neighbors to be alive on the next turn
    def play(grid, neighborsGrid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 0):  # dead cell (i,j)
                    if (neighborsGrid[i][j] == 3):  # have 3 neighbors
                        grid[i][j] = 1  # REBORN !!
                else:  # alive cell (i,j)
                    if (neighborsGrid[i][j] == 2):  # have 2 neighbors
                        grid[i][j] = 1 # still alive
                    elif (neighborsGrid[i][j] == 3):  # have 3 neighbors
                        grid[i][j] = 1 # still alive
                    else:  # et possede pas 2 ou 3 voisins
                        grid[i][j] = 0  # dead

    printGrid(grid)
    play(grid, neighborsGrid)
    return createNeighborsGrid(grid)

print("You have to give 3 arguments to the main function: height, width and list of list of 2 integer (coordinales of the alives cells)")
print("for example use the function: ")
print("     main(5,5,[[1,2],[3,2],[2,1],[2,3],[1,1]])")
print("I add below some interesting forms from wikipedia")

# main(5,5,[[1,2],[3,2],[2,1],[2,3],[1,1]])
# main(4,4,[[1,1],[1,2],[2,1],[2,2]]) block imutable
# main(5,6,[[1,2],[1,3],[3,2],[3,3],[2,1],[2,4]]) beehive imutable
# main(5,5,[[1,2],[3,2],[2,1],[2,3],[1,1]]) boat imutable
# main(5,5,[[1,2],[3,2],[2,1],[2,3]]) tub imutable
# main(5,5,[[2,1],[2,2],[2,3]]) blinker oscilator
# main(1,50,[[0,1],[0,2],[0,3]]) line


# main(1,50,[[0,0],[0,1],[0,2]])
