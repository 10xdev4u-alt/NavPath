import rclpy
from rclpy.node import Node

class DynamicMapUpdates(Node):
    def __init__(self):
        super().__init__('dynamic_map_updates')
        # Moving object removal from map
