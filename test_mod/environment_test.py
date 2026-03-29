from sys_module.environment import create_environment
from config import GRID_SIZE


def test_grid_creation():
    grid = create_environment()

    assert len(grid) == GRID_SIZE
    assert len(grid[0]) == GRID_SIZE

    print("Grid size test passed.")


def test_elements_present():
    grid = create_environment()

    waste = sum(row.count(-1) for row in grid)
    humans = sum(row.count(2) for row in grid)

    assert waste > 0
    assert humans > 0

    print("Environment elements test passed.")