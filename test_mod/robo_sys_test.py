from sys_module.environment import create_environment
from sys_module.robo_sys import RobotSystem


def test_system_run():
    grid = create_environment()
    system = RobotSystem(grid)

    system.run()

    agent = system.agent

    assert agent.moves >= 0
    assert agent.collected >= 0

    print("System run test passed.")