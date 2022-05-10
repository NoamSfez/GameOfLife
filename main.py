import time

def main():
    #create(4,4,[[1,1],[1,2],[2,1],[2,2]]) block imutable
    # create(5,6,[[1,2],[1,3],[3,2],[3,3],[2,1],[2,4]]) beehive imutable
    # create(5,5,[[1,2],[3,2],[2,1],[2,3],[1,1]]) boat imutable
    # create(5,5,[[1,2],[3,2],[2,1],[2,3]]) tub imutable
    #create(5,5,[[2,1],[2,2],[2,3]]) blinker oscilator

    grid = init(1,12,[[0,0]])
    neighboursGrid = createNeighborsGrid(grid)
    while checkSurvivant(grid):
        turn(grid,neighboursGrid)



def checkSurvivant(grid): #return true if ther is at least one live cellule
    bool = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                bool=True

    if (bool==False): #last print with only zeros
        result = ""
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                result += str(grid[i][j])
            result += "\n"
        print(result)
    return bool

def init(height,width,lifesList): #create a binary grid of size (height * width) with zeros for dead cellules and one for lives cellules

    def initEmptyGrid(height, width):  # create a grid of size height * width with only zeros
        grid = []
        for i in range(height):
            line = []
            for j in range(width):
                line.append(0)
            grid.append(line)
        return grid

    def initLifesCellules(grid, lifesList):  # add one for all lifes cellules received from lifesList
        for coordinate in lifesList:
            x = coordinate[0]
            y = coordinate[1]
            grid[x][y] = 1
        return grid

    zerosGrid = initEmptyGrid(height, width)
    return initLifesCellules(zerosGrid,lifesList)

def createNeighborsGrid(grid): #receive a grid and return his neighboor grid

    def fromGridToLifesList(grid):  # return a list of lives cellules in a specific grid
        lifesList = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 1):
                    lifesList.append([i, j]) #add the pair of coordinate
        return lifesList

    def initEmptyNeighbourGrid(grid):  # return a zero Neighboor Grid in the same size of grid
        neighbourGrid = []
        for i in range(len(grid)):
            line = []
            for j in range(len(grid[i])):
                line.append(0) #add only zeros on a specific line
            neighbourGrid.append(line) #add all zeros lines
        return neighbourGrid

    def addNeighboors(neighbourGrid,lifesList):  # receive an empty neighboor grid and return the specific number of neighboor for each cellule
        for coordinate in lifesList:
            x = coordinate[0]
            y = coordinate[1]
            if (x == 0):  # ligne du haut
                if (len(neighbourGrid) == 1 or len(neighbourGrid[0])==1): #forms [[x][x][x][x][x][x][x]] or [[x,x,x,x,x,x,x,x,x,x,x,x,x]]
                    break
                elif (y == 0):  # coin gauche
                    neighbourGrid[x][y + 1] += 1
                    neighbourGrid[x + 1][y] += 1
                    neighbourGrid[x + 1][y + 1] += 1
                elif (y == len(grid[0])):  # coin droit
                    neighbourGrid[x][y - 1] += 1
                    neighbourGrid[x + 1][y] += 1
                    neighbourGrid[x + 1][y - 1] += 1
                else:  # barre du haut sauf coins
                    neighbourGrid[x][y - 1] += 1  # gauche
                    neighbourGrid[x][y + 1] += 1  # droite
                    neighbourGrid[x + 1][y - 1] += 1  # en bas gauche
                    neighbourGrid[x + 1][y] += 1  # en bas
                    neighbourGrid[x + 1][y + 1] += 1  # en bas droite

            elif (x == len(grid) - 1):  # ligne du bas
                if (y == 0):  # coin gauche
                    neighbourGrid[x - 1][y] += 1  # au dessus
                    neighbourGrid[x][y + 1] += 1  # droite
                    neighbourGrid[x - 1][y + 1] += 1  # en haut a droite
                elif (y == len(grid[0])):  # coin droit
                    neighbourGrid[x - 1][y] += 1  # au dessus
                    neighbourGrid[x][y - 1] += 1  # gauche
                    neighbourGrid[x - 1][y - 1] += 1  # en haut a gauche
                else:  # barre du haut sauf coins
                    neighbourGrid[x][y - 1] += 1  # gauche
                    neighbourGrid[x][y + 1] += 1  # droite
                    neighbourGrid[x - 1][y - 1] += 1  # en haut gauche
                    neighbourGrid[x - 1][y] += 1  # en haut
                    neighbourGrid[x - 1][y + 1] += 1  # en haut droite

            elif (y == 0):  # colomne de gauche
                neighbourGrid[x - 1][y] += 1  # haut
                neighbourGrid[x + 1][y] += 1  # bas
                neighbourGrid[x][y + 1] += 1  # droite
                neighbourGrid[x - 1][y + 1] += 1  # haut droite
                neighbourGrid[x + 1][y + 1] += 1  # bas droite

            elif (y == 0):  # colomne de droite
                neighbourGrid[x - 1][y] += 1  # haut
                neighbourGrid[x + 1][y] += 1  # bas
                neighbourGrid[x][y - 1] += 1  # gauche
                neighbourGrid[x - 1][y - 1] += 1  # haut gauche
                neighbourGrid[x + 1][y - 1] += 1  # bas gauche

            else:  # centre de la matrix
                neighbourGrid[x - 1][y] += 1  # haut
                neighbourGrid[x + 1][y] += 1  # bas
                neighbourGrid[x][y - 1] += 1  # gauche
                neighbourGrid[x][y + 1] += 1  # droite
                neighbourGrid[x - 1][y - 1] += 1  # haut gauche
                neighbourGrid[x - 1][y + 1] += 1  # haut droite
                neighbourGrid[x + 1][y - 1] += 1  # bas gauche
                neighbourGrid[x + 1][y + 1] += 1  # bas droite

        return neighbourGrid

    lifesList = fromGridToLifesList(grid)
    emptyNeighboorGrid = initEmptyNeighbourGrid(grid)
    return addNeighboors(emptyNeighboorGrid,lifesList)

def turn(grid,neighboursGrid):
    def printGrid(grid):
        result = ""
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                result += str(grid[i][j])
            result += "\n"
        print(result)

    def play(grid, neighboursGrid):
        # rules:
        # je suis vivant et jai 2 ou 3 voisin ssi je vi encore
        # je suis mort alors je revis si jai exactement 3 voisins
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 0):  # cellule (i,j) morte
                    if (neighboursGrid[i][j] == 3):  # et possede 3 voisins
                        grid[i][j] = 1  # RESURECTION
                else:  # cellule (i,j) vivante
                    if (neighboursGrid[i][j] == 2):  # 2 voisins
                        grid[i][j] = 1
                    elif (neighboursGrid[i][j] == 3):  # 3 voisins
                        grid[i][j] = 1
                    else:  # et possede pas 2 ou 3 voisins
                        grid[i][j] = 0  # MORT



    printGrid(grid)
    play(grid, neighboursGrid)
    neighboursGrid = createNeighborsGrid(grid)
    time.sleep(0.5)



#[[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0]]

#01000
#01000
#01000

#[[2,1,2,0,0],[3,2,3,0,0],[2,1,2,0,0]]

#21200
#32300
#21200

#[[0,0,0,0,0],[1,1,1,0,0],[0,0,0,0,0]]

#00000
#11100
#00000

main()