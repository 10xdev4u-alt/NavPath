import rclpy
from rclpy.node import Node

class TaskPlanner(Node):
    def __init__(self):
        super().__init__('task_planner')
        # Traveling salesman and priority mission queue
