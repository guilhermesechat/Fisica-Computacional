import matplotlib.pyplot as plt
import matplotlib
import numpy as np
np.set_printoptions(threshold=np.inf)
import gif

grid_size = 200
rule = 24
time = 240

#create a grid matrix
Grid = np.array([[np.random.randint(2) for i in range(grid_size+2)] for j in range(grid_size+2)])
Grid[70][36] = 10
Grid[50][67] = 10
Grid[35][35] = 10
Grid[50][157] = 10
Grid[5][100] = 10
Grid[150][101] = 10
Grid[153][104] = 10
Grid[151][102] = 10
Grid[100][100] = 10
Grid[100][101] = 10
Grid[101][104] = 10
Grid[109][102] = 10
Grid[151][100] = 10

for i in range(grid_size+2- int(0.8*(grid_size+2))):
    for j in range(grid_size+2- int(0.7*(grid_size+2))):
        Grid[i][j] = int(np.random.choice(2, 1, p=[0.7, 0.3]))

for i in range(grid_size+2 - int(0.5*(grid_size+2)),grid_size+2):
    for j in range(grid_size+2 - int(0.5*(grid_size+2)), grid_size+2):
        Grid[i][j] = int(np.random.choice(2, 1, p=[0.7, 0.3]))


print(Grid)
#a draft matrix to be used inside the loop
newGrid = np.zeros((grid_size+2, grid_size+2))


@gif.frame
def plotca(grid_size):
    for l in range(1,grid_size+1):
        for m in range(1,grid_size+1):
    #it's a totalistic cellular automaton, so the nearest neighborhoods should be added to relate to the dictionary
            a = int(Grid[m][l]+Grid[m-1][l]+Grid[m+1][l]+Grid[m][l-1]+Grid[m][l+1]+Grid[m+1][l+1]+Grid[m-1][l-1]+Grid[m+1][l-1]+Grid[m-1][l+1])
            if Grid[m][l] == 0:
                newGrid[m][l] = 0
            elif a > 10:
                newGrid[m][l] = 10
            else:
                newGrid[m][l] = 1
    #here the draft matrix is made equal to the stanard on the be used as new in the new time loop
    Grid[:,:] = newGrid[:,:]
    
    fig, ax = plt.subplots(1,1,figsize=(10, 10))
    ax.imshow(Grid,cmap=plt.cm.tab10, interpolation='nearest')
    #fig.savefig('Nova/' + str(i) + '.png')

frames = []
for i in range(time): 
    frame = plotca(grid_size)
    frames.append(frame)

gif.save(frames, "corona.gif", duration=100)    