from pyclbr import Class

class ClassDwarfs:
    def __init__(self, name, color, physic):
        self.name = name
        self.color = color
        self.physic = int(physic)
        self.dwarfs = {}
        self.sorted_dwarfs = {}

    def add_new_dwarf(self, name, color, physic):
        if color not in self.dwarfs.keys():
            self.dwarfs[color] = {}
        if name not in self.dwarfs[color].keys():
            self.dwarfs[color][name] = 0
        if self.dwarfs[color][name] < int(physic):
            self.dwarfs[color][name] = int(physic)

    def sort_the_dictionary_by_value(self):
        for color, name_points in self.dwarfs.items():
            for name, points in name_points.items():
                self.dwarfs[color] = dict(sorted(name_points.items(), key=lambda x: (-x[1], x[0])))

    def __repr__(self):
        return f'{self.dwarfs}'


while True:
    text_input = input()
    if text_input == "Once upon a time":
        break

    name1, color1, physics1 = text_input.split(" <:> ")

    dwarf = ClassDwarfs(name1, color1, physics1)
    dwarf.add_new_dwarf(name1, color1, physics1)
    dwarf.sort_the_dictionary_by_value()

print(dwarf)
