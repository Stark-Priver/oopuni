class InheritanceExample:
    def __init__(self):
        self.title = "Inheritance: Departments as Specializations"
        self.concept = "Inheritance"
        self.description = (
            "Inheritance allows one class to derive properties and behaviors from another class. "
            "The child class inherits everything from the parent and can add or override features.\n\n"
            "Think of university departments. Every department is a department — they all have "
            "a name, head of department, courses, and students. But each department specializes.\n\n"
            "Computer Science is a department that also has laboratories and programming courses.\n"
            "Civil Engineering is a department that also has workshops and field projects.\n\n"
            "In OOP terms, ComputerScience inherits from Department and adds its own attributes."
        )
        self.example_code = (
            "class Department:\n"
            "    def __init__(self, name, hod):\n"
            "        self.name = name\n"
            "        self.hod = hod\n"
            "        self.staff = []\n\n"
            "    def add_staff(self, lecturer):\n"
            "        self.staff.append(lecturer)\n\n"
            "class ComputerScience(Department):  # Inheritance\n"
            "    def __init__(self, hod):\n"
            "        super().__init__('Computer Science', hod)\n"
            "        self.labs = []\n\n"
            "    def add_lab(self, lab_name):\n"
            "        self.labs.append(lab_name)\n\n"
            "cs = ComputerScience('Dr. Mbunda')\n"
            "cs.add_staff('Prof. Juma')\n"
            "cs.add_lab('AI Laboratory')"
        )
        self.location = "Any Department"
        self.completed = False

    def to_dict(self):
        return {
            "title": self.title,
            "concept": self.concept,
            "description": self.description,
            "example_code": self.example_code,
            "location": self.location,
            "completed": self.completed
        }


class CompositionExample:
    def __init__(self):
        self.title = "Composition: A University is Made of Parts"
        self.concept = "Composition"
        self.description = (
            "Composition is a relationship where one object is made up of other objects. "
            "If the parent object is destroyed, its parts are also destroyed.\n\n"
            "A university is composed of departments, buildings, students, and staff. "
            "If the university ceases to exist, those components cease to exist as part of it.\n\n"
            "Similarly, a Hostel object is composed of Room objects. "
            "If the Hostel is demolished, the rooms no longer exist."
        )
        self.example_code = (
            "class Room:\n"
            "    def __init__(self, number, capacity):\n"
            "        self.number = number\n"
            "        self.capacity = capacity\n\n"
            "class Hostel:\n"
            "    def __init__(self, name):\n"
            "        self.name = name\n"
            "        self.rooms = []  # Composition\n\n"
            "    def add_room(self, number, capacity):\n"
            "        room = Room(number, capacity)\n"
            "        self.rooms.append(room)\n"
            "        return room\n\n"
            "hostel_a = Hostel('Block A')\n"
            "room_101 = hostel_a.add_room(101, 4)"
        )
        self.location = "Hostels"
        self.completed = False

    def to_dict(self):
        return {
            "title": self.title,
            "concept": self.concept,
            "description": self.description,
            "example_code": self.example_code,
            "location": self.location,
            "completed": self.completed
        }


EXAMPLES = [InheritanceExample(), CompositionExample()]
