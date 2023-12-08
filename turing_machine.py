from typing import List

from state import State
from tape import Tape


class TuringMachine:
    def __init__(self, tape_number):
        self.tape_number = tape_number
        self.tapes: List[Tape] = []
        self.states: List[State] = []

    def init_tapes(self, start_symbol, empty_symbol, cells):
        for i in range(self.tape_number):
            tape_cells = list(cells) if i == 0 else list(empty_symbol)
            self.tapes.append(Tape(start_symbol, empty_symbol, tape_cells))

    def init_states(self, state_names):
        for state_name in state_names:
            self.states.append(State(state_name))

    def init_transitions(self, state_transitions):
        for state_transition in state_transitions:
            for state in self.states:
                if state.state_name == state_transition[0]:
                    current_state, next_state, conditions = state_transition
                    state.add_transition(next_state, conditions)

    def run(self, start_state, end_states):
        current_state = State.get_state_by_name(self.states, start_state)

        while True:
            transition = self.find_valid_transition(current_state)

            if transition is not None:
                self.execute_transition(transition)
                current_state = State.get_state_by_name(self.states, transition.next_state)
            else:
                break

        if current_state.state_name in end_states:
            print('Sim')
        else:
            print('Não')

    def find_valid_transition(self, current_state):
        for transition in current_state.transitions:
            conditions_match = all(
                transition.conditions[i].read_symbol == self.tapes[i].current_cell
                for i in range(self.tape_number)
            )
            if conditions_match:
                return transition
        return None

    def execute_transition(self, transition):
        for i in range(self.tape_number):
            self.tapes[i].set_current_cell(transition.conditions[i].write_symbol)
            if transition.conditions[i].move_direction_symbol == '>':
                self.tapes[i].right()
            elif transition.conditions[i].move_direction_symbol == '<':
                self.tapes[i].left()

    def __str__(self):
        return "\n".join([state.__str__() for state in self.states])
