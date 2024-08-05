# ElevatorPanel and the HallPanel are classes which use the instance of ElevatorButton and HallButton respectively.

class ElevatorPanel:
    def __init__(self, floor_buttons, open_button, close_button):
        self.__floor_buttons = floor_buttons
        self.__open_button = open_button
        self.__close_button = close_button


class HallPanel:
    def __init__(self, up, down):
        self.__up = up
        self.__down = down