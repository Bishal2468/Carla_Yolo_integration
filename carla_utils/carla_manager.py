
from config import carla, CARLA_HOST, CARLA_PORT, CARLA_TIMEOUT

class CarlaManager:
    def __init__(self):
        self.client = carla.Client(CARLA_HOST, CARLA_PORT)
        self.client.set_timeout(CARLA_TIMEOUT)
        self.world = self.client.get_world()
        self.spawn_points = self.world.get_map().get_spawn_points()

    def spawn_vehicle(self, vehicle_filter='*model3*'):
        vehicle_bp = self.world.get_blueprint_library().filter(vehicle_filter)
        start_point = self.spawn_points[0]
        vehicle = self.world.try_spawn_actor(vehicle_bp[0], start_point)
        vehicle.set_autopilot(True)
        return vehicle

    def cleanup(self):
        for actor in self.world.get_actors().filter('*vehicle*'):
            actor.destroy()
        for sensor in self.world.get_actors().filter('*sensor*'):
            sensor.destroy()