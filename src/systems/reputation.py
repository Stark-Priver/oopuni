class ReputationSystem:
    def __init__(self):
        self.reputation = {
            "Lecturers": 50,
            "Departments": 50,
            "Student Government": 50,
            "Library": 50,
            "Innovation Hub": 50,
            "Sports": 50,
            "Research Office": 50,
            "Career Centre": 50
        }

    def add_reputation(self, faction, amount):
        if faction in self.reputation:
            self.reputation[faction] = max(0, min(100, self.reputation[faction] + amount))

    def get_reputation(self, faction):
        return self.reputation.get(faction, 0)

    def get_all_reputations(self):
        return dict(self.reputation)

    def get_average_reputation(self):
        return sum(self.reputation.values()) / len(self.reputation) if self.reputation else 0

    def get_standing(self, faction):
        rep = self.get_reputation(faction)
        if rep >= 80:
            return "Excellent"
        elif rep >= 60:
            return "Good"
        elif rep >= 40:
            return "Neutral"
        elif rep >= 20:
            return "Poor"
        else:
            return "Hostile"

    def serialize(self):
        return {"reputation": self.reputation}

    @staticmethod
    def deserialize(data):
        system = ReputationSystem()
        system.reputation = data["reputation"]
        return system
