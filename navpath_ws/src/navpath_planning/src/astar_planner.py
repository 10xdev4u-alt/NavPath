import rclpy
from rclpy.node import Node

class AStarPlanner(Node):
    def __init__(self):
        super().__init__('astar_planner')
        # Grid-based A* pathfinding
