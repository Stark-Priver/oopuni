class AbstractionExample:
    def __init__(self):
        self.title = "Abstraction: Hiding Complexity"
        self.concept = "Abstraction"
        self.description = (
            "Abstraction means hiding complex implementation details and showing "
            "only the essential features of an object.\n\n"
            "Think about how you use a university timetable:\n\n"
            "You see: 'Monday 10AM - CS201 Lecture, Lecture Theatre B'\n"
            "You do NOT see: The room booking system, the lecturer scheduling algorithm, "
            "the conflict resolution logic, the department approval process.\n\n"
            "The timetable is an abstraction — it gives you what you need without "
            "exposing the complexity underneath.\n\n"
            "In Python, abstract classes (using the ABC module) define methods "
            "that must be implemented by subclasses."
        )
        self.example_code = (
            "from abc import ABC, abstractmethod\n\n"
            "class Timetable(ABC):\n"
            "    @abstractmethod\n"
            "    def get_lecture(self, day, time):\n"
            "        pass\n\n"
            "    @abstractmethod\n"
            "    def get_room(self, course):\n"
            "        pass\n\n"
            "class MUSTTimetable(Timetable):\n"
            "    def get_lecture(self, day, time):\n"
            "        return self._query_database(day, time)\n\n"
            "    def get_room(self, course):\n"
            "        return self._resolve_room_conflicts(course)\n\n"
            "    def _query_database(self, day, time):\n"
            "        return 'CS201 - OOP Principles'\n\n"
            "    def _resolve_room_conflicts(self, course):\n"
            "        return 'Lecture Theatre B'\n\n"
            "# User only calls get_lecture() and get_room()"
        )
        self.location = "Timetable Office"
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
