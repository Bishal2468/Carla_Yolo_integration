import sys
import os
sys.path.append(r'C:\Users\karki\AppData\Local\Programs\Python\Python37\Lib\site-packages\carla-0.9.10-py3.7-win-amd64.egg')

import carla
# CARLA settings
CARLA_HOST = 'localhost'
CARLA_PORT = 2000
CARLA_TIMEOUT = 10.0

CARLA_MAP = "/Game/Carla/Maps/Town04"  # Change this to any available CARLA map
CARLA_WEATHER_PRESET = 'ClearNoon'
CARLA_SPAWN_POINT = carla.Transform(carla.Location(x=2.0, y=0.0, z=1.0), carla.Rotation(yaw=180.0))


# Camera settings
CAMERA_POS_Z = 1.6  # Height of the camera
CAMERA_POS_X = 0.9  # Forward offset of the camera
IMAGE_WIDTH = 640
IMAGE_HEIGHT = 360

# YOLO settings
YOLO_MODEL_PATH = 'yolov8n.pt'