class GameTimer:
    def __init__(self):
        self.total_seconds = 0
        self.minutes = 0
        self.hours = 8
        self.days = 1
        self.time_scale = 60

    def update(self, dt):
        self.total_seconds += dt * self.time_scale / 1000
        total_minutes = int(self.total_seconds // 60)
        self.hours = (total_minutes // 60 + 8) % 24
        self.minutes = total_minutes % 60
        self.days = total_minutes // (24 * 60) + 1

    def get_time_string(self):
        period = "AM" if self.hours < 12 else "PM"
        h = self.hours if self.hours <= 12 else self.hours - 12
        if h == 0:
            h = 12
        return f"{h:02d}:{self.minutes:02d} {period}"

    def get_day_string(self):
        return f"Day {self.days}"

    def is_night(self):
        return self.hours < 6 or self.hours >= 18

    def serialize(self):
        return {"total_seconds": self.total_seconds, "days": self.days}

    @staticmethod
    def deserialize(data):
        timer = GameTimer()
        timer.total_seconds = data["total_seconds"]
        timer.days = data["days"]
        total_minutes = int(timer.total_seconds // 60)
        timer.hours = (total_minutes // 60 + 8) % 24
        timer.minutes = total_minutes % 60
        return timer
