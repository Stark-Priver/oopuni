import pygame
from src.config import WHITE, BLACK, BLUE, CYAN, LIGHT_GRAY


class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.Font(None, 52)
        self.font_option = pygame.font.Font(None, 34)
        self.font_hint = pygame.font.Font(None, 20)
        self.selected = 0
        self.options = ["Resume", "Save Game", "Load Game", "Quit to Menu", "Quit to Desktop"]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.selected == 0:
                    return "resume"
                elif self.selected == 1:
                    return "save"
                elif self.selected == 2:
                    return "load"
                elif self.selected == 3:
                    return "quit_menu"
                elif self.selected == 4:
                    return "quit_desktop"
            elif event.key == pygame.K_ESCAPE:
                return "resume"
        return None

    def render(self):
        sw, sh = self.screen.get_width(), self.screen.get_height()

        overlay = pygame.Surface((sw, sh))
        overlay.set_alpha(160)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))

        panel_w = 400
        panel_h = 50 + len(self.options) * 55
        px = (sw - panel_w) // 2
        py = (sh - panel_h) // 2
        pygame.draw.rect(self.screen, (20, 20, 45), (px, py, panel_w, panel_h), border_radius=12)
        pygame.draw.rect(self.screen, (60, 60, 100), (px, py, panel_w, panel_h), 2, border_radius=12)

        title = self.font_title.render("PAUSED", True, CYAN)
        self.screen.blit(title, (sw // 2 - title.get_width() // 2, py + 15))

        for i, option in enumerate(self.options):
            color = CYAN if i == self.selected else LIGHT_GRAY
            text = self.font_option.render(option, True, color)
            ox = sw // 2 - text.get_width() // 2
            oy = py + 60 + i * 50
            if i == self.selected:
                sel_rect = pygame.Rect(px + 20, oy - 6, panel_w - 40, 40)
                pygame.draw.rect(self.screen, (30, 30, 70), sel_rect, border_radius=6)
                pygame.draw.rect(self.screen, (0, 120, 200), sel_rect, 2, border_radius=6)
            self.screen.blit(text, (ox, oy))

        hint = self.font_hint.render("ESC to resume", True, (120, 120, 140))
        self.screen.blit(hint, (sw // 2 - hint.get_width() // 2, py + panel_h + 15))
