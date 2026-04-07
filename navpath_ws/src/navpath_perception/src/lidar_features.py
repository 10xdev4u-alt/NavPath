import rclpy
from rclpy.node import Node

class LidarFeatureExtractor(Node):
    def __init__(self):
        super().__init__('lidar_feature_extractor')
        # Scan-matching corner/edge detection
