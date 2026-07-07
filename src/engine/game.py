import pygame
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK, SAVE_SLOTS
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


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("OOP UNI: The Journey Through MUST")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "menu"

        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
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
        pygame.display.flip()

    def _check_location_interactions(self):
        current_loc = self.campus.get_location_at(self.player.x, self.player.y)
        if current_loc and current_loc != self.player.current_location:
            self.player.current_location = current_loc
            self.mission_system.on_location_entered(current_loc.name)
            if current_loc.name == "Administration":
                self.dialog.show_message("Administration Office", "Welcome to Administration. New students report here for registration.")
            elif current_loc.name == "Library":
                self.dialog.show_message("Library", "Welcome to the Library. Knowledge is power — and objects.")

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
        self.screen.fill(BLACK)
        font = pygame.font.Font(None, 48)
        text = font.render("The Object Framework has been restored.", True, (255, 255, 255))
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        text2 = font.render("You are a Software Engineer.", True, (100, 200, 255))
        self.screen.blit(text2, (SCREEN_WIDTH // 2 - text2.get_width() // 2, SCREEN_HEIGHT // 2 + 20))
        text3 = pygame.font.Font(None, 24).render("Press ENTER to return to menu", True, (200, 200, 200))
        self.screen.blit(text3, (SCREEN_WIDTH // 2 - text3.get_width() // 2, SCREEN_HEIGHT // 2 + 80))
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
