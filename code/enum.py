import enum


# We have three enumerations used in the system i.e., ElevatorState, Direction and DoorState. 
# Definition of enumerations used in elevator system


class ElevatorState(enum.Enum):
	IDLE = 1
	UP = 2
	DOWN = 3

class Direction(enum.Enum):
	UP = 1
	DOWN = 2

class DoorState(enum.Enum):
	OPEN = 1
	CLOSE = 2