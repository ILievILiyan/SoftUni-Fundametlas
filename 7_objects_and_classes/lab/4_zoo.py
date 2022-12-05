class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        Zoo.__animals += 1
        # self.__animals += 1
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        animals_names = None
        result = ""
        if species == "mammal":
            animals_names = self.mammals
            result = "Mammals"
        elif species == "fish":
            animals_names = self.fishes
            result = "Fishes"
        elif species == "bird":
            animals_names = self.birds
            result = "Birds"

        animals_data = ", ".join(animals_names)
        return f"""{result} in {self.name}: {animals_data}
Total animals: {self.__animals}"""


zoo_name = input()
n = int(input())
zoo = Zoo(zoo_name)
for i in range(n):
    args = input().split(" ")
    zoo.add_animal(args[0], args[1])

species_type = input()
result = zoo.get_info(species_type)

print(result)



