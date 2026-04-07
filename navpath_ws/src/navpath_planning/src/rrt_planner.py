import rclpy
from rclpy.node import Node

class RRTPlanner(Node):
    def __init__(self):
        super().__init__('rrt_planner')
        # Sampling-based kinodynamic planning
