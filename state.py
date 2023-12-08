from typing import List


class State:
    def __init__(self, state_name):
        self.transitions: List[Transition] = []
        self.state_name = state_name

    def __str__(self):
        transitions_str = "\n".join([t.__str__() for t in self.transitions])
        return f"Name: {self.state_name}\nTransitions:\n{transitions_str}\n"

    def add_transition(self, next_state, conditions):
        self.transitions.append(Transition(self.state_name, next_state, conditions))

    @classmethod
    def get_state_by_name(cls, states, name):
        return next((state for state in states if state.state_name == name), None)


class Transition:
    def __init__(self, current_state, next_state, conditions):
        self.current_state = current_state
        self.next_state = next_state
        self.conditions: List[Condition] = [Condition(condition) for condition in conditions]

    def __str__(self):
        conditions_str = " ".join([condition.__str__() for condition in self.conditions])
        return f"{self.current_state} --> {self.next_state} Conditions: {conditions_str}"


class Condition:
    def __init__(self, conditions):
        self.read_symbol = conditions[0]
        self.write_symbol = conditions[1]
        self.move_direction_symbol = conditions[2]

    def __str__(self):
        return f"(Read: {self.read_symbol}, Write: {self.write_symbol}, Move to: {self.move_direction_symbol})"
