import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class ImagePreprocess(Node):
    def __init__(self):
        super().__init__('image_preprocess')
        self.subscription = self.create_subscription(Image, 'image_raw', self.callback, 10)

    def callback(self, msg):
        # CV2 undistortion and rectification
        pass
