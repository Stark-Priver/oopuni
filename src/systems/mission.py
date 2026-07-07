class Mission:
    def __init__(self, mission_id, title, description, objectives, rewards=None):
        self.mission_id = mission_id
        self.title = title
        self.description = description
        self.objectives = objectives
        self.rewards = rewards or {}
        self.completed = False
        self.active = False
        self.progress = 0

    def to_dict(self):
        return {
            "mission_id": self.mission_id,
            "title": self.title,
            "description": self.description,
            "objectives": self.objectives,
            "rewards": self.rewards,
            "completed": self.completed,
            "active": self.active,
            "progress": self.progress
        }

    @staticmethod
    def from_dict(data):
        mission = Mission(data["mission_id"], data["title"], data["description"],
                         data["objectives"], data["rewards"])
        mission.completed = data["completed"]
        mission.active = data["active"]
        mission.progress = data["progress"]
        return mission


class MissionSystem:
    def __init__(self):
        self.active_missions = []
        self.completed_missions = []
        self.available_missions = []
        self._init_missions()

    def _init_missions(self):
        self.available_missions = [
            Mission("year1_admission", "The Admission Letter",
                    "Report to the Administration building to complete your registration.",
                    ["Find the Administration building", "Present your admission letter",
                     "Receive your student ID", "Create your student profile"],
                    {"reputation": {"Administration": 10}}),

            Mission("year1_orientation", "Orientation Week",
                    "Explore the campus and meet senior students to learn about university life.",
                    ["Visit the Library", "Visit the Student Centre",
                     "Visit the Cafeteria", "Visit a Lecture Theatre",
                     "Visit the Hostel"],
                    {"reputation": {"Student Government": 5}}),

            Mission("year1_first_class", "First Lecture",
                    "Attend your first OOP Principles lecture.",
                    ["Find Lecture Theatre A", "Attend the OOP lecture",
                     "Meet the lecturer"],
                    {"reputation": {"Lecturers": 10}}),

            Mission("year1_borrow_book", "Library Quest",
                    "Borrow your first book from the university library.",
                    ["Visit the Library", "Find a book on OOP",
                     "Check out the book using your student ID"],
                    {"reputation": {"Library": 10}}),

            Mission("year1_encapsulation", "Understanding Encapsulation",
                    "Visit the bank to learn how encapsulation protects data.",
                    ["Visit the Bank", "Talk to the bank teller",
                     "Deposit some money", "Learn about encapsulation"],
                    {"reputation": {"Departments": 5}}),

            Mission("year2_inheritance", "Department Inheritance",
                    "Visit three different departments and understand how they inherit from a common structure.",
                    ["Visit Computer Science department",
                     "Visit Civil Engineering department",
                     "Visit Business department",
                     "Compare their structures"],
                    {"reputation": {"Departments": 15}}),

            Mission("year2_polymorphism", "Many Lecturers, One Method",
                    "Observe how different lecturers teach the same concept in different ways.",
                    ["Attend a CS lecture", "Attend a Math lecture",
                     "Compare teaching styles",
                     "Report to Professor Object"],
                    {"reputation": {"Lecturers": 15}}),

            Mission("year3_industry", "Industrial Training",
                    "Complete your industrial training at a company in Mbeya.",
                    ["Find a placement company", "Complete 8 weeks of training",
                     "Submit your industrial report"],
                    {"reputation": {"Career Centre": 20}}),

            Mission("year4_project", "Final Year Project",
                    "Design and implement your final year project to restore the Object Framework.",
                    ["Choose a project topic", "Design the architecture",
                     "Implement the system", "Submit your project",
                     "Defend your project"],
                    {"reputation": {"Research Office": 25}}),

            Mission("chaos_bug_final", "The Chaos Bug Finale",
                    "Enter the deepest level of the Object Framework and rebuild the university systems.",
                    ["Reach the core of Object Framework",
                     "Identify the corrupted systems",
                     "Apply all OOP concepts to restore each system",
                     "Defeat the Chaos Bug",
                     "Graduate as a Software Engineer"],
                    {"reputation": {"Lecturers": 50, "Departments": 50}})
        ]

    def start_mission(self, mission_id):
        for mission in self.available_missions:
            if mission.mission_id == mission_id and not mission.completed:
                mission.active = True
                self.active_missions.append(mission)
                self.available_missions.remove(mission)
                return True
        return False

    def complete_mission(self, mission_id):
        for mission in self.active_missions:
            if mission.mission_id == mission_id:
                mission.completed = True
                mission.active = False
                mission.progress = 100
                self.completed_missions.append(mission)
                self.active_missions.remove(mission)
                return True
        return False

    def update(self, player, calendar):
        if calendar.year == 1 and calendar.current_event == "Registration":
            if "year1_admission" not in [m.mission_id for m in self.active_missions + self.completed_missions]:
                self.start_mission("year1_admission")

    def on_location_entered(self, location_name):
        for mission in self.active_missions:
            if location_name in [obj for obj in mission.objectives]:
                mission.progress += 1

    def get_active_mission_count(self):
        return len(self.active_missions)

    def serialize(self):
        return {
            "active_missions": [m.to_dict() for m in self.active_missions],
            "completed_missions": [m.to_dict() for m in self.completed_missions],
            "available_missions": [m.to_dict() for m in self.available_missions]
        }

    @staticmethod
    def deserialize(data):
        system = MissionSystem()
        system.active_missions = [Mission.from_dict(m) for m in data["active_missions"]]
        system.completed_missions = [Mission.from_dict(m) for m in data["completed_missions"]]
        system.available_missions = [Mission.from_dict(m) for m in data["available_missions"]]
        return system
