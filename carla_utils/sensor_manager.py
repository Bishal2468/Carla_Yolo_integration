
from config import carla, CAMERA_POS_Z, CAMERA_POS_X, IMAGE_WIDTH, IMAGE_HEIGHT

class SensorManager:
    def __init__(self, world, vehicle):
        self.world = world
        self.vehicle = vehicle

    def spawn_camera(self, camera_type='rgb'):
        camera_bp = self.world.get_blueprint_library().find(f'sensor.camera.{camera_type}')
        camera_bp.set_attribute('image_size_x', str(IMAGE_WIDTH))
        camera_bp.set_attribute('image_size_y', str(IMAGE_HEIGHT))
        camera_init_trans = carla.Transform(carla.Location(z=CAMERA_POS_Z, x=CAMERA_POS_X))
        camera = self.world.spawn_actor(camera_bp, camera_init_trans, attach_to=self.vehicle)
        return camera