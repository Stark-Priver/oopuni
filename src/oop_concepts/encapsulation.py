class EncapsulationDetail:
    def __init__(self):
        self.title = "Encapsulation in Depth"
        self.concept = "Encapsulation"
        self.description = (
            "Encapsulation is one of the four fundamental OOP principles. "
            "It bundles data (attributes) and methods that operate on that data "
            "into a single unit — a class — and restricts direct access to some components.\n\n"
            "Why does this matter?\n\n"
            "1. PROTECTION: Prevents accidental or unauthorized modification of data.\n"
            "2. VALIDATION: Ensures data integrity by controlling how data is changed.\n"
            "3. FLEXIBILITY: Internal implementation can change without affecting external code.\n"
            "4. MAINTAINABILITY: Code is easier to understand and modify.\n\n"
            "In the university context:\n"
            "- Exam results cannot be modified directly by students.\n"
            "- Library books cannot be checked out without proper procedure.\n"
            "- Student records are accessed only through authorized systems.\n\n"
            "These are all examples of encapsulation in action."
        )
        self.example_code = (
            "class ExamResult:\n"
            "    def __init__(self, student_id):\n"
            "        self.__student_id = student_id\n"
            "        self.__marks = {}  # private\n"
            "        self.__total = 0\n\n"
            "    def add_mark(self, course, score):\n"
            "        if 0 <= score <= 100:\n"
            "            self.__marks[course] = score\n"
            "            self.__calculate_total()\n\n"
            "    def __calculate_total(self):  # private method\n"
            "        self.__total = sum(self.__marks.values())\n\n"
            "    def get_transcript(self):\n"
            "        return dict(self.__marks)  # returns a copy"
        )
        self.location = "Examination Office"
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
