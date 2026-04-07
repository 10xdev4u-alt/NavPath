import rclpy
from rclpy.node import Node

class HybridAStar(Node):
    def __init__(self):
        super().__init__('hybrid_astar')
        # Kinematic-aware planning with Reeds-Shepp curves
