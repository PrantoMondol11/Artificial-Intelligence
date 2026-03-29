import random
from collections import deque
from config import MAX_STEPS


class RobotPolicy:

    def __init__(self, grid):
        self.grid = grid
        self.size = len(grid)
        self.grid_history = []

        while True:
            self.row = random.randint(0, self.size-1)
            self.col = random.randint(0, self.size-1)
            if self.grid[self.row][self.col] == 0:
                break

        self.moves = 0
        self.collected = 0
        self.human_detected = 0
        self.avoid_count = 0
        self.path_positions = []
        self.last_position = None

    def is_valid(self, r, c):
        return 0 <= r < self.size and 0 <= c < self.size

    def bfs_nearest_object(self):
        visited = [[False]*self.size for _ in range(self.size)]
        queue = deque()
        queue.append((self.row, self.col, []))
        visited[self.row][self.col] = True

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c, path = queue.popleft()

            if self.grid[r][c] == -1:
                return path

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if self.is_valid(nr, nc) and not visited[nr][nc]:
                    if self.grid[nr][nc] != 1:
                        visited[nr][nc] = True
                        queue.append((nr, nc, path + [(nr, nc)]))

        return []

    def random_move(self):

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        path = self.bfs_nearest_object()

        if path:
            target_r, target_c = path[-1]

            directions.sort(
                key=lambda d: abs((self.row+d[0])-target_r) +
                              abs((self.col+d[1])-target_c)
            )

        for dr, dc in directions:
            nr = self.row + dr
            nc = self.col + dc

            if not self.is_valid(nr, nc):
                continue

            if (nr, nc) == self.last_position:
                continue

            if self.grid[nr][nc] == 2:
                self.human_detected += 1
                self.avoid_count += 1
                continue

            if self.grid[nr][nc] == 1:
                continue

            self.last_position = (self.row, self.col)

            self.row, self.col = nr, nc
            self.moves += 1
            self.path_positions.append((self.row, self.col))
            return

    def collect(self):
        if self.grid[self.row][self.col] == -1:
            self.grid[self.row][self.col] = 0
            self.collected += 1

    def run(self):
        import copy

        for _ in range(MAX_STEPS):

            self.random_move()
            self.collect()

            self.grid_history.append(copy.deepcopy(self.grid))