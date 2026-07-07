import pygame
from src.config import (TILE_SIZE, WHITE, BLACK, GREEN, BLUE, GRAY,
                        DARK_GRAY, LIGHT_GRAY, BROWN, SKY_BLUE,
                        GRASS_GREEN, PATH_GRAY, CYAN, YELLOW, RED)


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font_small = pygame.font.Font(None, 18)
        self.font_medium = pygame.font.Font(None, 24)
        self.font_large = pygame.font.Font(None, 36)

    def clear(self):
        self.screen.fill(SKY_BLUE)

    def draw_campus(self, campus, camera):
        for x in range(0, campus.width, TILE_SIZE):
            for y in range(0, campus.height, TILE_SIZE):
                tile_rect = pygame.Rect(x - camera.x, y - camera.y, TILE_SIZE, TILE_SIZE)
                if (x, y) in campus.walkable_tiles:
                    if self._is_path(x, y):
                        pygame.draw.rect(self.screen, PATH_GRAY, tile_rect)
                    else:
                        pygame.draw.rect(self.screen, GRASS_GREEN, tile_rect)
                    pygame.draw.rect(self.screen, (30, 120, 30), tile_rect, 1)

        for building in campus.buildings:
            b_rect = pygame.Rect(building.x - camera.x, building.y - camera.y,
                                 building.width, building.height)
            pygame.draw.rect(self.screen, building.color, b_rect)
            pygame.draw.rect(self.screen, WHITE, b_rect, 2)
            label = self.font_small.render(building.name, True, WHITE)
            lx = building.x - camera.x + (building.width - label.get_width()) // 2
            ly = building.y - camera.y + (building.height - label.get_height()) // 2
            self.screen.blit(label, (lx, ly))

            entrance = building.get_entrance()
            ex = entrance[0] - camera.x
            ey = entrance[1] - camera.y
            pygame.draw.rect(self.screen, YELLOW, (ex - 8, ey - 4, 16, 8))

        for location in campus.locations:
            l_rect = pygame.Rect(location.x - camera.x, location.y - camera.y,
                                 location.width, location.height)
            pygame.draw.rect(self.screen, location.color, l_rect, 1)
            if location.is_visited:
                pygame.draw.rect(self.screen, GREEN, l_rect, 2)

    def _is_path(self, x, y):
        path_zones = [
            (1000, 200, 1600, 64),
            (200, 1000, 3000, 64),
            (500, 200, 64, 1200),
            (1500, 200, 64, 1200),
            (2500, 200, 64, 1200),
        ]
        for px, py, pw, ph in path_zones:
            if px <= x <= px + pw and py <= y <= py + ph:
                return True
        return False

    def draw_player(self, player, camera):
        px = player.x - camera.x
        py = player.y - camera.y
        color = (50, 150, 255)
        pygame.draw.rect(self.screen, color, (px, py, player.width, player.height))
        pygame.draw.rect(self.screen, WHITE, (px, py, player.width, player.height), 2)
        if player.facing == "down":
            eye_y = py + 6
        elif player.facing == "up":
            eye_y = py + 4
        elif player.facing == "left":
            eye_y = py + 8
        else:
            eye_y = py + 8
        pygame.draw.circle(self.screen, WHITE, (px + 8, eye_y), 3)
        pygame.draw.circle(self.screen, WHITE, (px + 24, eye_y), 3)
        pygame.draw.circle(self.screen, BLACK, (px + 8, eye_y), 1)
        pygame.draw.circle(self.screen, BLACK, (px + 24, eye_y), 1)

    def draw_npcs(self, npcs, camera):
        for npc in npcs:
            nx = npc.x - camera.x
            ny = npc.y - camera.y
            pygame.draw.rect(self.screen, npc.color, (nx, ny, npc.width, npc.height))
            pygame.draw.rect(self.screen, WHITE, (nx, ny, npc.width, npc.height), 1)
            name_label = self.font_small.render(npc.name, True, WHITE)
            self.screen.blit(name_label, (nx - 10, ny - 16))

    def draw_dialog(self, dialog):
        if dialog.visible and dialog.text:
            box_width = min(800, self.screen.get_width() - 40)
            box_height = 120
            bx = (self.screen.get_width() - box_width) // 2
            by = self.screen.get_height() - box_height - 20
            pygame.draw.rect(self.screen, BLACK, (bx, by, box_width, box_height))
            pygame.draw.rect(self.screen, WHITE, (bx, by, box_width, box_height), 2)

            title_label = self.font_small.render(dialog.title, True, CYAN)
            self.screen.blit(title_label, (bx + 10, by + 8))

            lines = self._wrap_text(dialog.text, self.font_medium, box_width - 20)
            for i, line in enumerate(lines[:4]):
                self.screen.blit(line, (bx + 10, by + 32 + i * 22))

            continue_text = self.font_small.render("Press SPACE to continue", True, LIGHT_GRAY)
            self.screen.blit(continue_text, (bx + box_width - 180, by + box_height - 24))

    def draw_pause_overlay(self):
        overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        pause_text = self.font_large.render("PAUSED", True, WHITE)
        self.screen.blit(pause_text, (self.screen.get_width() // 2 - pause_text.get_width() // 2,
                                       self.screen.get_height() // 2 - 50))
        hint1 = self.font_small.render("F5: Quick Save | F9: Quick Load | TAB: Save Menu", True, LIGHT_GRAY)
        hint2 = self.font_small.render("I: Player Info | M: Map | J: Missions | C: Calendar | R: Reputation", True, LIGHT_GRAY)
        hint3 = self.font_small.render("ESC: Resume", True, LIGHT_GRAY)
        self.screen.blit(hint1, (self.screen.get_width() // 2 - hint1.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(hint2, (self.screen.get_width() // 2 - hint2.get_width() // 2, self.screen.get_height() // 2 + 24))
        self.screen.blit(hint3, (self.screen.get_width() // 2 - hint3.get_width() // 2, self.screen.get_height() // 2 + 48))

    def draw_interact_prompt(self, player, campus):
        current_loc = campus.get_location_at(player.x, player.y)
        if not current_loc:
            return
        prompt = self.font_small.render("Press E to interact", True, YELLOW)
        prompt_shadow = self.font_small.render("Press E to interact", True, BLACK)
        px = self.screen.get_width() // 2 - prompt.get_width() // 2
        py = self.screen.get_height() // 2 + 40
        self.screen.blit(prompt_shadow, (px + 1, py + 1))
        self.screen.blit(prompt, (px, py))
        loc_name = self.font_medium.render(current_loc.name, True, WHITE)
        loc_shadow = self.font_medium.render(current_loc.name, True, BLACK)
        lx = self.screen.get_width() // 2 - loc_name.get_width() // 2
        ly = self.screen.get_height() // 2 - 40
        self.screen.blit(loc_shadow, (lx + 1, ly + 1))
        self.screen.blit(loc_name, (lx, ly))

    def _wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(font.render(current_line.strip(), True, WHITE))
                current_line = word + ' '
        if current_line:
            lines.append(font.render(current_line.strip(), True, WHITE))
        return lines if lines else [font.render(text, True, WHITE)]
