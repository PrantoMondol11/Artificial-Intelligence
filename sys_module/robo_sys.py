from policy_module.policy import RobotPolicy


class RobotSystem:

    def __init__(self, grid):
        self.agent = RobotPolicy(grid)

    def run(self):
        self.agent.run()