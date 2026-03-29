from sys_module.environment import create_environment
from sys_module.robo_sys import RobotSystem
from sys_module.performance import calculate_performance
from visualization.animator import animate
from config import SIMULATIONS


total_human = 0
total_avoid = 0
total_collected = 0
total_moves = 0

first_path = None
first_grid = None

for i in range(SIMULATIONS):

    grid = create_environment()
    system = RobotSystem(grid)

    system.run()

    agent = system.agent

    if i == 0:
        first_path = agent.path_positions
        first_grid = grid

    total_human += agent.human_detected
    total_avoid += agent.avoid_count
    total_collected += agent.collected
    total_moves += agent.moves


print("\n========== SUMMARY ==========\n")
print(f"Human detected : {total_human}")
print(f"Avoided        : {total_avoid}")
print(f"Collected      : {total_collected}")
print(f"Moves          : {total_moves}")

avg_score = calculate_performance(
    total_collected/SIMULATIONS,
    total_moves/SIMULATIONS
)

print(f"Average Score  : {avg_score:.2f}")


# 🎬 Animation
animate(
    system.agent.grid_history,
    system.agent.path_positions,
    system.agent
)