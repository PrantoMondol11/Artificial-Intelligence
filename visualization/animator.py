import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def animate(grid_history, path, agent):

    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()

        grid = np.array(grid_history[frame])

        # robot position
        r, c = path[frame]
        grid[r][c] = 5  # robot

        ax.imshow(grid)

        # 🔥 Show counters
        ax.set_title(
            f"Step: {frame} | Collected: {agent.collected} | "
            f"Moves: {agent.moves} | Avoided: {agent.avoid_count}"
        )

        ax.set_xticks([])
        ax.set_yticks([])

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(path),
        interval=300
    )

    plt.show()