from sys_module.environment import create_environment
from policy_module.policy import RobotPolicy


def test_agent_initialization():
    grid = create_environment()
    agent = RobotPolicy(grid)

    assert 0 <= agent.row < agent.size
    assert 0 <= agent.col < agent.size

    print("Agent initialization test passed.")


def test_agent_movement():
    grid = create_environment()
    agent = RobotPolicy(grid)

    old_position = (agent.row, agent.col)

    agent.random_move()

    new_position = (agent.row, agent.col)

    assert new_position != old_position or agent.moves == 0

    print("Agent movement test passed.")


def test_collect():
    grid = create_environment()
    agent = RobotPolicy(grid)

    # Force waste
    agent.grid[agent.row][agent.col] = -1

    agent.collect()

    assert agent.collected == 1

    print("Collect function test passed.")