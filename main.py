from config import *
import cv2
import numpy as np
from config import IMAGE_WIDTH, IMAGE_HEIGHT
from carla_utils.carla_manager import CarlaManager
from carla_utils.sensor_manager import SensorManager
from yolo_utils.yolo_manager import YoloManager
from utils.helpers import process_image

def main():
    # Initialize managers
    carla_manager = CarlaManager()

      # Change the map
    carla_manager.world = carla_manager.client.load_world(CARLA_MAP)

    vehicle = carla_manager.spawn_vehicle()
    sensor_manager = SensorManager(carla_manager.world, vehicle)
    yolo_manager = YoloManager()

    # Spawn RGB camera
    camera_rgb = sensor_manager.spawn_camera('rgb')
    camera_depth = sensor_manager.spawn_camera('depth')

    # Data dictionary to store images and detections
    camera_data = {'rgb_image': np.zeros((IMAGE_WIDTH, IMAGE_HEIGHT, 4)),
                   'detections': None}

    # Callback function for RGB camera
    def rgb_callback(image):
        camera_data['rgb_image'] = process_image(image)
        camera_data['detections'] = yolo_manager.detect_objects(camera_data['rgb_image'][:, :, :3])


        # Callback function for Depth camera

    def depth_callback(image):
        image.convert(carla.ColorConverter.Depth)
        camera_data['depth_image'] = process_image(image)[:, :, 0] * 1000 / 255.0  # Convert to meters

    # Start listening to RGB camera
    camera_rgb.listen(lambda image: rgb_callback(image))
    camera_depth.listen(lambda image: depth_callback(image))

    # Main loop
    try:
        while True:
            # Ensure image has the correct shape and type
            rgb_image = camera_data['rgb_image'][:, :, :3].copy().astype(np.uint8)

            if camera_data['detections'] is not None:
                for detection in camera_data['detections']:
                    x1, y1, x2, y2, conf, cls = detection
                    center_x, center_y = int((x1 + x2) / 2), int((y1 + y2) / 2)
                    distance = camera_data['depth_image'][center_y, center_x]

                    cv2.rectangle(rgb_image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 15), 2)
                    cv2.putText(rgb_image, f'{yolo_manager.model.names[int(cls)]} {conf:.2f} Dist: {distance:.2f}m', 
                                (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            cv2.imshow('RGB Detection', rgb_image)

            # Break loop if user presses 'q'
            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        # Cleanup
        cv2.destroyAllWindows()
        camera_rgb.stop()
        camera_depth.stop()
        carla_manager.cleanup()

if __name__ == '__main__':
    main()
