# ElevatorCar class contains the instance of Door, Display, and ElevatorPanel.

class ElevatorCar:
    def __init__(self, id, door, state, display, panel):
        self.__id = id
        self.__door = door
        self.__state = state
        self.__display = display
        self.__panel = panel

    def move(self, direction):
        # Update the elevator's state to moving
        self.__state = "moving"
        # Update the display to show the current direction
        self.__display.update(f"Moving {direction}")
        print(f"Elevator {self.__id} is moving {direction}")

    def stop(self, floor):
        # Update the elevator's state to stopped
        self.__state = "stopped"
        # Update the display to show the current floor
        self.__display.update(f"Floor {floor}")
        # Open the door
        self.__door.open()
        print(f"Elevator {self.__id} has stopped at floor {floor}")