from src.entities.npc import NPC


class Lecturer(NPC):
    def __init__(self, name, x, y, department, course):
        super().__init__(name, x, y, "Lecturer", (50, 50, 180))
        self.department = department
        self.course = course
        self.office_hours = []
        self.lecture_schedule = []
        self.supervises = []

    def add_supervisee(self, student_name):
        self.supervises.append(student_name)

    def get_lecture_topics(self):
        return [f"{self.course}: Lecture {i+1}" for i in range(12)]

    def serialize(self):
        data = super().serialize()
        data["type"] = "Lecturer"
        data["department"] = self.department
        data["course"] = self.course
        data["office_hours"] = self.office_hours
        data["lecture_schedule"] = self.lecture_schedule
        data["supervises"] = self.supervises
        return data

    @staticmethod
    def deserialize(data):
        lecturer = Lecturer(data["name"], data["x"], data["y"], data["department"], data["course"])
        lecturer.facing = data["facing"]
        lecturer.current_dialogue_index = data["current_dialogue_index"]
        lecturer.current_schedule_index = data["current_schedule_index"]
        lecturer.wait_timer = data["wait_timer"]
        lecturer.schedule = data["schedule"]
        lecturer.office_hours = data["office_hours"]
        lecturer.lecture_schedule = data["lecture_schedule"]
        lecturer.supervises = data["supervises"]
        return lecturer
