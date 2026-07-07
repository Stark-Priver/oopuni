class Building:
    def __init__(self, name, x, y, width, height, color):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.entrance_x = x + width // 2
        self.entrance_y = y + height
        self.floors = 1
        self.locations = []

    def add_location(self, location):
        self.locations.append(location)

    def get_entrance(self):
        return (self.entrance_x, self.entrance_y)

    def contains_point(self, px, py):
        return (self.x <= px <= self.x + self.width and
                self.y <= py <= self.y + self.height)

    def serialize(self):
        return {
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "color": self.color,
            "floors": self.floors,
            "locations": [loc.serialize() for loc in self.locations]
        }

    @staticmethod
    def deserialize(data):
        building = Building(data["name"], data["x"], data["y"],
                           data["width"], data["height"], data["color"])
        building.floors = data["floors"]
        building.locations = [Location.deserialize(loc) for loc in data["locations"]]
        return building
