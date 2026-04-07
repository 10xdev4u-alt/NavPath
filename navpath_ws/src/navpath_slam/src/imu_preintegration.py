import rclpy
from rclpy.node import Node

class IMUPreintegration(Node):
    def __init__(self):
        super().__init__('imu_preintegration')
        # High-frequency bias estimation
