"""
Chapter One: Admission

The game begins outside Mbeya. The player travels by bus through the hills,
arrives at the university, and receives their student identity.

This module handles the introductory storyline and admission sequence.
"""


class ChapterOne:
    def __init__(self, player, dialog_system, mission_system, calendar):
        self.player = player
        self.dialog = dialog_system
        self.missions = mission_system
        self.calendar = calendar
        self.stage = 0
        self.completed = False

    def start_admission(self):
        if self.stage == 0:
            self.dialog.queue = [
                ("Narrator", "The bus winds through the hills surrounding Mbeya..."),
                ("Narrator", "Morning sunlight illuminates the mountains as the city skyline appears."),
                ("Narrator", "The bus reaches the university entrance. Security officers welcome newly admitted students."),
                ("Security", "Welcome to Mbeya University of Science and Technology! Please present your admission letter."),
                ("System", "Presenting admission letter... Identity verified."),
                ("System", "Creating student profile..."),
                ("Registrar", "Congratulations! You are now officially a student of MUST."),
                ("Registrar", f"Your Student ID: MUST/{2026}/CS/001"),
                ("Registrar", f"Your University Email: {self.player.name.lower()}.student@must.ac.tz"),
                ("System", "Student ID assigned: MUST/2026/CS/001"),
                ("System", "Registration Number: MUST/CS/2026/001"),
                ("System", "Faculty: Science and Technology"),
                ("System", "Department: Computer Science"),
                ("System", "Academic Year: Year One"),
                ("System", "University Email: student@must.ac.tz"),
                ("System", "Student Portal Account: activated"),
                ("System", "Orientation Guide: received"),
                ("System", "MUST Almanac: received"),
                ("System", "Digital Timetable: synced"),
                ("System", "Save Profile Access: granted"),
                ("System", "First Checkpoint Token: received"),
                ("System", "The first Object has been created."),
                ("Professor Object", "Excellent... You have successfully become an instance of the Student class."),
                ("Professor Object", "Your student ID is your identifier. Your attributes are now defined."),
                ("Professor Object", "But this is only the beginning. The Chaos Bug is already spreading."),
                ("Professor Object", "Explore the campus. Visit the Administration building to begin your first mission."),
            ]
            self.dialog.advance_queue()
            self._apply_admission_effects()
            self.stage = 1

    def _apply_admission_effects(self):
        self.player.student_id = "MUST/2026/CS/001"
        self.player.registration_number = "MUST/CS/2026/001"
        self.player.faculty = "Science and Technology"
        self.player.department = "Computer Science"
        self.player.email = "student@must.ac.tz"
        self.player.add_item(AdmissionItem("Student ID Card", "Your official MUST student identification"))
        self.player.add_item(AdmissionItem("Orientation Guide", "A guide to campus facilities and services"))
        self.player.add_item(AdmissionItem("MUST Almanac", "University calendar and important dates"))
        self.player.add_item(AdmissionItem("Digital Timetable", "Your personalized lecture schedule"))
        self.player.add_item(AdmissionItem("First Checkpoint Token", "Allows you to save progress"))
        self.missions.start_mission("year1_admission")
        self.calendar.current_event = "Registration"

    def update(self):
        if self.stage == 0:
            self.start_admission()

    def is_completed(self):
        return self.stage >= 1


class AdmissionItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def serialize(self):
        return {"name": self.name, "description": self.description}

    def __str__(self):
        return self.name
