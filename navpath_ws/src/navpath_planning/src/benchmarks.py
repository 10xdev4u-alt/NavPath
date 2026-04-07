import rclpy
from rclpy.node import Node

class PlanningBenchmarks(Node):
    def __init__(self):
        super().__init__('planning_benchmarks')
        # Success rate and planning time metrics
