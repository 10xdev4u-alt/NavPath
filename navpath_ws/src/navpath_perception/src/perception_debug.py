import rclpy
from rclpy.node import Node

class PerceptionDebugger(Node):
    def __init__(self):
        super().__init__('perception_debug')
        # Visualization markers for objects and paths
