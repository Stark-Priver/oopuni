import pygame


class DialogSystem:
    def __init__(self):
        self.visible = False
        self.title = ""
        self.text = ""
        self.queue = []
        self.history = []

    def show_message(self, title, text):
        self.title = title
        self.text = text
        self.visible = True
        self.history.append({"title": title, "text": text})

    def show_welcome_message(self, player):
        self.queue = [
            ("Professor Object", "...Welcome, new student. I have been watching you."),
            ("Professor Object", "I am Professor Object, guardian of the Object Framework."),
            ("Professor Object", "This university runs on code. Every student, every building, every system is an object."),
            ("Professor Object", "A Chaos Bug is spreading through the framework. I need your help to restore it."),
            ("Professor Object", "But first... you must learn. Explore the campus. Discover how objects work."),
            ("Professor Object", "Begin at the Administration building. Your journey starts now."),
            ("System", "Mission Added: The Admission Letter"),
        ]
        self.advance_queue()

    def advance_queue(self):
        if self.queue:
            self.title, self.text = self.queue.pop(0)
            self.visible = True
            self.history.append({"title": self.title, "text": self.text})
        else:
            self.visible = False

    def handle_event(self, event):
        if self.visible and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.queue:
                    self.advance_queue()
                else:
                    self.visible = False

    def serialize(self):
        return {"history": self.history[-50:]}

    @staticmethod
    def deserialize(data):
        dialog = DialogSystem()
        dialog.history = data.get("history", [])
        return dialog
