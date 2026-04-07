import rclpy
from rclpy.node import Node
from message_filters import ApproximateTimeSynchronizer, Subscriber
from sensor_msgs.msg import Image, LaserScan

class SensorSync(Node):
    def __init__(self):
        super().__init__('sensor_sync')
        self.image_sub = Subscriber(self, Image, 'image_raw')
        self.scan_sub = Subscriber(self, LaserScan, 'scan')
        self.ts = ApproximateTimeSynchronizer([self.image_sub, self.scan_sub], 10, 0.1)
        self.ts.registerCallback(self.callback)

    def callback(self, image, scan):
        self.get_logger().info('Synced sensors received')
