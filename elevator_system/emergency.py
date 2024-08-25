import logging
from elevator_system.algorithm import SCANAlgorithm
from elevator_system.elevator_enums import Direction

class EmergencyHandler:
    def __init__(self, algorithm: SCANAlgorithm):
        self.algorithm = algorithm

    def handle_fire_alarm(self):
        logging.warning("Fire alarm activated! Initiating emergency procedures.")
        for elevator_id, state in self.algorithm.elevator_states.items():
            state.direction = Direction.IDLE  # Stop the elevator
            self.algorithm._move_elevator(elevator_id)  # Move to the nearest floor
            self.open_doors(elevator_id)  # Open doors to allow passengers to exit

    def handle_power_outage(self):
        logging.warning("Power outage detected! Activating backup systems.")
        for elevator_id, state in self.algorithm.elevator_states.items():
            state.direction = Direction.IDLE  # Stop the elevator
            self.algorithm._move_elevator(elevator_id)  # Move to the nearest floor
            self.open_doors(elevator_id)  # Open doors to allow passengers to exit

    def open_doors(self, elevator_id: int):
        logging.info(f"Opening doors for Elevator {elevator_id}.")
        # Logic to open the elevator doors
        # This could involve calling a method on the ElevatorCar class
        # Example: self.algorithm.elevator_states[elevator_id].door.open()
        # Assuming you have a method in your ElevatorCar class to open the door
        # self.algorithm.elevator_states[elevator_id].door.open()