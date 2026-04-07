import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class ImuDriver(Node):
    def __init__(self):
        super().__init__('imu_driver')
        self.publisher = self.create_publisher(Imu, 'imu/data', 10)

def main():
    rclpy.init()
    node = ImuDriver()
    rclpy.spin(node)
