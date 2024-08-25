# algorithm.py

from elevator_system.elevator_enums import Direction, ElevatorState, Enum, DoorState  # Added DoorState import
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Direction(Enum):
    UP = 1
    DOWN = 2
    IDLE = 3

class ElevatorState:
    def __init__(self, current_floor: int, direction: Direction):
        if current_floor < 1:
            raise ValueError("Current floor must be 1 or higher.")
        if direction not in Direction:
            raise ValueError("Invalid direction.")
        self._current_floor = current_floor
        self._direction = direction
        logging.debug(f"ElevatorState initialized at floor {current_floor} with direction {direction}")

    @property
    def current_floor(self):
        return self._current_floor

    @current_floor.setter
    def current_floor(self, value):
        self._current_floor = value

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

class SCANAlgorithm:
    def __init__(self, num_floors: int, num_elevators: int):
        self.num_floors = num_floors
        self.num_elevators = num_elevators
        self.elevator_states: Dict[int, ElevatorState] = {}
        self.requests: Dict[int, List[int]] = {}
        print(f"Initialized SCANAlgorithm with {num_floors} floors and {num_elevators} elevators")

    def initialize_elevators(self):
        for i in range(self.num_elevators):
            self.elevator_states[i] = ElevatorState(1, Direction.IDLE)

    def add_request(self, floor: int, destination: int):
        if floor < 1 or floor > self.num_floors:
            raise ValueError("Floor must be within valid range.")
        if destination < 1 or destination > self.num_floors:
            raise ValueError("Destination must be within valid range.")
        if floor not in self.requests:
            self.requests[floor] = []
        self.requests[floor].append(destination)

    def process_requests(self):
        for elevator_id, state in self.elevator_states.items():
            logging.debug(f"Processing requests for Elevator {elevator_id} at floor {state.current_floor}")
            if state.direction == Direction.IDLE:
                nearest_floor = self._find_nearest_floor_with_request(state.current_floor)
                if nearest_floor is not None:
                    if nearest_floor > state.current_floor:
                        state.direction = Direction.UP
                    elif nearest_floor < state.current_floor:
                        state.direction = Direction.DOWN
            
            self._move_elevator(elevator_id)

    def _find_nearest_floor_with_request(self, current_floor: int) -> int:
        if current_floor < 1 or current_floor > self.num_floors:
            raise ValueError("Current floor must be within valid range.")
        floors_with_requests = list(self.requests.keys())
        if not floors_with_requests:
            return None
        return min(floors_with_requests, key=lambda x: abs(x - current_floor))

    def _move_elevator(self, elevator_id: int):
        if elevator_id not in self.elevator_states:
            raise ValueError("Invalid elevator ID.")
        state = self.elevator_states[elevator_id]
        logging.info(f"Before move: Elevator {elevator_id} at floor {state.current_floor}, direction {state.direction}")
        
        if state.direction == Direction.UP:
            if state.current_floor < self.num_floors:
                state.current_floor += 1
            else:
                state.direction = Direction.DOWN
        elif state.direction == Direction.DOWN:
            if state.current_floor > 1:
                state.current_floor -= 1
            else:
                state.direction = Direction.UP
        
        # Update the state in the dictionary
        self.elevator_states[elevator_id] = state

        logging.info(f"After move: Elevator {elevator_id} at floor {state.current_floor}, direction {state.direction}")
        logging.info(f"Elevator states: {self.elevator_states}")
        
        # Check if there are any requests at the current floor
        if state.current_floor in self.requests:
            self.requests.remove(state.current_floor)
        
        # If there are no more requests, set the elevator to IDLE
        if not self.requests:
            state.direction = Direction.IDLE

        self._handle_floor_requests(elevator_id, state.current_floor)

    def _handle_floor_requests(self, elevator_id: int, floor: int):
        if floor in self.requests:
            destinations = self.requests[floor]
            for dest in destinations:
                logging.info(f"Elevator {elevator_id} picks up passenger at floor {floor} going to floor {dest}")
            del self.requests[floor]

    def get_elevator_state(self, elevator_id: int) -> ElevatorState:
        return self.elevator_states[elevator_id]

# Integration with existing classes

class ElevatorSystem:
    def __init__(self, building):
        self.__building = building
        self.__algorithm = SCANAlgorithm(len(building.floors), len(building.elevators))
        self.__algorithm.initialize_elevators()

    def dest_floor(self, floor: int):
        if floor < 1 or floor > len(self.__building.floors):
            raise ValueError("Destination floor must be within valid range.")
        logging.info(f"Destination floor requested: {floor}")
        # This method is called when an ElevatorButton is pressed
        current_floor = self.__building.elevators[0].get_current_floor()  # Assuming we're using the first elevator
        self.__algorithm.add_request(current_floor, floor)
        self.process_requests()

    def process_requests(self):
        for elevator_id, state in self.__algorithm.elevator_states.items():
            if state.direction == Direction.IDLE:
                nearest_floor = self.__algorithm._find_nearest_floor_with_request(state.current_floor)
                if nearest_floor is not None:
                    if nearest_floor > state.current_floor:
                        state.direction = Direction.UP
                    elif nearest_floor < state.current_floor:
                        state.direction = Direction.DOWN
            
            self.__algorithm._move_elevator(elevator_id)

    def handle_arrival(self, elevator_id: int, floor: int):
        if elevator_id < 0 or elevator_id >= len(self.__building.elevators):
            raise ValueError("Invalid elevator ID.")
        if floor < 1 or floor > len(self.__building.floors):
            raise ValueError("Invalid floor number.")
        logging.info(f"Elevator {elevator_id} has arrived at floor {floor}")
        elevator_car = self.__building.elevators[elevator_id]
        elevator_car.door.open_door()
        print(f"Elevator {elevator_id} has arrived at floor {floor}")
        # Simulate passengers entering/exiting
        elevator_car.door.close_door()

class ElevatorCar:
    def __init__(self, id: int, door, display):
        self.__id = id
        self.__door = door
        self.__display = display
        self.__current_floor = 1

    def move(self, direction: Direction):
        if direction not in Direction:
            raise ValueError("Invalid direction.")
        logging.debug(f"Elevator {self.__id} moving {direction}")
        if direction == Direction.UP:
            self.__current_floor += 1
        elif direction == Direction.DOWN:
            self.__current_floor -= 1
        self.__display.update(self.__current_floor)

    def get_current_floor(self):
        return self.__current_floor

    @property
    def door(self):
        return self.__door

class Door:
    def __init__(self):
        self.__state = DoorState.CLOSED

    def open_door(self):
        if self.__state == DoorState.OPEN:
            raise RuntimeError("Door is already open.")
        self.__state = DoorState.OPEN
        logging.info("Door is now open")

    def close_door(self):
        if self.__state == DoorState.CLOSED:
            raise RuntimeError("Door is already closed.")
        self.__state = DoorState.CLOSED
        logging.info("Door is now closed")

class Display:
    def __init__(self):
        self.__floor = 1

    def update(self, floor: int):
        self.__floor = floor
        self.show_elevator_display()

    def show_elevator_display(self):
        logging.debug(f"Current Floor: {self.__floor}")

class ElevatorButton:
    def __init__(self, floor: int, elevator_system: ElevatorSystem):
        self.__floor = floor
        self.__elevator_system = elevator_system
        self.__is_pressed = False

    def press_down(self):
        logging.info(f"Button pressed for floor {self.__floor}")
        self.__is_pressed = True
        self.__elevator_system.dest_floor(self.__floor)

    def unpress(self):
        self.__is_pressed = False