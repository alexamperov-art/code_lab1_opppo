from oppo_1_lab import Fish, Bird, Insect,  handle_add, animals, handle_rem, handle_print, process_command

def test_Fish():
    fish = Fish("Судак", "река")
    assert fish.name == "Судак"
    assert fish.habitat == "река"

def test_Bird():
    bird = Bird("Аист", 120.0)
    assert bird.name == "Аист"
    assert bird.speed == 120.0

def test_Insect():
    insect = Insect("Бабочка", 5.0, "01.10.2026")
    assert insect.name == "Бабочка"
    assert insect.size == 5.0
    assert insect.date == "01.10.2026"

def test_add_insect():
    animals.clear()
    handle_add("ADD Insect;name=Бабочка;size=5.0;date=01.10.2026")
    assert len(animals) == 1
    assert isinstance(animals[0], Insect)
    assert animals[0].name == "Бабочка"
    assert animals[0].size == 5.0
    assert animals[0].date == "01.10.2026"

def test_add_fish():
    animals.clear()
    handle_add("ADD Fish;name=Лосось;habitat=Океан")
    assert len(animals) == 1
    assert isinstance(animals[0], Fish)
    assert animals[0].name == "Лосось"
    assert animals[0].habitat == "Океан"

def test_add_bird():
    animals.clear()
    handle_add("ADD Bird;name=Аист;speed=120")
    assert len(animals) == 1
    assert isinstance(animals[0], Bird)
    assert animals[0].name == "Аист"
    assert animals[0].speed == 120.0

def test_add_unknown_type(capsys):
    animals.clear()
    handle_add("ADD Jellyfish;name=Бордовоежало")
    captured = capsys.readouterr()
    assert "Неизвестный тип Jellyfish" in captured.out
    assert len(animals) == 0

def test_remove_fish():
    animals.clear()
    handle_add("ADD Fish;name=Лосось;habitat=Океан")
    handle_rem("REM name=Лосось")
    assert len(animals) == 0

def test_remove_not_found():
    animals.clear()
    handle_add("ADD Fish;name=Лосось;habitat=Океан")
    handle_rem("REM name=Аист")
    assert len(animals) == 1
    assert animals[0].name == "Лосось"

def test_print_empty(capsys):
    animals.clear()
    handle_print()
    captured = capsys.readouterr()
    assert "Список пуст" in captured.out

def test_print_animals(capsys):
    animals.clear()
    handle_add("ADD Fish;name=Лосось;habitat=Океан")
    handle_print()
    captured = capsys.readouterr() #capsys перехватывает вывод, readouterr забирает перехваченный вывод
    assert "Fish(name=Лосось, habitat=Океан)" in captured.out

def test_fish_describe():
    fish = Fish("Судак", "река")
    assert fish.describe() == "Среда обитания: река"


def test_bird_describe():
    bird = Bird("Аист", 120.0)
    assert bird.describe() == "Скорость: 120.0"


def test_insect_describe():
    insect = Insect("Бабочка", 5.0, "01.10.2026")
    assert insect.describe() == "Размер: 5.0, дата: 01.10.2026"


def test_fish_str():
    fish = Fish("Судак", "река")
    assert str(fish) == "Fish(name=Судак, habitat=река)"


def test_bird_str():
    bird = Bird("Аист", 120.0)
    assert str(bird) == "Bird(name=Аист, speed=120.0)"


def test_insect_str():
    insect = Insect("Бабочка", 5.0, "01.10.2026")
    assert str(insect) == "Insect(name=Бабочка, size=5.0, date=01.10.2026)"


def test_process_command_add():
    animals.clear()
    process_command("ADD Fish;name=Лосось;habitat=Океан")
    assert len(animals) == 1
    assert isinstance(animals[0], Fish)


def test_process_command_remove():
    animals.clear()
    handle_add("ADD Fish;name=Лосось;habitat=Океан")
    process_command("REM name=Лосось")
    assert len(animals) == 0


def test_process_command_print(capsys):
    animals.clear()
    handle_add("ADD Fish;name=Лосось;habitat=Океан")
    process_command("PRINT")
    captured = capsys.readouterr()
    assert "Fish(name=Лосось, habitat=Океан)" in captured.out

