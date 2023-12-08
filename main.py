import argparse
import json

from json_mt_decoder import JsonMt
from turing_machine import TuringMachine

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="TM")
    parser.add_argument("json_file", type=str, help="Path to the JSON file containing Turing Machine information")
    parser.add_argument("cells", type=str, nargs='?', default='', help="Input cells for the Turing Machine")

    args = parser.parse_args()

    with open(args.json_file, 'r') as file:
        json_data = json.load(file)

    json_mt = JsonMt(json_data)

    turing_machine = TuringMachine(json_mt.tape_number)
    turing_machine.init_states(json_mt.states)
    turing_machine.init_transitions(json_mt.transitions)
    turing_machine.init_tapes(json_mt.start_symbol, json_mt.empty_symbol, args.cells)

    turing_machine.run(json_mt.start_state, json_mt.end_states)
