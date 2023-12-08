class JsonMt:
    def __init__(self, json_data):
        self.mt = json_data.get("mt", [])

        self.tape_number = self.mt[0]
        self.states = self.mt[1]
        self.alphabet = self.mt[2]
        self.tape_alphabet = self.mt[3]
        self.start_symbol = self.mt[4]
        self.empty_symbol = self.mt[5]
        self.transitions = self.mt[6]
        self.start_state = self.mt[7]
        self.end_states = self.mt[8]

    def __str__(self):
        return (
            f"Turing Machine:\n"
            f"Tape Number: {self.tape_number}\n"
            f"States: {self.states}\n"
            f"Alphabet: {self.alphabet}\n"
            f"Tape Alphabet: {self.tape_alphabet}\n"
            f"Start Symbol: {self.start_symbol}\n"
            f"Empty Symbol: {self.empty_symbol}\n"
            f"Transitions: {self.transitions}\n"
            f"Start State: {self.start_state}\n"
            f"End States: {self.end_states}\n"
        )