FROM osrf/ros:humble-desktop-full
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y     python3-pip     python3-colcon-common-extensions     git     && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip3 install -r requirements.txt
WORKDIR /navpath_ws
