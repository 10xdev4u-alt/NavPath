import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class CameraDriver(Node):
    def __init__(self):
        super().__init__('camera_driver')
        self.publisher = self.create_publisher(Image, 'image_raw', 10)

def main():
    rclpy.init()
    node = CameraDriver()
    rclpy.spin(node)
