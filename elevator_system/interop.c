// This C file serves as an interoperability layer between the Python elevator system
// and lower-level C code. It provides several benefits:

// 1. Performance: C code can be faster for certain operations, especially those
//    involving frequent state changes or complex calculations.

// 2. Memory efficiency: C allows for more fine-grained control over memory allocation
//    and management, which can be beneficial for resource-intensive operations.

// 3. Hardware interaction: If the elevator system needs to interact with specific
//    hardware components, C code can provide lower-level access to system resources.

// 4. Legacy system integration: If the elevator system needs to interface with
//    existing C libraries or older systems, this file can serve as a bridge.

// 5. Portability: C code can be more easily ported to different platforms or
//    embedded systems if needed.

// This file specifically provides:
// - A C struct for representing elevator state
// - Functions for creating and managing elevator state
// - Python wrapper functions to allow the Python code to interact with the C structs

#include <Python.h>
#include <stdbool.h>

// Enum for elevator direction
typedef enum {
    IDLE,
    UP,
    DOWN
} Direction;

// Struct to represent elevator state
typedef struct {
    int current_floor;
    Direction direction;
} ElevatorState;

// Function to initialize elevator state
static ElevatorState* create_elevator_state(int floor, Direction dir) {
    ElevatorState* state = (ElevatorState*)malloc(sizeof(ElevatorState));
    if (state) {
        state->current_floor = floor;
        state->direction = dir;
    }
    return state;
}

// Function to free elevator state
static void free_elevator_state(ElevatorState* state) {
    free(state);
}

// Python wrapper for create_elevator_state
static PyObject* py_create_elevator_state(PyObject* self, PyObject* args) {
    int floor;
    int dir;
    if (!PyArg_ParseTuple(args, "ii", &floor, &dir)) {
        return NULL;
    }
    ElevatorState* state = create_elevator_state(floor, (Direction)dir);
    return PyCapsule_New(state, "ElevatorState", (PyCapsule_Destructor)free_elevator_state);
}

// Python wrapper to get current floor
static PyObject* py_get_current_floor(PyObject* self, PyObject* args) {
    PyObject* capsule;
    if (!PyArg_ParseTuple(args, "O", &capsule)) {
        return NULL;
    }
    ElevatorState* state = (ElevatorState*)PyCapsule_GetPointer(capsule, "ElevatorState");
    return PyLong_FromLong(state->current_floor);
}

// Python wrapper to get direction
static PyObject* py_get_direction(PyObject* self, PyObject* args) {
    PyObject* capsule;
    if (!PyArg_ParseTuple(args, "O", &capsule)) {
        return NULL;
    }
    ElevatorState* state = (ElevatorState*)PyCapsule_GetPointer(capsule, "ElevatorState");
    return PyLong_FromLong(state->direction);
}

// Method definitions
static PyMethodDef ElevatorMethods[] = {
    {"create_elevator_state", py_create_elevator_state, METH_VARARGS, "Create a new elevator state"},
    {"get_current_floor", py_get_current_floor, METH_VARARGS, "Get the current floor of an elevator"},
    {"get_direction", py_get_direction, METH_VARARGS, "Get the direction of an elevator"},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef elevatormodule = {
    PyModuleDef_HEAD_INIT,
    "elevator",
    "Elevator system interop module",
    -1,
    ElevatorMethods
};

// Module initialization function
PyMODINIT_FUNC PyInit_elevator(void) {
    return PyModule_Create(&elevatormodule);
}
