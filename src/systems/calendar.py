class AcademicCalendar:
    def __init__(self):
        self.year = 1
        self.semester = 1
        self.week = 1
        self.day_of_week = 1
        self.total_days = 1
        self.current_event = "Registration"
        self.events = {
            1: {
                1: ["Registration", "Orientation", "Classes Begin",
                    "Continuous Assessment", "Mid Semester", "Projects",
                    "Practical Sessions", "Industrial Visits",
                    "Final Examinations", "Semester Break"],
                2: ["Registration", "Classes Begin", "Continuous Assessment",
                    "Mid Semester", "Projects", "Practical Sessions",
                    "Industrial Visits", "Final Examinations", "Semester Break"]
            },
            2: {
                1: ["Registration", "Classes Begin", "Continuous Assessment",
                    "Mid Semester", "Projects", "Final Examinations", "Semester Break"],
                2: ["Registration", "Classes Begin", "Continuous Assessment",
                    "Mid Semester", "Projects", "Final Examinations", "Semester Break"]
            },
            3: {
                1: ["Registration", "Industrial Training", "Classes Begin",
                    "Continuous Assessment", "Mid Semester", "Projects",
                    "Final Examinations", "Semester Break"],
                2: ["Registration", "Classes Begin", "Continuous Assessment",
                    "Mid Semester", "Projects", "Final Examinations", "Semester Break"]
            },
            4: {
                1: ["Registration", "Final Year Project Prep", "Classes Begin",
                    "Continuous Assessment", "Mid Semester", "Project Development",
                    "Final Examinations", "Semester Break"],
                2: ["Registration", "Project Completion", "Classes Begin",
                    "Continuous Assessment", "Mid Semester", "Project Submission",
                    "Final Examinations", "Graduation"]
            }
        }
        self.week_length = 7
        self.semester_length = 15

    def update(self, dt):
        pass

    def advance_day(self):
        self.total_days += 1
        self.day_of_week = (self.day_of_week % 7) + 1
        if self.day_of_week == 1:
            self.week += 1
        if self.week > self.semester_length:
            self.week = 1
            if self.semester == 1:
                self.semester = 2
            else:
                self.semester = 1
                if self.year < 4:
                    self.year += 1
                else:
                    self.current_event = "Graduation"
        self._update_event()

    def _update_event(self):
        events_list = self.events.get(self.year, {}).get(self.semester, [])
        idx = min(self.week - 1, len(events_list) - 1)
        if idx >= 0:
            self.current_event = events_list[idx]

    def get_current_event(self):
        return self.current_event

    def get_day_name(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[(self.day_of_week - 1) % 7]

    def get_semester_progress(self):
        return f"Week {self.week}/{self.semester_length}"

    def serialize(self):
        return {
            "year": self.year,
            "semester": self.semester,
            "week": self.week,
            "day_of_week": self.day_of_week,
            "total_days": self.total_days,
            "current_event": self.current_event
        }

    @staticmethod
    def deserialize(data):
        cal = AcademicCalendar()
        cal.year = data["year"]
        cal.semester = data["semester"]
        cal.week = data["week"]
        cal.day_of_week = data["day_of_week"]
        cal.total_days = data["total_days"]
        cal.current_event = data["current_event"]
        return cal

    def reset(self):
        self.year = 1
        self.semester = 1
        self.week = 1
        self.day_of_week = 1
        self.total_days = 1
        self.current_event = "Registration"
