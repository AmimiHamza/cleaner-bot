import matplotlib.pyplot as plt
import numpy as np
import time

def draw_matrix(matrix):
    nrows, ncols = len(matrix), len(matrix[0])

    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(ncols+1)-0.5)
    ax.set_yticks(np.arange(nrows+1)-0.5)
    ax.grid(True, which='both', color='black', linestyle='-', linewidth=1)
    for i in range(nrows):
        for j in range(ncols):
            if matrix[i][j] == 'AA':
                ax.add_patch(plt.Circle((j, i), 0.4, color='blue'))
            elif matrix[i][j] == 'D':
                ax.add_patch(plt.Circle((j, i), 0.4, color='red'))
            else:
                ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1, facecolor='white', edgecolor='black'))

    plt.xlim([-0.5, ncols-0.5])
    plt.ylim([-0.5, nrows-0.5])
    plt.show()

matrix = [
    [' ', ' ', ' ', 'D', ' '],
    [' ', 'AA', ' ', 'D', ' '],
    ['D', ' ', ' ', ' ', 'D'],
    [' ', ' ', 'D', 'D', ' '],
    [' ', 'D', ' ', ' ', ' '],
]

draw_matrix(matrix)
time.sleep(1)  # Delay before displaying the next plot
plt.close()  # close the plot
