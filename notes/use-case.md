## **System**

Our system is an "elevator."

## **Actors**

### **Primary actors**

**Passenger:** This actor is the passenger in an elevator. It can request an elevator, open and close the door of an elevator, move up and down using the elevator, and press the emergency button.

### **Secondary actors**

**System:** It can open and close the elevator door, display floor level, and move the elevator according to the dispatcher algorithm.

## **Use Cases**

We have listed the use cases according to their respective interactions with a particular actor.

### **Passenger**

- **Press elevator panel button:** To press the button on the elevator panel to select the destination floor, request to open/close the elevator door while it is stopped, or call an emergency
- **Press hall panel button:** To press the button on the hall panel to select the request for the elevator

### **System**

- **Move/stop elevator:** To move up or down or to stop the elevator on a specific floor
- **Dispatcher algorithm:** For proper elevator functionality according to the algorithm
- **Display (inside/outside):** To display the floor number on the screen inside and outside the elevator
- **Open/close door:** To open and close the elevator door

There are some use cases that are not directly related to any actor. These are elaborated below

- **Request for elevator:** To request the elevator
- **Floor request:** To submit a request for the destination floor
- **Door open/close request:** To submit a request to open/close the elevator door
- **Call Emergency:** To call the support team in case of emergency

## **Relationships**

### **Generalization**

We can press the elevator panel button to select the destination floor, request to open/close the elevator door while it is stopped, or call an emergency. This demonstrates that the “Press elevator panel button” use case has a generalization relationship with “Floor request,” “Door open/close request,” and “Call emergency” use cases.

### **Associations**

The table below shows the association relationship between actors and their use cases.

| Passenger | System |
| --- | --- |
| Press elevator panel button | Dispatcher algorithm |
| Press hall panel button | Open/close door |
|  | Display (inside/outside) |
|  | Move/stop elevator |

### **Include**

- When a floor request is submitted, the system will move the elevator and stop it at the requested floor. Hence, the “Floor request” use case has an include relationship with the “Move/stop elevator” use case.
- When a door open/close request is submitted, the system will open/close the elevator door. Hence, the “Door open/close request” use case has an include relationship with the “Open/close door” use case.
- When any button on the hall panel is pressed, a request for the elevator is submitted. Hence, the “Press hall panel button” use case has an include relationship with the “Request for elevator” use case.



