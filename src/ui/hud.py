import pygame
from src.config import WHITE, BLACK, CYAN, YELLOW, GREEN, RED, LIGHT_GRAY


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

        panel_w = 280
        y = 8
        for item in [
            f"{self.player.name} | {self.player.academic_year}",
            f"{self.calendar.get_day_name()} | {self.calendar.get_current_event()}",
            f"{self.calendar.get_semester_progress()}",
            f"Active Missions: {self.mission_system.get_active_mission_count()}",
        ]:
            text = self.font.render(item, True, WHITE)
            shadow = self.font.render(item, True, BLACK)
            screen.blit(shadow, (9, y + 1))
            screen.blit(text, (8, y))
            y += 22

        if self.mission_system.active_missions:
            y = screen.get_height() - 65
            pygame.draw.rect(screen, (0, 0, 0, 180), (0, y, panel_w + 20, 65))
            pygame.draw.rect(screen, (60, 60, 80), (0, y, panel_w + 20, 65), 1)
            mission = self.mission_system.active_missions[0]
            title = self.small_font.render(f"[MISSION] {mission.title}", True, CYAN)
            progress = self.small_font.render(
                f"Progress: {mission.progress}/{len(mission.objectives)}", True, LIGHT_GRAY)
            screen.blit(title, (10, y + 5))
            screen.blit(progress, (10, y + 22))
            bar_width = panel_w
            fill = (mission.progress / len(mission.objectives)) * bar_width if mission.objectives else 0
            pygame.draw.rect(screen, (40, 40, 40), (10, y + 42, bar_width, 10), border_radius=5)
            if fill > 0:
                pygame.draw.rect(screen, GREEN, (10, y + 42, int(fill), 10), border_radius=5)
