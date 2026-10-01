class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name})"


class Fish(Animal):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

    def __str__(self):
        return f"Fish(name={self.name}, habitat={self.habitat})"


class Bird(Animal):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def __str__(self):
        return f"Bird(name={self.name}, speed={self.speed})"


class Insect(Animal):
    def __init__(self, name, size, date):
        super().__init__(name)
        self.size = size
        self.date = date

    def __str__(self):
        return (
            f"Insect(name={self.name}, "
            f"size={self.size}, date={self.date})"
        )


animals = []


def process_command(command):
    if command.startswith("ADD"):
        handle_add(command)
    elif command.startswith("REM"):
        handle_rem(command)
    elif command.startswith("PRINT"):
        handle_print()


def handle_add(command):
    animal_data = {}

    _, command_data = command.strip().split(" ", 1)
    animal_type, parameters = command_data.split(";", 1)

    for parameter in parameters.split(";"):
        key, value = parameter.split("=")
        animal_data[key] = value

    if animal_type == "Fish":
        animal = Fish(
            animal_data["name"],
            animal_data["habitat"]
        )
    elif animal_type == "Bird":
        animal = Bird(
            animal_data["name"],
            animal_data["speed"]
        )
    elif animal_type == "Insect":
        animal = Insect(
            animal_data["name"],
            animal_data["size"],
            animal_data["date"]
        )
    else:
        print("Неизвестный тип", animal_type)
        return

    animals.append(animal)


def handle_rem(command):
    clean_line = command.strip()

    _, rest = clean_line.split(" ", 1)
    _, name_to_delete = rest.split("=", 1)

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
        return

    for animal in animals:
        print(animal)

    print()


with open("animals.txt", "r") as f:
    for line in f:
        process_command(line.strip())