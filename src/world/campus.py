from src.world.location import Location
from src.world.building import Building
from src.config import BROWN, SKY_BLUE, GRASS_GREEN, PATH_GRAY


class Campus:
    def __init__(self):
        self.width = 3200
        self.height = 2400
        self.buildings = []
        self.locations = []
        self.walkable_tiles = set()
        self._generate()

    def _generate(self):
        self._add_walkable_tiles()
        self._add_buildings()
        self._add_locations()

    def _add_walkable_tiles(self):
        for x in range(0, self.width, 32):
            for y in range(0, self.height, 32):
                self.walkable_tiles.add((x, y))

    def _add_buildings(self):
        building_data = [
            ("Administration", 200, 200, 200, 150, (139, 69, 19)),
            ("Library", 600, 150, 250, 200, (100, 50, 150)),
            ("Lecture Theatre A", 1200, 200, 300, 180, (70, 70, 70)),
            ("Lecture Theatre B", 1700, 200, 300, 180, (90, 90, 90)),
            ("Innovation Hub", 2200, 180, 240, 200, (0, 150, 200)),
            ("Computer Lab", 200, 500, 200, 150, (50, 100, 200)),
            ("Laboratory A", 600, 500, 180, 150, (200, 100, 50)),
            ("Laboratory B", 1000, 500, 180, 150, (200, 150, 50)),
            ("Engineering Workshop", 1400, 500, 250, 200, (180, 100, 50)),
            ("Student Centre", 1800, 500, 220, 180, (50, 180, 50)),
            ("Health Centre", 2200, 500, 180, 150, (200, 50, 50)),
            ("Cafeteria", 200, 800, 200, 150, (200, 150, 50)),
            ("Bookshop", 600, 800, 150, 120, (100, 150, 200)),
            ("Bank", 1000, 800, 150, 120, (150, 150, 50)),
            ("Hostel Block A", 1400, 800, 200, 200, (150, 100, 50)),
            ("Hostel Block B", 1800, 800, 200, 200, (180, 120, 60)),
            ("Sports Complex", 2200, 800, 300, 250, (50, 150, 50)),
            ("Bus Terminal", 200, 1100, 250, 100, (100, 100, 100)),
            ("Car Park", 600, 1100, 300, 100, (80, 80, 80)),
            ("Main Gate", 1050, 1200, 200, 50, (139, 69, 19)),
        ]

        for name, x, y, w, h, color in building_data:
            building = Building(name, x, y, w, h, color)
            self.buildings.append(building)

            for bx in range(x, x + w, 32):
                for by in range(y, y + h, 32):
                    self.walkable_tiles.discard((bx, by))

    def _add_locations(self):
        loc_data = [
            ("Administration Office", 220, 220, 160, 110, "admin", BROWN),
            ("Library Reading Room", 620, 170, 210, 160, "library", (100, 50, 150)),
            ("Lecture Theatre A Hall", 1220, 220, 260, 140, "lecture", (70, 70, 70)),
            ("Lecture Theatre B Hall", 1720, 220, 260, 140, "lecture", (90, 90, 90)),
            ("Innovation Lab", 2220, 200, 200, 160, "hub", (0, 150, 200)),
            ("Computer Science Lab", 220, 520, 160, 110, "lab", (50, 100, 200)),
            ("Engineering Workshop Floor", 1420, 520, 210, 160, "workshop", (180, 100, 50)),
            ("Student Lounge", 1820, 520, 180, 140, "social", (50, 180, 50)),
            ("Clinic", 2220, 520, 140, 110, "health", (200, 50, 50)),
            ("Cafeteria Hall", 220, 820, 160, 110, "dining", (200, 150, 50)),
            ("Bookshop Store", 620, 820, 110, 80, "shop", (100, 150, 200)),
            ("Bank Hall", 1020, 820, 110, 80, "bank", (150, 150, 50)),
            ("Hostel Block A Dorm", 1420, 820, 160, 160, "hostel", (150, 100, 50)),
            ("Hostel Block B Dorm", 1820, 820, 160, 160, "hostel", (180, 120, 60)),
            ("Sports Field", 2220, 820, 260, 210, "sports", (50, 150, 50)),
            ("Bus Stop", 220, 1120, 210, 60, "transport", (100, 100, 100)),
            ("Parking Area", 620, 1120, 260, 60, "parking", (80, 80, 80)),
            ("University Entrance", 1050, 1220, 200, 30, "entrance", (139, 69, 19)),
        ]

        for name, x, y, w, h, ltype, color in loc_data:
            location = Location(name, x, y, w, h, ltype, color)
            self.locations.append(location)

    def is_walkable(self, x, y, width, height):
        margin = 4
        check_points = [
            (x + margin, y + margin),
            (x + width - margin, y + margin),
            (x + margin, y + height - margin),
            (x + width - margin, y + height - margin)
        ]
        for px, py in check_points:
            tile_x = int(px // 32) * 32
            tile_y = int(py // 32) * 32
            if (tile_x, tile_y) not in self.walkable_tiles:
                return False
            if px < 0 or py < 0 or px >= self.width or py >= self.height:
                return False
        return True

    def get_location_at(self, x, y):
        for location in self.locations:
            if location.contains_point(x, y):
                return location
        return None

    def get_building_at(self, x, y):
        for building in self.buildings:
            if building.contains_point(x, y):
                return building
        return None

    def serialize(self):
        return {
            "width": self.width,
            "height": self.height,
            "buildings": [b.serialize() for b in self.buildings],
            "locations": [l.serialize() for l in self.locations],
            "walkable_tiles": list(self.walkable_tiles)
        }

    @staticmethod
    def deserialize(data):
        campus = Campus.__new__(Campus)
        campus.width = data["width"]
        campus.height = data["height"]
        campus.buildings = [Building.deserialize(b) for b in data["buildings"]]
        campus.locations = [Location.deserialize(l) for l in data["locations"]]
        campus.walkable_tiles = set(tuple(t) for t in data["walkable_tiles"])
        return campus
