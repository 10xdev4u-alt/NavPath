import rclpy
from rclpy.node import Node

class Map2D(Node):
    def __init__(self):
        super().__init__('map_2d')
        # Grid-based topological map
