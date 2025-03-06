"""
config.py

Configuration file for CARLA settings, camera parameters, and YOLO model path.
This file centralizes all configurable parameters for ease of modification.
"""

import sys
import os
import glob
import time

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass



# === Add Required Paths ===
sys.path.append(r'C:\Users\karki\AppData\Local\Programs\Python\Python37\Lib\site-packages\carla-0.9.10-py3.7-win-amd64.egg')
sys.path.append(r'C:\carla\Build\UE4Carla\0.9.10-dirty\WindowsNoEditor\PythonAPI')
sys.path.append(r'C:\carla\Build\UE4Carla\0.9.10-dirty\WindowsNoEditor\PythonAPI\examples')

import carla 


# === CARLA Connection Settings ===
CARLA_HOST = 'localhost'
CARLA_PORT = 2000
CARLA_TIMEOUT = 10.0  # Timeout in seconds

# === CARLA Environment Settings ===
CARLA_MAP = "/Game/Carla/Maps/Town01"  # Change this to any available CARLA map
CARLA_WEATHER_PRESET = 'ClearNoon'  # Options: ClearNoon, CloudyNoon, WetNoon, etc.

# Vehicle Spawn Settings
CARLA_SPAWN_POINT = carla.Transform(carla.Location(x=2.0, y=0.0, z=1.0),carla.Rotation(yaw=180.0))

# === Camera Settings ===
CAMERA_POS_Z = 1.6  # Height of the camera from the ground (meters)
CAMERA_POS_X = 0.9  # Forward offset of the camera (meters)

IMAGE_WIDTH = 854  # Camera image width 1280,845
IMAGE_HEIGHT = 480  # Camera image height 720,480

# === YOLO Model Settings ===
YOLO_MODEL_PATH = 'best.pt'  # Path to the YOLOv8 model

# === Debugging Helper ===
def print_config():
    """Prints all configuration settings for debugging purposes."""
    print(f"CARLA_HOST: {CARLA_HOST}")
    print(f"CARLA_PORT: {CARLA_PORT}")
    print(f"CARLA_TIMEOUT: {CARLA_TIMEOUT} sec")
    print(f"CARLA_MAP: {CARLA_MAP}")
    print(f"CARLA_WEATHER_PRESET: {CARLA_WEATHER_PRESET}")
    print(f"CARLA_SPAWN_POINT: {CARLA_SPAWN_POINT}")
    print(f"CAMERA_POS_Z: {CAMERA_POS_Z} meters")
    print(f"CAMERA_POS_X: {CAMERA_POS_X} meters")
    print(f"IMAGE_WIDTH: {IMAGE_WIDTH} px")
    print(f"IMAGE_HEIGHT: {IMAGE_HEIGHT} px")
    print(f"YOLO_MODEL_PATH: {YOLO_MODEL_PATH}")

if __name__ == "__main__":
    print_config()
