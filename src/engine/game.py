import pygame
from src.config import FPS, BLACK, SAVE_SLOTS
from src.engine.camera import Camera
from src.engine.timer import GameTimer
from src.entities.player import Player
from src.world.campus import Campus
from src.world.npc_scheduler import NPCScheduler
from src.systems.save_system import SaveSystem
from src.systems.calendar import AcademicCalendar
from src.systems.timetable import Timetable
from src.systems.reputation import ReputationSystem
from src.systems.mission import MissionSystem
from src.ui.renderer import Renderer
from src.ui.menu import MainMenu
from src.ui.hud import HUD
from src.ui.dialog import DialogSystem
from src.ui.save_menu import SaveMenu
from src.ui.tkinter_gui import TkinterGUI


LOCATION_MISSION_KEYWORDS = {
    "Administration Office": "Administration",
    "Library Reading Room": "Library",
    "Student Lounge": "Student Centre",
    "Cafeteria Hall": "Cafeteria",
    "Lecture Theatre A Hall": "Lecture Theatre A",
    "Lecture Theatre B Hall": "Lecture Theatre",
    "Hostel Block A Dorm": "Hostel",
    "Hostel Block B Dorm": "Hostel",
}


class Game:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.fullscreen = True
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        pygame.display.set_caption("OOP UNI: The Journey Through MUST")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "menu"

        self.camera = Camera(self.screen_width, self.screen_height)
        self.game_timer = GameTimer()
        self.player = Player("New Student", 400, 300)
        self.campus = Campus()
        self.npc_scheduler = NPCScheduler(self.campus)
        self.calendar = AcademicCalendar()
        self.timetable = Timetable(self.calendar)
        self.reputation = ReputationSystem()
        self.mission_system = MissionSystem()
        self.save_system = SaveSystem()
        self.renderer = Renderer(self.screen)
        self.main_menu = MainMenu(self.screen)
        self.hud = HUD(self.player, self.calendar, self.mission_system)
        self.dialog = DialogSystem()
        self.save_menu = SaveMenu(self.screen, self.save_system)
        self.tkinter_gui = TkinterGUI(self)
        self.paused = False
        self.interact_prompt_timer = 0
        self.show_interact_prompt = False
        self.location_entry_dialog_shown = False

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS)
            if self.state == "menu":
                self._handle_menu_state(dt)
            elif self.state == "playing":
                self._handle_playing_state(dt)
            elif self.state == "save_menu":
                self._handle_save_menu_state(dt)
            elif self.state == "game_over":
                self._handle_game_over_state(dt)
        pygame.quit()

    def _handle_menu_state(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            result = self.main_menu.handle_event(event)
            if result == "new_game":
                self._start_new_game()
            elif result == "load_game":
                self._open_load_menu()
            elif result == "quit":
                self.running = False
        self.main_menu.render()
        pygame.display.flip()

    def _start_new_game(self):
        self.state = "playing"
        self.player = Player("New Student", 400, 300)
        self.calendar.reset()
        self.mission_system = MissionSystem()
        self.reputation = ReputationSystem()
        self.dialog.show_welcome_message(self.player)
        self.save_system.autosave(self._build_save_data())

    def _open_load_menu(self):
        self.state = "save_menu"
        self.save_menu.set_mode("load")

    def _handle_playing_state(self, dt):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                elif event.key == pygame.K_F5:
                    self._quick_save()
                elif event.key == pygame.K_F9:
                    self._quick_load()
                elif event.key == pygame.K_TAB:
                    self._open_save_menu()
                elif event.key == pygame.K_i:
                    self.tkinter_gui.show_player_info(self.player)
                elif event.key == pygame.K_m:
                    self.tkinter_gui.show_map(self.campus)
                elif event.key == pygame.K_j:
                    self.tkinter_gui.show_missions(self.mission_system)
                elif event.key == pygame.K_c:
                    self.tkinter_gui.show_calendar(self.calendar, self.timetable)
                elif event.key == pygame.K_r:
                    self.tkinter_gui.show_reputation(self.reputation)
                elif event.key == pygame.K_e:
                    self._interact_with_location()

            self.dialog.handle_event(event)
            self.tkinter_gui.process_events()

        if not self.paused:
            self.player.update(keys, self.campus, dt)
            self.camera.update(self.player)
            self.npc_scheduler.update(dt, self.game_timer)
            self.game_timer.update(dt)
            self.calendar.update(dt)
            self.timetable.update()
            self.mission_system.update(self.player, self.calendar)
            self._check_location_interactions()

        self.renderer.clear()
        self.renderer.draw_campus(self.campus, self.camera)
        self.renderer.draw_npcs(self.npc_scheduler.get_all_npcs(), self.camera)
        self.renderer.draw_player(self.player, self.camera)
        self.renderer.draw_dialog(self.dialog)
        self.hud.render(self.screen, self.paused)
        if self.paused:
            self.renderer.draw_pause_overlay()
        if self.show_interact_prompt and not self.dialog.visible:
            self.renderer.draw_interact_prompt(self.player, self.campus)
        pygame.display.flip()

    def _get_location_keyword(self, loc_name):
        return LOCATION_MISSION_KEYWORDS.get(loc_name, loc_name)

    def _check_location_interactions(self):
        current_loc = self.campus.get_location_at(self.player.x, self.player.y)
        self.show_interact_prompt = current_loc is not None
        if current_loc and current_loc != self.player.current_location:
            self.player.current_location = current_loc
            keyword = self._get_location_keyword(current_loc.name)
            self.mission_system.on_location_entered(keyword)
            self.player.discover_location(current_loc.name)
            current_loc.is_visited = True
            self.location_entry_dialog_shown = False

            if current_loc.name == "Administration Office":
                self.dialog.show_message("Administration Office",
                    "Welcome to Administration. New students report here for registration. Press E to interact.")
                if not self.mission_system.is_mission_active("year1_admission"):
                    self.mission_system.start_mission("year1_admission")
            elif current_loc.name == "Library Reading Room":
                self.dialog.show_message("Library",
                    "Welcome to the Library. Knowledge is power — and objects. Press E to browse books.")
                if not self.mission_system.is_mission_active("year1_borrow_book"):
                    self.mission_system.start_mission("year1_borrow_book")
            elif "Lecture Theatre" in current_loc.name:
                self.dialog.show_message(current_loc.name,
                    "A lecture is in progress. Press E to attend.")
                if not self.mission_system.is_mission_active("year1_first_class") and \
                   self.mission_system.is_mission_completed("year1_admission"):
                    self.mission_system.start_mission("year1_first_class")
            else:
                self.dialog.show_message(current_loc.name,
                    f"You have discovered {current_loc.name}. Press E to interact.")
                if not self.mission_system.is_mission_active("year1_orientation") and \
                   self.mission_system.is_mission_completed("year1_admission"):
                    self.mission_system.start_mission("year1_orientation")

    def _interact_with_location(self):
        if self.dialog.visible:
            return
        current_loc = self.campus.get_location_at(self.player.x, self.player.y)
        if not current_loc:
            self.dialog.show_message("Info", "There is nothing to interact with here.")
            return

        if current_loc.name == "Administration Office":
            if not self.player.registration_number:
                self.player.student_id = f"MUST-{self.calendar.year}{self.calendar.semester}-{hash(self.player.name) % 10000:04d}"
                self.player.registration_number = self.player.student_id
                self.player.faculty = "Science and Technology"
                self.player.department = "Computer Science"
                self.player.email = f"{self.player.name.lower().replace(' ', '.')}@must.ac.tz"
                self.reputation.add_reputation("Administration", 10)
                if not self.mission_system.is_mission_completed("year1_admission"):
                    for m in self.mission_system.active_missions:
                        if m.mission_id == "year1_admission":
                            m.progress = len(m.objectives)
                    self.mission_system.complete_mission("year1_admission")
                self.dialog.show_message("Registration Complete",
                    f"Welcome to MUST, {self.player.name}!\n\n"
                    f"Student ID: {self.player.student_id}\n"
                    f"Faculty: {self.player.faculty}\n"
                    f"Department: {self.player.department}\n"
                    f"Email: {self.player.email}\n\n"
                    "Mission 'The Admission Letter' completed!\n"
                    "Press J to view your next missions.")
            else:
                self.dialog.show_message("Administration Office",
                    "You are already registered. Your details are on file.")
        elif current_loc.name == "Library Reading Room":
            self.dialog.show_message("Library",
                "You browse the shelves and find a book on OOP Principles.\n"
                "You check it out using your student ID.")
            self.player.add_item(type("Item", (), {"name": "OOP Principles Book"})())
            self.mission_system.on_location_entered("Library")
        elif "Lecture Theatre" in current_loc.name:
            self.dialog.show_message("Lecture",
                "You attend the lecture. The professor explains OOP concepts.\n"
                "Objects, classes, inheritance — it all starts to make sense.")
            self.mission_system.on_location_entered("Lecture Theatre A")
        elif current_loc.name == "Cafeteria Hall":
            self.dialog.show_message("Cafeteria",
                "You grab a meal and meet fellow students. They share tips about campus life.")
            self.mission_system.on_location_entered("Cafeteria")
        elif current_loc.name == "Student Lounge":
            self.dialog.show_message("Student Centre",
                "Senior students welcome you. They explain the orientation schedule.")
            self.mission_system.on_location_entered("Student Centre")
        elif "Hostel" in current_loc.name:
            self.dialog.show_message(current_loc.name,
                "You check out the hostel facilities. This will be your home for the next few years.")
            self.mission_system.on_location_entered("Hostel")
        else:
            self.dialog.show_message(current_loc.name,
                f"You explore {current_loc.name}. There's much to discover at MUST!")

    def _handle_save_menu_state(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            result = self.save_menu.handle_event(event)
            if result == "back":
                self.state = "playing"
            elif result and isinstance(result, dict):
                if "save" in result:
                    self.save_system.save(result["slot"], self._build_save_data())
                    self.state = "playing"
                elif "load" in result:
                    data = self.save_system.load(result["slot"])
                    if data:
                        self._restore_save_data(data)
                    self.state = "playing"
        self.save_menu.render()
        pygame.display.flip()

    def _handle_game_over_state(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.state = "menu"
        sw, sh = self.screen.get_width(), self.screen.get_height()
        self.screen.fill(BLACK)
        font = pygame.font.Font(None, 48)
        text = font.render("The Object Framework has been restored.", True, (255, 255, 255))
        self.screen.blit(text, (sw // 2 - text.get_width() // 2, sh // 2 - 50))
        text2 = font.render("You are a Software Engineer.", True, (100, 200, 255))
        self.screen.blit(text2, (sw // 2 - text2.get_width() // 2, sh // 2 + 20))
        text3 = pygame.font.Font(None, 24).render("Press ENTER to return to menu", True, (200, 200, 200))
        self.screen.blit(text3, (sw // 2 - text3.get_width() // 2, sh // 2 + 80))
        pygame.display.flip()

    def _build_save_data(self):
        return {
            "player": self.player.serialize(),
            "calendar": self.calendar.serialize(),
            "timetable": self.timetable.serialize(),
            "reputation": self.reputation.serialize(),
            "missions": self.mission_system.serialize(),
            "campus": self.campus.serialize(),
            "npc_scheduler": self.npc_scheduler.serialize(),
            "game_timer": self.game_timer.serialize(),
            "dialogue_history": self.dialog.serialize(),
            "version": "1.0.0"
        }

    def _restore_save_data(self, data):
        self.player = Player.deserialize(data["player"])
        self.calendar = AcademicCalendar.deserialize(data["calendar"])
        self.timetable = Timetable.deserialize(data["timetable"])
        self.reputation = ReputationSystem.deserialize(data["reputation"])
        self.mission_system = MissionSystem.deserialize(data["missions"])
        self.campus = Campus.deserialize(data["campus"])
        self.npc_scheduler = NPCScheduler.deserialize(data["npc_scheduler"], self.campus)
        self.game_timer = GameTimer.deserialize(data["game_timer"])
        self.dialog = DialogSystem.deserialize(data["dialogue_history"])
        self.hud = HUD(self.player, self.calendar, self.mission_system)

    def _quick_save(self):
        self.save_system.quick_save(self._build_save_data())
        self.dialog.show_message("Quick Save", "Game saved. Press F9 to load.")

    def _quick_load(self):
        data = self.save_system.quick_load()
        if data:
            self._restore_save_data(data)
            self.dialog.show_message("Quick Load", "Save restored successfully.")

    def _open_save_menu(self):
        self.state = "save_menu"
        self.save_menu.set_mode("save")
