from src.entities.npc import NPC


class Student(NPC):
    def __init__(self, name, x, y, year, department):
        super().__init__(name, x, y, "Student", (100, 180, 100))
        self.year = year
        self.department = department
        self.classes = []
        self.club_memberships = []
        self.mood = "neutral"

    def enroll_class(self, course_name):
        self.classes.append(course_name)

    def join_club(self, club_name):
        self.club_memberships.append(club_name)

    def set_mood(self, mood):
        self.mood = mood

    def serialize(self):
        data = super().serialize()
        data["type"] = "Student"
        data["year"] = self.year
        data["department"] = self.department
        data["classes"] = self.classes
        data["club_memberships"] = self.club_memberships
        data["mood"] = self.mood
        return data

    @staticmethod
    def deserialize(data):
        student = Student(data["name"], data["x"], data["y"], data["year"], data["department"])
        student.facing = data["facing"]
        student.current_dialogue_index = data["current_dialogue_index"]
        student.current_schedule_index = data["current_schedule_index"]
        student.wait_timer = data["wait_timer"]
        student.schedule = data["schedule"]
        student.classes = data["classes"]
        student.club_memberships = data["club_memberships"]
        student.mood = data["mood"]
        return student
