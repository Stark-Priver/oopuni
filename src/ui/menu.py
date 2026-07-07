import pygame
from src.config import WHITE, BLACK, BLUE, CYAN, LIGHT_GRAY


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.Font(None, 72)
        self.font_subtitle = pygame.font.Font(None, 28)
        self.font_menu = pygame.font.Font(None, 36)
        self.font_hint = pygame.font.Font(None, 20)
        self.selected = 0
        self.options = ["New Game", "Load Game", "Quit"]
        self.title = "OOP UNI"
        self.subtitle = "The Journey Through MUST"

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.selected == 0:
                    return "new_game"
                elif self.selected == 1:
                    return "load_game"
                elif self.selected == 2:
                    return "quit"
        return None

    def render(self):
        self.screen.fill((10, 10, 30))

        sw, sh = self.screen.get_width(), self.screen.get_height()
        for y_offset in range(0, sh, 4):
            shade = max(0, 255 - y_offset // 6)
            pygame.draw.line(self.screen, (shade // 3, shade // 3, shade), (0, y_offset), (sw, y_offset))

        title_shadow = self.font_title.render(self.title, True, (0, 100, 200))
        title_text = self.font_title.render(self.title, True, CYAN)
        subtitle_text = self.font_subtitle.render(self.subtitle, True, LIGHT_GRAY)

        tx = sw // 2 - title_text.get_width() // 2
        ty = 120
        self.screen.blit(title_shadow, (tx + 3, ty + 3))
        self.screen.blit(title_text, (tx, ty))
        self.screen.blit(subtitle_text, (sw // 2 - subtitle_text.get_width() // 2, ty + 80))

        lines = [
            "A Story-Driven Educational Adventure Game",
            "for Learning Object-Oriented Programming"
        ]
        for i, line in enumerate(lines):
            ltext = self.font_hint.render(line, True, LIGHT_GRAY)
            self.screen.blit(ltext, (sw // 2 - ltext.get_width() // 2, ty + 115 + i * 22))

        for i, option in enumerate(self.options):
            color = CYAN if i == self.selected else LIGHT_GRAY
            text = self.font_menu.render(option, True, color)
            ox = sw // 2 - text.get_width() // 2
            oy = 350 + i * 50
            if i == self.selected:
                pygame.draw.rect(self.screen, (30, 30, 80), (ox - 20, oy - 8, text.get_width() + 40, 40))
                pygame.draw.rect(self.screen, BLUE, (ox - 20, oy - 8, text.get_width() + 40, 40), 2)
            self.screen.blit(text, (ox, oy))

        hints = [
            "WASD/Arrow Keys: Move | ESC: Pause | F5: Quick Save | F9: Quick Load",
            "I: Player Info | M: Map | J: Missions | C: Calendar | R: Reputation"
        ]
        for i, hint in enumerate(hints):
            htext = self.font_hint.render(hint, True, LIGHT_GRAY)
            self.screen.blit(htext, (sw // 2 - htext.get_width() // 2, sh - 60 + i * 20))

        version = self.font_hint.render("v1.0.0", True, (100, 100, 100))
        self.screen.blit(version, (sw - 80, sh - 30))
