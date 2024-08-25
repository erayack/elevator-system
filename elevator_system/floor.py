# In the Door class, the enumeration DoorState is used and the Floor class contains the instances of Display and HallPanel.

class Door:
    def __init__(self, state):
        self.__state = state
    
    def isOpen(self):
        # Return True if the door is open, False otherwise
        return self.__state == "open"

class Floor:
    def __init__(self, display, panel, floor_number, total_floors):
        self.__display = display
        self.__panel = panel
        self.__floor_number = floor_number
        self.__total_floors = total_floors

    def is_bottom_most(self):
        # Check if the current floor is the bottom-most floor
        return self.__floor_number == 0

    def is_top_most(self):
        # Check if the current floor is the top-most floor
        return self.__floor_number == self.__total_floors - 1