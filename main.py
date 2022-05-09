import time

def main():
    grid = createGrid(50,50)
    lifesAray=[[0,2],[2,28],[15,18],[38,0],[21,42]] # a changer en random
    initLifesCellules(grid,lifesAray)
    neighboursGrid = createNeibhoursGrid(grid,lifesAray)
    while True:
        print(grid)
        time.sleep(0.5)
        grid = play(grid,neighboursGrid)


def createGrid(height,width): #creation avec tout 0 selon les dimensions
    grid = []
    for i in range(height):
        line = []
        for j in range(width):
            line.append(0)
        grid.append(line)
    return grid

def initLifesCellules(grid,lifesAray): #a partir dune liste on creer nos cellules vivantes
    for coordonate in lifesAray:
        grid[coordonate[0]][coordonate[1]] = 1
    return grid

def createNeibhoursGrid(grid,lifesArray): #a reecrire et verifier les mikre katse et aussi si c'est len ou len-1
    #creation dune nouvelle grid des voisins vide auy debut
    neighbourGrid = []
    for i in range(len(grid)-1):
        line = []
        for j in range(len(grid[i])-1):
            line.append(0)
        neighbourGrid.append(line)

    #puis ajoute +1 dans tous les cas de figure possibles
    for coordonate in lifesArray:
        x=coordonate[0]
        y=coordonate[1]

        if (coordonate[0]==0): #ligne du haut
            if(coordonate[1]==0): #coin gauche
                neighbourGrid[coordonate[0]][coordonate[1]+1] += 1
                neighbourGrid[coordonate[0]+1][coordonate[1]] += 1
                neighbourGrid[coordonate[0]+1][coordonate[1]+1] += 1
            elif(coordonate[1]==len(grid[i])-1): #coin droit
                neighbourGrid[coordonate[0]][coordonate[1] - 1] += 1
                neighbourGrid[coordonate[0]+1][coordonate[1]] += 1
                neighbourGrid[coordonate[0]+1][coordonate[1]-1] += 1
            else: #barre du haut sauf coins
                neighbourGrid[coordonate[0]][coordonate[1]-1] += 1 #gauche
                neighbourGrid[coordonate[0]][coordonate[1]+1] += 1 #droite
                neighbourGrid[coordonate[0]+1][coordonate[1]-1] += 1 #en bas gauche
                neighbourGrid[coordonate[0]+1][coordonate[1]] += 1 #en bas
                neighbourGrid[coordonate[0]+1][coordonate[1]+1] += 1 #en bas droite

        elif(coordonate[0]==len(grid)-1): #ligne du bas
            if(coordonate[1]==0): #coin gauche
                neighbourGrid[coordonate[0]-1][coordonate[1]] += 1 #au dessus
                neighbourGrid[coordonate[0]][coordonate[1]+1] += 1 #droite
                neighbourGrid[coordonate[0]-1][coordonate[1]+1] += 1 #en haut a droite
            elif(coordonate[1]==len(grid[i])-1): #coin droit
                neighbourGrid[coordonate[0]-1][coordonate[1]] += 1 #au dessus
                neighbourGrid[coordonate[0]][coordonate[1]-1] += 1 #gauche
                neighbourGrid[coordonate[0]-1][coordonate[1]-1] += 1#en haut a gauche
            else: #barre du haut sauf coins
                neighbourGrid[coordonate[0]][coordonate[1]-1] += 1 #gauche
                neighbourGrid[coordonate[0]][coordonate[1]+1] += 1 #droite
                neighbourGrid[coordonate[0]-1][coordonate[1]-1] += 1 #en haut gauche
                neighbourGrid[coordonate[0]-1][coordonate[1]] += 1 #en haut
                neighbourGrid[coordonate[0]-1][coordonate[1]+1] += 1 #en haut droite

        elif (coordonate[1]==0): #colomne de gauche
            neighbourGrid[coordonate[0]-1][coordonate[1]] += 1  # haut
            neighbourGrid[coordonate[0]+1][coordonate[1]] += 1  # bas
            neighbourGrid[coordonate[0]][coordonate[1] + 1] += 1  # droite
            neighbourGrid[coordonate[0]-1][coordonate[1] + 1] += 1  # haut droite
            neighbourGrid[coordonate[0]+1][coordonate[1] + 1] += 1  # bas droite

        elif (coordonate[1]==0): #colomne de droite
            neighbourGrid[coordonate[0]-1][coordonate[1]] += 1  # haut
            neighbourGrid[coordonate[0]+1][coordonate[1]] += 1  # bas
            neighbourGrid[coordonate[0]][coordonate[1] - 1] += 1  # gauche
            neighbourGrid[coordonate[0]-1][coordonate[1] - 1] += 1  # haut gauche
            neighbourGrid[coordonate[0]+1][coordonate[1] - 1] += 1  # bas gauche

        else: #centre de la matrix
            neighbourGrid[coordonate[0] - 1][coordonate[1]] += 1  # haut
            neighbourGrid[coordonate[0] + 1][coordonate[1]] += 1  # bas
            neighbourGrid[coordonate[0]][coordonate[1] - 1] += 1  # gauche
            neighbourGrid[coordonate[0]][coordonate[1] + 1] += 1  # droite
            neighbourGrid[coordonate[0] - 1][coordonate[1] - 1] += 1  # haut gauche
            neighbourGrid[coordonate[0] - 1][coordonate[1] + 1] += 1  # haut droite
            neighbourGrid[coordonate[0] + 1][coordonate[1] - 1] += 1  # bas gauche
            neighbourGrid[coordonate[0] + 1][coordonate[1] + 1] += 1  # bas droite

    return neighbourGrid

def play(grid,neighboursGrid):
#je suis vivant et jai 2 ou 3 voisin ssi je vi encore
#je suis mort alors je revis si jai exactement 3 voisins
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j]==0): #cellule (i,j) morte
                if (neighboursGrid[i][j]==3): #et possede 3 voisins
                    grid[i][j] = 1 #RESURECTION
            else:  #cellule (i,j) vivante
                if(neighboursGrid[i][j] != 2 & neighboursGrid[i][j]!= 3 ): #et possede pas 2 ou 3 voisins
                    grid[i][j] = 1  # MORT

    return grid

def __str__(grid):
    result = ""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            result += str(grid[i][j])
        result += "\n"


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