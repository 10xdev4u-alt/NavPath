#!/bin/bash
# Automated testing across multiple scenarios
for scenario in configs/*.yaml; do
  ros2 launch navpath_bringup sim.launch.py scenario:=$scenario
done
