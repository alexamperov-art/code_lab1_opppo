class Animal:
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name})"


class Fish(Animal):
    def __init__(self, name: str, habitat: str):
        super().__init__(name)
        self.habitat = habitat
    def __str__(self):
        return f'Fish(name={self.name}, habitat={self.habitat})'


class Bird(Animal):
    def __init__(self, name: str, speed: float):
        super().__init__(name)
        self.speed = speed
    def __str__(self):
        return f'Bird(name={self.name}, speed={self.speed})'



class Insect(Animal):
    def __init__(self, name: str, size: float, date:str):
        super().__init__(name)
        self.size = size
        self.date = date
    def __str__(self):
        return f'Insect(name={self.name}, size={self.size}, date={self.date})'


animals = []

def process_command(line):
    if line.startswith("ADD"):
        handle_add(line)
    elif line.startswith("REM"):
        handle_rem(line)
    elif line.startswith("PRINT"):
        handle_print()


def handle_add(line):
    dictionary = {}
    line = line.strip()
    cmd, rest = line.split(" ", 1)
    obj_type, params = rest.split(";", 1)
    for param in params.split(";"):
        key, value = param.split("=")
        dictionary[key] = value

    if obj_type == "Fish":
        fiz = Fish(dictionary["name"], dictionary["habitat"])
    elif obj_type == "Bird":
        fiz = Bird(dictionary["name"], dictionary["speed"])
    elif obj_type == "Insect":
        fiz = Insect(dictionary["name"], dictionary["size"], dictionary["date"])
    else:
        print("Неизвестный тип", obj_type)
        return
    animals.append(fiz)

def handle_rem(line):
    line = line.strip()
    cmd, rest = line.split(" ", 1)
    key, name_to_delete = rest.split("=", 1)

    found = False

    for animal in animals[:]:
        if animal.name == name_to_delete:
            animals.remove(animal)
            found = True

    if not found:
        print("Животное не найдено:", name_to_delete)


def handle_print():
    if not animals:
        print("Список пуст")
        print()
    for f in animals:
        print(f)
    print()

with open("animals.txt", "r", encoding="utf-8") as f:
    for line in f:
        process_command(line.strip())