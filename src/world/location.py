class Location:
    def __init__(self, name, x, y, width, height, location_type, color, description=""):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = location_type
        self.color = color
        self.description = description
        self.is_visited = False
        self.is_locked = False
        self.interactions = []

    def get_center(self):
        return (self.x + self.width // 2, self.y + self.height // 2)

    def contains_point(self, px, py):
        return (self.x <= px <= self.x + self.width and
                self.y <= py <= self.y + self.height)

    def add_interaction(self, interaction):
        self.interactions.append(interaction)

    def serialize(self):
        return {
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "type": self.type,
            "color": self.color,
            "description": self.description,
            "is_visited": self.is_visited,
            "is_locked": self.is_locked
        }

    @staticmethod
    def deserialize(data):
        loc = Location(data["name"], data["x"], data["y"],
                       data["width"], data["height"],
                       data["type"], data["color"],
                       data["description"])
        loc.is_visited = data["is_visited"]
        loc.is_locked = data["is_locked"]
        return loc
