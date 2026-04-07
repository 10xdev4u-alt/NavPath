import rclpy
from rclpy.node import Node

class SemanticSegmentation(Node):
    def __init__(self):
        super().__init__('semantic_segmentation')
        # SegFormer/DeepLabV3 terrain classification
