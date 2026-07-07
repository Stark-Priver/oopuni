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
            box_width = min(900, self.screen.get_width() - 40)
            box_height = 160
            bx = (self.screen.get_width() - box_width) // 2
            by = self.screen.get_height() - box_height - 20
            pygame.draw.rect(self.screen, BLACK, (bx, by, box_width, box_height))
            pygame.draw.rect(self.screen, (60, 60, 80), (bx, by, box_width, box_height), 2)

            title_label = self.font_small.render(dialog.title, True, CYAN)
            self.screen.blit(title_label, (bx + 12, by + 8))

            lines = self._wrap_text(dialog.text, self.font_medium, box_width - 24)
            max_lines = 5
            for i, line in enumerate(lines[:max_lines]):
                self.screen.blit(line, (bx + 12, by + 30 + i * 24))

            if len(lines) > max_lines:
                more = self.font_small.render(f"... ({len(lines) - max_lines} more lines)", True, LIGHT_GRAY)
                self.screen.blit(more, (bx + 12, by + 30 + max_lines * 24))

            continue_text = self.font_small.render("SPACE to continue", True, LIGHT_GRAY)
            self.screen.blit(continue_text, (bx + box_width - 130, by + box_height - 22))

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
        paragraphs = text.split('\n')
        lines = []
        for para in paragraphs:
            words = para.split(' ')
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
