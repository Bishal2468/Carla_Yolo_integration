

from ultralytics import YOLO
from config import YOLO_MODEL_PATH

class YoloManager:
    def __init__(self):
        self.model = YOLO(YOLO_MODEL_PATH)

    def detect_objects(self, image):
        results = self.model(image)
        return results[0].boxes.data.cpu().numpy()