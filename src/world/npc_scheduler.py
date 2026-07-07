from src.entities.npc import NPC
from src.entities.lecturer import Lecturer
from src.entities.student import Student
import random


class NPCScheduler:
    def __init__(self, campus):
        self.campus = campus
        self.npcs = []
        self._generate_npcs()

    def _generate_npcs(self):
        lecturer_data = [
            ("Prof. Juma", 300, 250, "Computer Science", "OOP Principles"),
            ("Dr. Mbunda", 700, 200, "Software Engineering", "Data Structures"),
            ("Dr. Mwakyusa", 1300, 260, "Mathematics", "Discrete Math"),
            ("Prof. Mushi", 1800, 260, "Civil Engineering", "Structural Analysis"),
            ("Dr. Mfaume", 2300, 230, "Electrical Engineering", "Circuits"),
        ]
        for name, x, y, dept, course in lecturer_data:
            lecturer = Lecturer(name, x, y, dept, course)
            lecturer.set_dialogues([
                f"Welcome to {dept} department. I teach {course}.",
                f"Have you completed the {course} assignment?",
                "Remember, office hours are every Wednesday at 2PM.",
                "Object-Oriented Programming is the foundation of modern software."
            ])
            self._generate_lecturer_schedule(lecturer)
            self.npcs.append(lecturer)

        student_names = [
            "Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona",
            "George", "Hannah", "Ivan", "Julia", "Kevin", "Lina"
        ]
        departments = ["Computer Science", "Software Engineering", "Civil Engineering",
                       "Electrical Engineering", "Business", "Education"]
        for i, name in enumerate(student_names[:8]):
            dept = departments[i % len(departments)]
            sx = 400 + random.randint(0, 2000)
            sy = 400 + random.randint(0, 600)
            student = Student(name, sx, sy, "Year One", dept)
            student.set_dialogues([
                f"Hey! I'm {name} from {dept}.",
                "Have you been to the Innovation Hub yet? It's amazing!",
                "I'm still trying to understand classes and objects.",
                "The cafeteria has great chips mayai!",
                "Don't forget to check your timetable for tomorrow."
            ])
            self._generate_student_schedule(student)
            self.npcs.append(student)

        guard = NPC("Security Officer Mkono", 1100, 1250, "Security", (0, 0, 100))
        guard.set_dialogues([
            "Welcome to MUST. Please present your student ID.",
            "Keep your student card visible at all times.",
            "The campus is safe, but stay aware of your surroundings."
        ])
        guard.schedule = [(1100, 1250, 300), (1100, 1200, 200), (1100, 1250, 300)]
        self.npcs.append(guard)

        librarian = NPC("Mrs. Kasanga", 700, 250, "Librarian", (100, 50, 130))
        librarian.set_dialogues([
            "Welcome to the library. Silence is golden.",
            "Books must be returned within two weeks.",
            "The OOP section is on the second floor."
        ])
        librarian.schedule = [(700, 250, 200), (750, 250, 300), (700, 250, 200)]
        self.npcs.append(librarian)

    def _generate_lecturer_schedule(self, lecturer):
        building = self.campus.get_building_at(lecturer.x, lecturer.y)
        if building:
            entrance = building.get_entrance()
            lecturer.schedule = [
                (lecturer.x, lecturer.y, 180),
                (entrance[0], entrance[1], 60),
                (lecturer.x, lecturer.y, 180)
            ]
        else:
            lecturer.schedule = [(lecturer.x, lecturer.y, 300)]

    def _generate_student_schedule(self, student):
        student.schedule = [
            (student.x, student.y, 120),
            (student.x + random.randint(-100, 100), student.y + random.randint(-100, 100), 60),
            (student.x, student.y, 120)
        ]

    def update(self, dt, game_timer):
        for npc in self.npcs:
            npc.update(self.campus, dt)

    def get_all_npcs(self):
        return self.npcs

    def get_npcs_in_range(self, x, y, radius):
        result = []
        for npc in self.npcs:
            dx = npc.x - x
            dy = npc.y - y
            if (dx * dx + dy * dy) <= radius * radius:
                result.append(npc)
        return result

    def get_npc_by_name(self, name):
        for npc in self.npcs:
            if npc.name.lower() == name.lower():
                return npc
        return None

    def serialize(self):
        return {"npcs": [npc.serialize() for npc in self.npcs]}

    @staticmethod
    def deserialize(data, campus):
        scheduler = NPCScheduler(campus)
        npc_data = []
        for npc_d in data["npcs"]:
            if npc_d.get("type") == "Lecturer":
                npc_data.append(Lecturer.deserialize(npc_d))
            elif npc_d.get("type") == "Student":
                npc_data.append(Student.deserialize(npc_d))
            else:
                npc_data.append(NPC.deserialize(npc_d))
        scheduler.npcs = npc_data
        return scheduler
