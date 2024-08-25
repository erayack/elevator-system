# Display class is responsible for showing the display inside and outside of the elevator cars.

class Display:
    def __init__(self, floor, capacity, direction):
        self.__floor = floor
        self.__capacity = capacity
        self.__direction = direction

    def show_elevator_display(self, current_floor, direction):
        # Display the current floor and direction of the elevator
        self.__floor = current_floor
        self.__direction = direction
        print(f"Elevator is on floor {self.__floor}, moving {self.__direction}")

    def show_hall_display(self, floor):
        # Display the status of the elevator at the specified floor
        print(f"Floor {floor}: Elevator is {'arrived' if self.__floor == floor else 'not arrived'}")