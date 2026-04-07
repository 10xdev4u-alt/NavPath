import rclpy
from rclpy.node import Node

class DijkstraPlanner(Node):
    def __init__(self):
        super().__init__('dijkstra_planner')
        # Uniform cost search for multi-goal support
