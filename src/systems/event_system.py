class Event:
    def __init__(self, event_id, name, description, trigger_condition, effects):
        self.event_id = event_id
        self.name = name
        self.description = description
        self.trigger_condition = trigger_condition
        self.effects = effects
        self.triggered = False

    def check_trigger(self, game_state):
        if not self.triggered:
            for key, value in self.trigger_condition.items():
                if game_state.get(key) != value:
                    return False
            self.triggered = True
            return True
        return False


class EventSystem:
    def __init__(self):
        self.events = []

    def register(self, event):
        self.events.append(event)

    def update(self, game_state):
        triggered = []
        for event in self.events:
            if event.check_trigger(game_state):
                triggered.append(event)
        return triggered
