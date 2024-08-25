# Singleton ElevatorSystem class that represents the entire system and a Building class that contains instances of Floor and ElevatorCar.

import ctypes
import logging

from elevator_system.algorithm import SCANAlgorithm, Direction

class __ElevatorSystem(type):  # Define the metaclass
    pass  # Add any necessary metaclass logic here

class ElevatorSystem(metaclass=__ElevatorSystem):
    def __init__(self, building):
        self.__building = building
        # Load the shared C library
        self.elevator_lib = ctypes.CDLL('./path/to/elevator.so')
        self.algorithm = SCANAlgorithm(len(building.floors), len(building.elevators))
        self.emergency_handler = EmergencyHandler(self.algorithm)

    def monitoring(self):
        # Monitor the status of all elevators and floors
        for elevator in self.__building.get_elevators():
            current_floor = elevator.get_current_floor()
            direction = elevator.get_direction()
            elevator.display.show_elevator_display(current_floor, direction)

    def dispatcher(self, requested_floor):
        # Dispatch the nearest elevator to the requested floor
        nearest_elevator = None
        min_distance = float('inf')

        for elevator in self.__building.get_elevators():
            if elevator.is_in_maintenance():  # Skip elevators in maintenance
                continue
            distance = abs(elevator.get_current_floor() - requested_floor)
            if distance < min_distance:
                min_distance = distance
                nearest_elevator = elevator

        if nearest_elevator:
            # Call the C function to create an elevator state
            state = self.elevator_lib.create_elevator_state(requested_floor, nearest_elevator.get_direction())
            nearest_elevator.move(requested_floor)
            print(f"Dispatched elevator {nearest_elevator.get_id()} to floor {requested_floor}")

            # Optionally, you can free the elevator state if needed
            self.elevator_lib.free_elevator_state(state)

    def handle_emergency(self, emergency_type):
        if emergency_type == "fire":
            self.emergency_handler.handle_fire_alarm()
        elif emergency_type == "power_outage":
            self.emergency_handler.handle_power_outage()

    def set_elevator_maintenance(self, elevator_id, maintenance: bool):
        elevator = self.__building.get_elevator(elevator_id)
        if elevator:
            elevator.set_maintenance_mode(maintenance)
        else:
            logging.warning(f"Elevator {elevator_id} not found.")

class __Building(object):
  __instances = None
  
  def __new__(cls):
    if cls.__instances is None:
        cls.__instances = super(__Building, cls).__new__(cls)
    return cls.__instances

class Building(metaclass=__Building):
  def __init__(self):
    self.__floor = []
    self.__elevator = []

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