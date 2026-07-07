import pygame
import math
from src.config import WHITE, BLACK, BLUE, CYAN, LIGHT_GRAY


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.Font(None, 80)
        self.font_subtitle = pygame.font.Font(None, 30)
        self.font_menu = pygame.font.Font(None, 38)
        self.font_hint = pygame.font.Font(None, 20)
        self.font_small = pygame.font.Font(None, 16)
        self.selected = 0
        self.options = ["New Game", "Load Game", "Quit"]
        self.title = "OOP UNI"
        self.subtitle = "The Journey Through MUST"
        self.alpha = 0
        self.particles = [(math.sin(i * 0.5) * 200 + 400, math.cos(i * 0.7) * 200 + 300,
                           i * 0.02) for i in range(20)]

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
        sw, sh = self.screen.get_width(), self.screen.get_height()
        self.alpha = min(self.alpha + 2, 255)

        overlay = pygame.Surface((sw, sh))
        for y in range(sh):
            t = y / sh
            r = int(8 + t * 12)
            g = int(8 + t * 16)
            b = int(30 + t * 40)
            pygame.draw.line(overlay, (r, g, b), (0, y), (sw, y))
        overlay.set_alpha(self.alpha)
        self.screen.fill((8, 8, 30))
        self.screen.blit(overlay, (0, 0))

        time = pygame.time.get_ticks() / 1000
        for i, p in enumerate(self.particles):
            px = sw // 2 + int(math.sin(time * 0.3 + i) * 250)
            py = sh // 3 + int(math.cos(time * 0.4 + i * 1.3) * 150)
            size = int(2 + math.sin(time + i) * 1)
            color = (40 + int(math.sin(time + i) * 20),
                     100 + int(math.cos(time * 0.5 + i) * 30),
                     180 + int(math.sin(time * 0.7 + i * 2) * 40))
            pygame.draw.circle(self.screen, color, (px, py), max(size, 1))

        title_shadow = self.font_title.render(self.title, True, (0, 60, 140))
        title_text = self.font_title.render(self.title, True, CYAN)
        glow = pygame.Surface((title_text.get_width() + 40, title_text.get_height() + 20))
        glow.fill((0, 100, 200))
        glow.set_alpha(int(20 + math.sin(time * 2) * 10))
        tx = sw // 2 - title_text.get_width() // 2
        ty = sh // 4 - 30
        self.screen.blit(glow, (tx - 20 + 3, ty - 10 + 3))
        self.screen.blit(title_shadow, (tx + 4, ty + 4))
        self.screen.blit(title_text, (tx, ty))

        subtitle_text = self.font_subtitle.render(self.subtitle, True, LIGHT_GRAY)
        self.screen.blit(subtitle_text, (sw // 2 - subtitle_text.get_width() // 2, ty + 90))

        taglines = [
            "A Story-Driven Educational Adventure Game",
            "for Learning Object-Oriented Programming"
        ]
        for i, line in enumerate(taglines):
            ltext = self.font_small.render(line, True, (150, 170, 200))
            self.screen.blit(ltext, (sw // 2 - ltext.get_width() // 2, ty + 125 + i * 22))

        for i, option in enumerate(self.options):
            color = CYAN if i == self.selected else LIGHT_GRAY
            text = self.font_menu.render(option, True, color)
            ox = sw // 2 - text.get_width() // 2
            oy = sh // 2 + 50 + i * 55
            if i == self.selected:
                glow_alpha = int(30 + math.sin(time * 3) * 15)
                sel_rect = pygame.Rect(ox - 25, oy - 10, text.get_width() + 50, 45)
                pygame.draw.rect(self.screen, (0, 80, 160), sel_rect, border_radius=6)
                glow_surf = pygame.Surface(sel_rect.size)
                glow_surf.fill((0, 120, 220))
                glow_surf.set_alpha(glow_alpha)
                self.screen.blit(glow_surf, sel_rect)
                pygame.draw.rect(self.screen, (0, 150, 255), sel_rect, 2, border_radius=6)
                arrow = self.font_menu.render(">>", True, CYAN)
                self.screen.blit(arrow, (ox - 55, oy))
            self.screen.blit(text, (ox, oy))

        hints = [
            "WASD/Arrow Keys: Move  |  ESC: Pause  |  E: Interact",
            "I: Player Info  |  M: Map  |  J: Missions  |  C: Calendar  |  R: Reputation",
            "F5: Quick Save  |  F9: Quick Load  |  TAB: Save Menu"
        ]
        for i, hint in enumerate(hints):
            htext = self.font_small.render(hint, True, (130, 140, 160))
            self.screen.blit(htext, (sw // 2 - htext.get_width() // 2, sh - 80 + i * 20))

        version = self.font_small.render("v1.0.0", True, (80, 80, 100))
        self.screen.blit(version, (sw - 90, sh - 30))

        credits = self.font_small.render("Mbeya University of Science and Technology", True, (60, 60, 80))
        self.screen.blit(credits, (20, sh - 30))
