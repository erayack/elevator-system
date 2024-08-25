# simulation.py

import random
import time
from elevator_system.algorithm import SCANAlgorithm
from elevator_system.elevator_enums import Direction

class ElevatorSimulation:
    def __init__(self, num_floors: int, num_elevators: int):
        self.algorithm = SCANAlgorithm(num_floors, num_elevators)
        self.algorithm.initialize_elevators()

    def generate_random_requests(self, num_requests: int):
        for _ in range(num_requests):
            floor = random.randint(1, self.algorithm.num_floors)
            destination = random.randint(1, self.algorithm.num_floors)
            if floor != destination:  # Ensure the request is valid
                self.algorithm.add_request(floor, destination)
                print(f"Request added: Floor {floor} to {destination}")

    def run_simulation(self, num_requests: int, simulation_time: int):
        start_time = time.time()
        while time.time() - start_time < simulation_time:
            self.generate_random_requests(num_requests)
            self.algorithm.process_requests()
            time.sleep(1)  # Simulate time passing
            self.display_elevator_states()

    def display_elevator_states(self):
        for elevator_id, state in self.algorithm.elevator_states.items():
            print(f"Elevator {elevator_id}: Floor {state.current_floor}, Direction {state.direction.name}")

# Example usage
if __name__ == "__main__":
    num_floors = 10
    num_elevators = 3
    simulation = ElevatorSimulation(num_floors, num_elevators)
    simulation.run_simulation(num_requests=5, simulation_time=30)  # 5 requests every second for 30 seconds