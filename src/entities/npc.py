import pygame
from src.config import NPC_SPEED, TILE_SIZE


class NPC:
    def __init__(self, name, x, y, role, color):
        self.name = name
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.role = role
        self.color = color
        self.speed = NPC_SPEED
        self.facing = "down"
        self.dialogues = []
        self.current_dialogue_index = 0
        self.schedule = []
        self.current_schedule_index = 0
        self.wait_timer = 0
        self.is_moving = False
        self.width = TILE_SIZE
        self.height = TILE_SIZE

    def update(self, campus, dt):
        if self.wait_timer > 0:
            self.wait_timer -= dt
            return

        if self.schedule and len(self.schedule) > self.current_schedule_index:
            target = self.schedule[self.current_schedule_index]
            tx, ty, wait = target
            dx = tx - self.x
            dy = ty - self.y
            dist = (dx * dx + dy * dy) ** 0.5

            if dist > self.speed:
                self.x += (dx / dist) * self.speed
                self.y += (dy / dist) * self.speed
                if abs(dx) > abs(dy):
                    self.facing = "right" if dx > 0 else "left"
                else:
                    self.facing = "down" if dy > 0 else "up"
                self.is_moving = True
            else:
                self.x, self.y = tx, ty
                self.wait_timer = wait
                self.current_schedule_index = (self.current_schedule_index + 1) % len(self.schedule)
                self.is_moving = False

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def set_dialogues(self, dialogues):
        self.dialogues = dialogues

    def get_current_dialogue(self):
        if self.dialogues:
            return self.dialogues[self.current_dialogue_index % len(self.dialogues)]
        return f"Hello, I am {self.name}."

    def advance_dialogue(self):
        self.current_dialogue_index += 1

    def serialize(self):
        return {
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "role": self.role,
            "color": self.color,
            "facing": self.facing,
            "current_dialogue_index": self.current_dialogue_index,
            "current_schedule_index": self.current_schedule_index,
            "wait_timer": self.wait_timer,
            "schedule": self.schedule
        }

    @staticmethod
    def deserialize(data):
        npc = NPC(data["name"], data["x"], data["y"], data["role"], data["color"])
        npc.facing = data["facing"]
        npc.current_dialogue_index = data["current_dialogue_index"]
        npc.current_schedule_index = data["current_schedule_index"]
        npc.wait_timer = data["wait_timer"]
        npc.schedule = data["schedule"]
        return npc
