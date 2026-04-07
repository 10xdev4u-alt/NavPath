import rclpy
from rclpy.node import Node

class Explorer(Node):
    def __init__(self):
        super().__init__('explorer')
        # Frontier-based information gain maximization
