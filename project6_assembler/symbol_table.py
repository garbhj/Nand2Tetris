import os


class SymbolTable(dict):
    """Allows the user to add and retrieve mappings between symbols and addresses in RAM"""
    def __init__(self):
        # adds the predefined symbols to the table
        super().__init__()
        here = os.path.dirname(__file__)
        predefined_path = os.path.join(here, "predefined.txt")
        # with open("predefined.txt", "r") as p:
        with open(predefined_path, "r") as p:
            symbols = p.readlines()

        for symbol in symbols:
            key, value = symbol.split(":")
            self[key.strip()] = value.strip()

    def add(self, symbol, value):
        self[symbol] = value

    def get(self, symbol):
        if symbol in self.keys():
            return self[symbol]
        else:
            return -1


def test_symbol_table():
    t = SymbolTable()


if __name__ == "__main__":
    test_symbol_table()
