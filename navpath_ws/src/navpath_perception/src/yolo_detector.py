import rclpy
from rclpy.node import Node

class YOLODetector(Node):
    def __init__(self):
        super().__init__('yolo_detector')
        # YOLOv8 integration for object detection
