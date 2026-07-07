import random


class Timetable:
    def __init__(self, calendar):
        self.calendar = calendar
        self.entries = {}
        self._generate()

    def _generate(self):
        courses = [
            "OOP Principles", "Data Structures", "Database Systems",
            "Web Development", "Networking", "Software Engineering",
            "Mathematics", "Programming Fundamentals"
        ]
        time_slots = [
            "08:00 - 10:00", "10:00 - 12:00", "12:00 - 14:00",
            "14:00 - 16:00", "16:00 - 18:00"
        ]
        locations = [
            "Lecture Theatre A", "Lecture Theatre B", "Computer Lab",
            "Laboratory A", "Engineering Workshop"
        ]
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        for day in days:
            self.entries[day] = []
            day_courses = random.sample(courses, min(4, len(courses)))
            for i, course in enumerate(day_courses):
                entry = {
                    "course": course,
                    "time": time_slots[i % len(time_slots)],
                    "location": locations[i % len(locations)],
                    "attended": False
                }
                self.entries[day].append(entry)

    def update(self):
        pass

    def get_today_entries(self):
        day_name = self.calendar.get_day_name()
        return self.entries.get(day_name, [])

    def mark_attended(self, course_name):
        for day_entries in self.entries.values():
            for entry in day_entries:
                if entry["course"] == course_name and not entry["attended"]:
                    entry["attended"] = True
                    return True
        return False

    def get_attendance_rate(self):
        total = 0
        attended = 0
        for day_entries in self.entries.values():
            for entry in day_entries:
                total += 1
                if entry["attended"]:
                    attended += 1
        return (attended / total * 100) if total > 0 else 0

    def serialize(self):
        return {"entries": self.entries}

    @staticmethod
    def deserialize(data, calendar=None):
        timetable = Timetable.__new__(Timetable)
        timetable.calendar = calendar
        timetable.entries = data["entries"]
        return timetable
