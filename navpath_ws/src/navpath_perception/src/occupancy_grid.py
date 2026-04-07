import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid

class OccupancyGridGenerator(Node):
    def __init__(self):
        super().__init__('occupancy_grid_generator')
        self.publisher = self.create_publisher(OccupancyGrid, 'map', 10)
