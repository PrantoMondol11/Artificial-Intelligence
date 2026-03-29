import random
from config import GRID_SIZE, TOTAL_WASTE, HUMAN_COUNT


def create_environment():
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Buildings
    buildings = [(2,2), (2,12), (12,2), (12,12)]
    size = 4

    for r, c in buildings:
        for i in range(r, r+size):
            for j in range(c, c+size):
                if i < GRID_SIZE and j < GRID_SIZE:
                    grid[i][j] = 1

    # Waste
    placed = 0
    while placed < TOTAL_WASTE:
        r = random.randint(0, GRID_SIZE-1)
        c = random.randint(0, GRID_SIZE-1)
        if grid[r][c] == 0:
            grid[r][c] = -1
            placed += 1

    # Humans
    placed = 0
    while placed < HUMAN_COUNT:
        r = random.randint(0, GRID_SIZE-1)
        c = random.randint(0, GRID_SIZE-1)
        if grid[r][c] == 0:
            grid[r][c] = 2
            placed += 1

    return grid