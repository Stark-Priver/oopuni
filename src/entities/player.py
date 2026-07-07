import pygame
from src.config import PLAYER_SPEED, TILE_SIZE


class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.speed = PLAYER_SPEED
        self.facing = "down"
        self.animation_frame = 0
        self.current_location = None
        self.registration_number = ""
        self.faculty = ""
        self.department = ""
        self.academic_year = "Year One"
        self.email = ""
        self.student_id = ""
        self.inventory = []
        self.attendance = 100
        self.marks = 0
        self.scholarship = False
        self.discovered_locations = set()
        self.completed_tutorials = []
        self.story_flags = {}
        self.dialogue_choices = {}
        self.width = TILE_SIZE
        self.height = TILE_SIZE

    def update(self, keys, campus, dt):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -self.speed
            self.facing = "left"
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = self.speed
            self.facing = "right"
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -self.speed
            self.facing = "up"
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = self.speed
            self.facing = "down"

        if dx != 0 or dy != 0:
            self.animation_frame += 1

        new_x = self.x + dx
        new_y = self.y + dy

        if campus.is_walkable(new_x, new_y, self.width, self.height):
            self.x = new_x
            self.y = new_y

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def add_item(self, item):
        self.inventory.append(item)

    def has_item(self, item_name):
        return any(item.name == item_name for item in self.inventory)

    def discover_location(self, location_name):
        self.discovered_locations.add(location_name)

    def serialize(self):
        return {
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "facing": self.facing,
            "registration_number": self.registration_number,
            "faculty": self.faculty,
            "department": self.department,
            "academic_year": self.academic_year,
            "email": self.email,
            "student_id": self.student_id,
            "inventory": [item.serialize() if hasattr(item, "serialize") else {"name": str(item)} for item in self.inventory],
            "attendance": self.attendance,
            "marks": self.marks,
            "scholarship": self.scholarship,
            "discovered_locations": list(self.discovered_locations),
            "completed_tutorials": self.completed_tutorials,
            "story_flags": self.story_flags,
            "dialogue_choices": self.dialogue_choices,
            "current_location": self.current_location.name if self.current_location else None
        }

    @staticmethod
    def deserialize(data):
        player = Player(data["name"], data["x"], data["y"])
        player.facing = data["facing"]
        player.registration_number = data["registration_number"]
        player.faculty = data["faculty"]
        player.department = data["department"]
        player.academic_year = data["academic_year"]
        player.email = data["email"]
        player.student_id = data["student_id"]
        player.attendance = data["attendance"]
        player.marks = data["marks"]
        player.scholarship = data["scholarship"]
        player.discovered_locations = set(data["discovered_locations"])
        player.completed_tutorials = data["completed_tutorials"]
        player.story_flags = data["story_flags"]
        player.dialogue_choices = data["dialogue_choices"]
        return player
