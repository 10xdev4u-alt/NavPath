import rclpy
from rclpy.node import Node

class DWAPlanner(Node):
    def __init__(self):
        super().__init__('dwa_planner')
        # Dynamic Window Approach velocity sampling
