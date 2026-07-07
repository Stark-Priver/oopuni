import os
import pygame


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
SAVES_DIR = os.path.join(BASE_DIR, "saves")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILE_SIZE = 32
FPS = 60

PLAYER_SPEED = 3
NPC_SPEED = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 100, 255)
YELLOW = (255, 255, 50)
PURPLE = (180, 50, 255)
ORANGE = (255, 150, 50)
CYAN = (50, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (40, 40, 40)
LIGHT_GRAY = (200, 200, 200)
BROWN = (139, 69, 19)
SKY_BLUE = (135, 206, 235)
GRASS_GREEN = (34, 139, 34)
PATH_GRAY = (180, 180, 160)

COLOR_KEY = (255, 0, 255)

ACADEMIC_YEARS = ["Year One", "Year Two", "Year Three", "Year Four"]
SEMESTERS = ["Semester One", "Semester Two"]

DEPARTMENTS = [
    "Computer Science", "Software Engineering", "Civil Engineering",
    "Electrical Engineering", "Mechanical Engineering", "Architecture",
    "Business", "Education", "Agriculture", "Laboratory Sciences"
]

CAMPUS_LOCATIONS = [
    "Administration", "Library", "Lecture Theatre A", "Lecture Theatre B",
    "Innovation Hub", "Laboratory A", "Laboratory B", "Hostel Block A",
    "Hostel Block B", "Student Centre", "Health Centre", "Bookshop",
    "Bank", "Sports Complex", "Engineering Workshop", "Computer Lab",
    "Cafeteria", "Main Gate", "Bus Terminal", "Car Park"
]

SAVE_SLOTS = 5
AUTOSAVE_INTERVAL = 300
