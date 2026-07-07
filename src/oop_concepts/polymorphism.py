class PolymorphismExample:
    def __init__(self):
        self.title = "Polymorphism: Many Forms, One Interface"
        self.concept = "Polymorphism"
        self.description = (
            "Polymorphism means 'many forms'. It allows objects of different classes "
            "to be treated as objects of a common parent class. Each object responds "
            "to the same method call in its own way.\n\n"
            "Think of lecturers. Every lecturer conducts a lecture, but each one does it differently:\n\n"
            "- A Computer Science lecturer writes code on a projector.\n"
            "- A Mathematics lecturer solves problems on the whiteboard.\n"
            "- A Music lecturer plays instruments.\n\n"
            "They all 'conduct_lecture()', but the implementation differs. "
            "That is polymorphism.\n\n"
            "In Python, polymorphism works through method overriding and duck typing."
        )
        self.example_code = (
            "class Lecturer:\n"
            "    def conduct_lecture(self):\n"
            "        return 'Lecturer conducts a lecture'\n\n"
            "class CSLecturer(Lecturer):\n"
            "    def conduct_lecture(self):\n"
            "        return 'Writing Python code on the projector'\n\n"
            "class MathLecturer(Lecturer):\n"
            "    def conduct_lecture(self):\n"
            "        return 'Solving equations on the whiteboard'\n\n"
            "lecturers = [CSLecturer(), MathLecturer()]\n"
            "for l in lecturers:\n"
            "    print(l.conduct_lecture())  # Same call, different output"
        )
        self.location = "Lecture Theatre A"
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
