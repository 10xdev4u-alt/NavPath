import rclpy
from rclpy.node import Node

class SemanticMapping(Node):
    def __init__(self):
        super().__init__('semantic_mapping')
        # Object-level SLAM landmarks
