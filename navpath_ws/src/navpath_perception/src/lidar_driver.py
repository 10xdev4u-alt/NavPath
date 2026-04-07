import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarDriver(Node):
    def __init__(self):
        super().__init__('lidar_driver')
        self.publisher = self.create_publisher(LaserScan, 'scan', 10)
        self.timer = self.create_timer(0.1, self.publish_scan)

    def publish_scan(self):
        msg = LaserScan()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'laser_frame'
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = LidarDriver()
    rclpy.spin(node)
