import pygame
from src.config import SCREEN_WIDTH, WHITE, BLACK, CYAN, YELLOW, GREEN, RED, LIGHT_GRAY


class HUD:
    def __init__(self, player, calendar, mission_system):
        self.player = player
        self.calendar = calendar
        self.mission_system = mission_system
        self.font = pygame.font.Font(None, 20)
        self.small_font = pygame.font.Font(None, 16)

    def render(self, screen, paused):
        if paused:
            return

        info_items = [
            f"{self.player.name} | {self.player.academic_year}",
            f"{self.calendar.get_day_name()} | {self.calendar.get_current_event()}",
            f"{self.calendar.get_semester_progress()}",
            f"Active Missions: {self.mission_system.get_active_mission_count()}",
        ]
        y = 8
        for item in info_items:
            text = self.font.render(item, True, WHITE)
            shadow = self.font.render(item, True, BLACK)
            screen.blit(shadow, (9, y + 1))
            screen.blit(text, (8, y))
            y += 22

        if self.mission_system.active_missions:
            y = screen.get_height() - 60
            pygame.draw.rect(screen, BLACK, (0, y, 300, 60))
            pygame.draw.rect(screen, WHITE, (0, y, 300, 60), 1)
            mission = self.mission_system.active_missions[0]
            title = self.small_font.render(f"Mission: {mission.title}", True, CYAN)
            progress = self.small_font.render(
                f"Progress: {mission.progress}/{len(mission.objectives)}", True, LIGHT_GRAY)
            screen.blit(title, (5, y + 2))
            screen.blit(progress, (5, y + 20))
            bar_width = 280
            fill = (mission.progress / len(mission.objectives)) * bar_width if mission.objectives else 0
            pygame.draw.rect(screen, DARK_GRAY := (40, 40, 40), (10, y + 38, bar_width, 8))
            pygame.draw.rect(screen, GREEN, (10, y + 38, int(fill), 8))
