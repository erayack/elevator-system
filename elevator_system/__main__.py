from elevator_system.system import ElevatorSystem
from elevator_system.building import Building  

if __name__ == "__main__":
    building = Building()  # Assuming you have a Building class
    elevator_system = ElevatorSystem(building)

    # Simulate a fire alarm
    elevator_system.handle_emergency("fire")

    # Simulate a power outage
    elevator_system.handle_emergency("power_outage")

    # Set elevator 0 to maintenance mode
    elevator_system.set_elevator_maintenance(0, True)

    # Simulate a request (this will not dispatch elevator 0)
    elevator_system.dispatcher(3)

    # Set elevator 0 back to normal operation
    elevator_system.set_elevator_maintenance(0, False)

    # User input for elevator requests
    while True:
        try:
            floor = int(input("Enter the floor number to request the elevator (or -1 to exit): "))
            if floor == -1:
                break
            elevator_system.dispatcher(floor)  # Assuming this method exists
        except ValueError:
            print("Please enter a valid floor number.")