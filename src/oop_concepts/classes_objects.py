class Tutorial:
    def __init__(self, title, concept, description, example_code, location):
        self.title = title
        self.concept = concept
        self.description = description
        self.example_code = example_code
        self.location = location
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


CLASSES_OBJECTS_TUTORIAL = Tutorial(
    title="Introduction to Classes and Objects",
    concept="Classes and Objects",
    description=(
        "In Object-Oriented Programming, a class is like a blueprint or template. "
        "Just as the university has a standard registration process for every new student, "
        "a class defines the structure and behavior that every object of that type will have.\n\n"
        "An object is an instance of a class — a specific realization of the blueprint. "
        "When you register as a student, you become an instance of the Student class. "
        "Your student ID, name, department, and academic year are your attributes. "
        "Your ability to attend lectures, submit assignments, and borrow books are your methods."
    ),
    example_code=(
        "class Student:\n"
        "    def __init__(self, name, student_id, department):\n"
        "        self.name = name\n"
        "        self.student_id = student_id\n"
        "        self.department = department\n\n"
        "    def attend_lecture(self, course):\n"
        "        print(f'{self.name} is attending {course}')\n\n"
        "# Creating an object (instance)\n"
        "player = Student('You', 'MUST/001/2026', 'Computer Science')\n"
        "player.attend_lecture('OOP Principles')"
    ),
    location="Administration"
)

CONSTRUCTORS_TUTORIAL = Tutorial(
    title="Constructors: The Birth of an Object",
    concept="Constructors",
    description=(
        "A constructor is a special method that runs automatically when an object is created. "
        "It initializes the object's attributes and prepares it for use.\n\n"
        "Think of the university registration desk. When you arrive as a new student, "
        "the registration officer (the constructor) sets up your profile: "
        "they assign your student ID, record your name, register your department, "
        "and configure your email. Without this process, you cannot function as a student.\n\n"
        "In Python, the constructor is always called __init__."
    ),
    example_code=(
        "class Student:\n"
        "    def __init__(self, name, department):\n"
        "        print(f'Registering {name}...')\n"
        "        self.name = name\n"
        "        self.department = department\n"
        "        self.student_id = self._generate_id()\n"
        "        self.email = f'{name.lower()}@must.ac.tz'\n"
        "        print(f'{name} registered successfully!')\n\n"
        "# Constructor runs automatically\n"
        "s = Student('John', 'Computer Science')"
    ),
    location="Administration"
)

ATTRIBUTES_METHODS_TUTORIAL = Tutorial(
    title="Attributes and Methods",
    concept="Attributes and Methods",
    description=(
        "Attributes are the data that describes an object. They are the characteristics "
        "that make each object unique.\n\n"
        "Methods are the actions an object can perform. They define the behavior.\n\n"
        "For a student object:\n"
        "- Attributes: name, age, department, GPA, student_id\n"
        "- Methods: study(), attend_lecture(), submit_assignment(), borrow_book()\n\n"
        "The library is an excellent example: each book has attributes (title, author, ISBN) "
        "and methods (check_out(), return_book(), reserve())."
    ),
    example_code=(
        "class Book:\n"
        "    def __init__(self, title, author, isbn):\n"
        "        self.title = title        # attribute\n"
        "        self.author = author      # attribute\n"
        "        self.isbn = isbn          # attribute\n"
        "        self.is_checked_out = False\n\n"
        "    def check_out(self):          # method\n"
        "        if not self.is_checked_out:\n"
        "            self.is_checked_out = True\n"
        "            return f'{self.title} checked out.'\n"
        "        return 'Already checked out.'"
    ),
    location="Library"
)

ENCAPSULATION_TUTORIAL = Tutorial(
    title="Encapsulation: Protecting Data",
    concept="Encapsulation",
    description=(
        "Encapsulation is the practice of keeping an object's internal data private "
        "and providing controlled access through methods.\n\n"
        "Think of the bank on campus. You cannot directly modify your account balance. "
        "Instead, you deposit money (one method), withdraw money (another method), "
        "and check your balance (a third method). The bank protects your data "
        "by controlling how it is accessed and modified.\n\n"
        "In Python, attributes prefixed with __ are name-mangled to suggest privacy."
    ),
    example_code=(
        "class BankAccount:\n"
        "    def __init__(self, owner, initial_balance):\n"
        "        self.owner = owner\n"
        "        self.__balance = initial_balance  # private attribute\n\n"
        "    def deposit(self, amount):\n"
        "        if amount > 0:\n"
        "            self.__balance += amount\n\n"
        "    def withdraw(self, amount):\n"
        "        if 0 < amount <= self.__balance:\n"
        "            self.__balance -= amount\n\n"
        "    def get_balance(self):\n"
        "        return self.__balance\n\n"
        "# Cannot do: account.__balance = 9999"
    ),
    location="Bank"
)


TUTORIALS_BY_LOCATION = {
    "Administration": [CLASSES_OBJECTS_TUTORIAL, CONSTRUCTORS_TUTORIAL],
    "Library": [ATTRIBUTES_METHODS_TUTORIAL],
    "Bank": [ENCAPSULATION_TUTORIAL]
}

ALL_TUTORIALS = [CLASSES_OBJECTS_TUTORIAL, CONSTRUCTORS_TUTORIAL,
                 ATTRIBUTES_METHODS_TUTORIAL, ENCAPSULATION_TUTORIAL]
