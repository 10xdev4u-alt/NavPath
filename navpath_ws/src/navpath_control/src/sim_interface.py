import rclpy
from rclpy.node import Node

class SimInterface(Node):
    def __init__(self):
        super().__init__('sim_interface')
        # Gazebo/Webots integration for control loop
