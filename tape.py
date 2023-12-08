class Tape:

    def __init__(self, start_symbol, empty_symbol, cells):
        self.start_symbol = start_symbol
        self.empty_symbol = empty_symbol
        self.__cells = [start_symbol] + cells + [empty_symbol]
        self.__head = 1

    @property
    def current_cell(self):
        return self.__cells[self.__head]

    def set_current_cell(self, value):
        self.__cells[self.__head] = value

    def right(self):
        if self.__head + 1 < len(self.__cells):
            old_cell = self.current_cell
            old_head = self.__head
            self.__head += 1
            # return f'{old_cell}[{old_head}] R--> {self.current_cell}[{self.__head}]'
        else:
            self.__cells.append(self.empty_symbol)
            old_cell = self.current_cell
            old_head = self.__head
            self.__head += 1
            # return f'{old_cell}[{old_head}] R--> {self.current_cell}[{self.__head}]'

    def left(self):
        if self.__head - 1 >= 0:
            old_cell = self.current_cell
            old_head = self.__head
            self.__head -= 1
            # return f'{old_cell}[{old_head}] L--> {self.current_cell}[{self.__head}]'
        else:
            # return f'{self.current_cell} is the first cell'
            pass

    def __str__(self):
        return f'Tape: {self.__cells}, Head: {self.__head}, Current Cell: {self.current_cell}'
