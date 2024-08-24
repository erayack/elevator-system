import pytest
from elevator_system.elevator_enums import Direction, ElevatorState
from elevator_system.algorithm import SCANAlgorithm, ElevatorState as AlgorithmElevatorState


class TestSCANAlgorithm:
    @pytest.fixture
    def algorithm(self):
        return SCANAlgorithm(num_floors=10, num_elevators=3)

    def test_initialize_elevators(self, algorithm):
        algorithm.initialize_elevators()
        assert len(algorithm.elevator_states) == 3
        for state in algorithm.elevator_states.values():
            assert state.current_floor == 1
            assert state.direction.name == 'IDLE'

    def test_add_request(self, algorithm):
        algorithm.add_request(3, 7)
        assert 3 in algorithm.requests
        assert 7 in algorithm.requests[3]

    def test_find_nearest_floor_with_request(self, algorithm):
        algorithm.add_request(3, 7)
        algorithm.add_request(5, 2)
        assert algorithm._find_nearest_floor_with_request(1) == 3
        assert algorithm._find_nearest_floor_with_request(4) == 3
        assert algorithm._find_nearest_floor_with_request(10) == 5

    def test_move_elevator(self, algorithm):
        algorithm.initialize_elevators()
        print(f"Initial state: {algorithm.elevator_states[0].current_floor}, {algorithm.elevator_states[0].direction}")
        algorithm.elevator_states[0].direction = Direction.UP
        print(f"After setting direction: {algorithm.elevator_states[0].current_floor}, {algorithm.elevator_states[0].direction}")
        algorithm._move_elevator(0)
        print(f"Final state: {algorithm.elevator_states[0].current_floor}, {algorithm.elevator_states[0].direction}")
        assert algorithm.elevator_states[0].current_floor == 2, f"Expected floor 2, but got {algorithm.elevator_states[0].current_floor}"

        # Add more detailed assertions
        assert algorithm.elevator_states[0].direction == Direction.UP, f"Expected direction UP, but got {algorithm.elevator_states[0].direction}"
        
        # Test moving down
        algorithm.elevator_states[1].direction = Direction.DOWN
        algorithm.elevator_states[1].current_floor = 5
        algorithm._move_elevator(1)
        assert algorithm.elevator_states[1].current_floor == 4, f"Expected floor 4, but got {algorithm.elevator_states[1].current_floor}"
        assert algorithm.elevator_states[1].direction == Direction.DOWN, f"Expected direction DOWN, but got {algorithm.elevator_states[1].direction}"

    def test_handle_floor_requests(self, algorithm):
        algorithm.add_request(3, 7)
        algorithm.add_request(3, 5)
        algorithm._handle_floor_requests(0, 3)
        assert 3 not in algorithm.requests

    def test_process_requests(self, algorithm):
        algorithm.initialize_elevators()
        algorithm.add_request(3, 7)
        algorithm.add_request(5, 2)
        algorithm.process_requests()
        assert algorithm.elevator_states[0].direction != Direction.IDLE

    def test_get_elevator_state(self, algorithm):
        algorithm.initialize_elevators()
        state = algorithm.get_elevator_state(0)
        assert isinstance(state, AlgorithmElevatorState)
        assert state.current_floor == 1
        assert state.direction.name == 'IDLE'

if __name__ == "__main__":
    pytest.main()