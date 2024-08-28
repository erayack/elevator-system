# Designing an Elevator System

An elevator system is a system that controls the movement of elevators in a building. The elevator system is a complex system that consists of multiple components such as elevators, floors, buttons, and displays. 

## Table of Contents
- [Elevator System](#elevator-system)
- [Notes](#notes)
- [Components](#components)
- [Test](#test)
- [C Interoperability](#c-interoperability)

## Code
This repository contains the design and implementation of an elevator system.

## Elevator System
The `Notes` folder contains algorithms, class diagrams, use case explanation and requirements.

## Components
The implementation has the following components:
- **ElevatorSystem**: The main class that manages the elevators and their interactions.
- **ElevatorCar**: Represents individual elevators, including their state and behavior.
- **Floor**: Represents the floors in the building, including the display and hall panels.
- **Button**: Abstract class for buttons, with specific implementations for elevator and hall buttons.
- **Display**: Manages the display of the current floor and direction of the elevator.
- **EmergencyHandler**: Handles emergency situations, such as fire alarms and power outages.
- **MaintenanceHandler**: Handles maintenance requests, such as setting an elevator to maintenance mode.


## Algorithm
- SCAN algorithm: Moves the elevator in two direction, servicing requests along the way.

## Test
The `Test` folder contains the test cases for the elevator system. You can also run specific tests using:

```
python -m pytest elevator_system/tests/test_algorithm.py
```

## C Interoperability
The project includes a C interoperability layer located in `elevator_system/interop.c`.