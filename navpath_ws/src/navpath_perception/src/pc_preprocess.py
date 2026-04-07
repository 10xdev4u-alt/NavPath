import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2

class PCPreprocess(Node):
    def __init__(self):
        super().__init__('pc_preprocess')
        self.subscription = self.create_subscription(PointCloud2, 'cloud_in', self.listener_callback, 10)

    def listener_callback(self, msg):
        # Filtering and downsampling logic
        pass
