class DesignPatternsTutorial:
    def __init__(self):
        self.title = "Design Patterns: Proven Solutions"
        self.concept = "Design Patterns"
        self.description = (
            "Design patterns are reusable solutions to common software design problems. "
            "They are like architectural blueprints that you can adapt to your specific needs.\n\n"
            "Just as university buildings follow standard architectural patterns "
            "(lecture theatres, laboratories, offices), software systems follow "
            "design patterns that have been proven to work.\n\n"
            "Key patterns include:\n\n"
            "SINGLETON: Ensures a class has only one instance (like the University itself).\n\n"
            "FACTORY: Creates objects without specifying the exact class (like the Registration Office).\n\n"
            "OBSERVER: Notifies multiple objects when something changes (like the university announcement system).\n\n"
            "STRATEGY: Allows selecting an algorithm at runtime (like choosing a study method)."
        )
        self.example_code = (
            "class SingletonUniversity:\n"
            "    _instance = None\n\n"
            "    def __new__(cls):\n"
            "        if cls._instance is None:\n"
            "            cls._instance = super().__new__(cls)\n"
            "            cls._instance.name = 'Mbeya University'\n"
            "        return cls._instance\n\n"
            "# Both variables point to the same object\n"
            "u1 = SingletonUniversity()\n"
            "u2 = SingletonUniversity()\n"
            "print(u1 is u2)  # True"
        )
        self.location = "Innovation Hub"
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


class ObserverPatternExample:
    def __init__(self):
        self.title = "Observer Pattern: The University Notification System"
        self.concept = "Observer Pattern"
        self.description = (
            "The Observer pattern defines a one-to-many dependency between objects. "
            "When one object changes state, all its dependents are notified automatically.\n\n"
            "Think of the university announcement system:\n\n"
            "When the Academic Registrar sends a notice:\n"
            "- Students receive it on their portals\n"
            "- Lecturers receive it via email\n"
            "- Department heads receive it in their dashboard\n"
            "- The notice board updates\n\n"
            "Everyone who 'subscribes' gets notified automatically."
        )
        self.example_code = (
            "class AnnouncementSystem:\n"
            "    def __init__(self):\n"
            "        self.subscribers = []\n\n"
            "    def subscribe(self, observer):\n"
            "        self.subscribers.append(observer)\n\n"
            "    def notify_all(self, message):\n"
            "        for observer in self.subscribers:\n"
            "            observer.receive(message)\n\n"
            "class StudentPortal:\n"
            "    def receive(self, message):\n"
            "        print(f'Portal: {message}')\n\n"
            "system = AnnouncementSystem()\n"
            "system.subscribe(StudentPortal())\n"
            "system.notify_all('Exam results are out!')"
        )
        self.location = "Student Centre"
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


PATTERNS = [DesignPatternsTutorial(), ObserverPatternExample()]
