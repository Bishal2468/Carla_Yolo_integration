
from config import *
import carla
import random

class CarlaManager:
    def __init__(self):
        # Connect to the CARLA server
        self.client = carla.Client(CARLA_HOST, CARLA_PORT)
        self.client.set_timeout(CARLA_TIMEOUT)
        self.world = self.client.load_world(CARLA_MAP)
        self.spawn_points = self.world.get_map().get_spawn_points()
        self.vehicles = []  # List to store all spawned actors
        self.pedestrians =[]


    def spawn_vehicle(self, vehicle_filter='vehicle.tesla.model3', max_attempts=10):
        blueprint_library = self.world.get_blueprint_library()
        vehicle_bp = random.choice(blueprint_library.filter(vehicle_filter))

        attempts = 0
        while attempts < max_attempts:
            spawn_point = random.choice(self.world.get_map().get_spawn_points())
            start_point = self.spawn_points[0]
            vehicle = self.world.try_spawn_actor(vehicle_bp, spawn_point)
            try:
                if vehicle is not None:
                    vehicle.set_autopilot(True)
                    self.vehicles.append(vehicle)  # Add to the list for cleanup
                    print(f"Spawned vehicle: {vehicle.type_id} at {spawn_point.location}")
                    return vehicle
                else:
                    print(f"Attempt {attempts+1}/{max_attempts}: Failed to spawn vehicle, retrying...")

                attempts += 1
                time.sleep(0.5)  # Small delay before retrying
            except Exception as e:
                print(f"Failed to spawn vehicle: {e}")
                return None
        print("ERROR: Could not spawn vehicle after multiple attempts.")
        return None

       


    def vehicle(self, max_attempts=5):
        blueprint_library = self.world.get_blueprint_library()
        vehicle_bp = random.choice(blueprint_library.filter('vehicle.*'))
        spawn_points = self.world.get_map().get_spawn_points()
        random.shuffle(spawn_points)  # Shuffle to increase variety

        for attempt in range(max_attempts):
            if not spawn_points:
                print(" No available spawn points left.")
                return None
            
            spawn_point = spawn_points.pop(0)  # Take the first spawn point from the shuffled list
            nearby_vehicles = self.world.get_actors().filter('vehicle.*')
            
            # Check if spawn point is free
            if any(v.get_location().distance(spawn_point.location) < 3.0 for v in nearby_vehicles):
                print(f" Spawn point occupied at {spawn_point.location}, trying another...")
                continue
            
            vehicle = self.world.try_spawn_actor(vehicle_bp, spawn_point)
            if vehicle:
                print(f" Spawned vehicle: {vehicle.type_id} at {spawn_point.location}")
                return vehicle
            else:
                print(f" Attempt {attempt+1}: Failed to spawn, trying again...")

        print(" ERROR: Could not spawn vehicle after multiple attempts.")
        return None
    

      

    def spawn_multiple_vehicles(self):
        for i in range(random.randint(5, 10)):
            print(f"Spawning vehicle {i + 1}")
            self.vehicle()
            time.sleep(2.0)
            print(f"Waiting 2.0 seconds before spawning the next vehicle...")


    def cleanup(self):
        print("Destroying actors...")

        # Destroy vehicles
        for vehicle in self.vehicles:
            try:
                if vehicle.is_alive:
                    vehicle.destroy()
            except:
                print(f"Warning: Vehicle {vehicle.id} already removed.")

        # Destroy pedestrians
        for pedestrian in self.pedestrians:
            try:
                if pedestrian.is_alive:
                    pedestrian.destroy()
            except:
                print(f"Warning: Pedestrian {pedestrian.id} already removed.")

        # Destroy sensors
        for sensor in self.world.get_actors().filter('*sensor*'):
            try:
                if sensor.is_alive:
                    sensor.destroy()
            except:
                print(f"Warning: Sensor {sensor.id} already removed.")

        print("All actors destroyed.")

        


