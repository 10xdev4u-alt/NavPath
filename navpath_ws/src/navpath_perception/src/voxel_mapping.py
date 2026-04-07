import rclpy
from rclpy.node import Node

class VoxelMapping(Node):
    def __init__(self):
        super().__init__('voxel_mapping')
        # Octomap integration for 3D mapping
