import rclpy
from rclpy.node import Node

class ObstaclePredictor(Node):
    def __init__(self):
        super().__init__('obstacle_predictor')
        # Constant velocity and LSTM trajectory models
