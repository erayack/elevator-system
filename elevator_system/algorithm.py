# algorithm.py

from elevator_system.elevator_enums import Direction, ElevatorState, Enum
from typing import List, Dict


class Direction(Enum):
    UP = 1
    DOWN = 2
    IDLE = 3

class ElevatorState:
    def __init__(self, current_floor: int, direction: Direction):
        self._current_floor = current_floor
        self._direction = direction

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
        if floor not in self.requests:
            self.requests[floor] = []
        self.requests[floor].append(destination)

    def process_requests(self):
        for elevator_id, state in self.elevator_states.items():
            if state.direction == Direction.IDLE:
                nearest_floor = self._find_nearest_floor_with_request(state.current_floor)
                if nearest_floor is not None:
                    if nearest_floor > state.current_floor:
                        state.direction = Direction.UP
                    elif nearest_floor < state.current_floor:
                        state.direction = Direction.DOWN
            
            self._move_elevator(elevator_id)

    def _find_nearest_floor_with_request(self, current_floor: int) -> int:
        floors_with_requests = list(self.requests.keys())
        if not floors_with_requests:
            return None
        return min(floors_with_requests, key=lambda x: abs(x - current_floor))

    def _move_elevator(self, elevator_id: int):
    state = self.elevator_states[elevator_id]
    print(f"Before move: Elevator {elevator_id} at floor {state.current_floor}, direction {state.direction}")
    
    if state.direction == Direction.UP:
        state.current_floor += 1
        print(f"After increment: Elevator {elevator_id} at floor {state.current_floor}")
    elif state.direction == Direction.DOWN:
        state.current_floor -= 1
    
    # Ensure the elevator stays within the building's floor range
    state.current_floor = max(1, min(state.current_floor, self.num_floors))
    
    print(f"After move: Elevator {elevator_id} at floor {state.current_floor}, direction {state.direction}")
    self._handle_floor_requests(elevator_id, state.current_floor)

    def _handle_floor_requests(self, elevator_id: int, floor: int):
        if floor in self.requests:
            destinations = self.requests[floor]
            for dest in destinations:
                print(f"Elevator {elevator_id} picks up passenger at floor {floor} going to floor {dest}")
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
        self.__state = DoorState.OPEN
        print("Door is now open")

    def close_door(self):
        self.__state = DoorState.CLOSED
        print("Door is now closed")

class Display:
    def __init__(self):
        self.__floor = 1

    def update(self, floor: int):
        self.__floor = floor
        self.show_elevator_display()

    def show_elevator_display(self):
        print(f"Current Floor: {self.__floor}")

class ElevatorButton:
    def __init__(self, floor: int, elevator_system: ElevatorSystem):
        self.__floor = floor
        self.__elevator_system = elevator_system
        self.__is_pressed = False

    def press_down(self):
        self.__is_pressed = True
        self.__elevator_system.dest_floor(self.__floor)

    def unpress(self):
        self.__is_pressed = False