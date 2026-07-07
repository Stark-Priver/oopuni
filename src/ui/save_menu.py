import pygame
from src.config import SAVE_SLOTS, WHITE, BLACK, BLUE, CYAN, YELLOW, LIGHT_GRAY, DARK_GRAY


class SaveMenu:
    def __init__(self, screen, save_system):
        self.screen = screen
        self.save_system = save_system
        self.font = pygame.font.Font(None, 30)
        self.small_font = pygame.font.Font(None, 20)
        self.title_font = pygame.font.Font(None, 48)
        self.selected_slot = 0
        self.mode = "save"
        self.slots = self.save_system.get_all_slots()
        self.action = None

    def set_mode(self, mode):
        self.mode = mode
        self.slots = self.save_system.get_all_slots()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_slot = (self.selected_slot - 1) % SAVE_SLOTS
            elif event.key == pygame.K_DOWN:
                self.selected_slot = (self.selected_slot + 1) % SAVE_SLOTS
            elif event.key == pygame.K_RETURN:
                if self.mode == "save":
                    return {"save": self.selected_slot}
                else:
                    if self.slots[self.selected_slot] is not None:
                        return {"load": self.selected_slot}
            elif event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                return "back"
            elif event.key == pygame.K_DELETE:
                self.save_system.delete(self.selected_slot)
                self.slots = self.save_system.get_all_slots()
        return None

    def render(self):
        sw, sh = self.screen.get_width(), self.screen.get_height()
        self.screen.fill((15, 15, 35))

        title_text = self.title_font.render(
            f"{'Save Game' if self.mode == 'save' else 'Load Game'}", True, CYAN)
        self.screen.blit(title_text, (sw // 2 - title_text.get_width() // 2, 40))

        info_text = self.small_font.render(
            "UP/DOWN: Select  |  ENTER: Confirm  |  ESC: Back  |  DEL: Delete",
            True, (150, 160, 180))
        self.screen.blit(info_text, (sw // 2 - info_text.get_width() // 2, 90))

        slot_width = min(600, sw - 120)
        start_x = (sw - slot_width) // 2

        for i in range(SAVE_SLOTS):
            slot_y = 140 + i * 95
            is_selected = i == self.selected_slot
            slot_info = self.slots[i]

            bg_color = (25, 25, 55) if not is_selected else (35, 35, 80)
            border_color = CYAN if is_selected else (60, 60, 100)
            pygame.draw.rect(self.screen, bg_color, (start_x, slot_y, slot_width, 85),
                             border_radius=8)
            pygame.draw.rect(self.screen, border_color, (start_x, slot_y, slot_width, 85), 2,
                             border_radius=8)

            slot_num = self.small_font.render(f"Slot {i + 1}", True, YELLOW if is_selected else LIGHT_GRAY)
            self.screen.blit(slot_num, (start_x + 20, slot_y + 10))

            if slot_info:
                name_text = self.small_font.render(
                    f"{slot_info['player_name']}  |  {slot_info['academic_year']}  |  {slot_info['department'] or 'N/A'}",
                    True, WHITE)
                time_text = self.small_font.render(
                    f"Saved: {slot_info['saved_at'][:19]}", True, (150, 150, 170))
                self.screen.blit(name_text, (start_x + 20, slot_y + 35))
                self.screen.blit(time_text, (start_x + 20, slot_y + 55))
            else:
                empty_text = self.small_font.render("Empty Slot", True, (80, 80, 100))
                self.screen.blit(empty_text, (start_x + 20, slot_y + 40))

            if is_selected:
                arrow = self.font.render(">", True, CYAN)
                self.screen.blit(arrow, (start_x - 25, slot_y + 30))

        hint_text = self.small_font.render(
            "Quick Save: F5  |  Quick Load: F9", True, (80, 100, 80))
        self.screen.blit(hint_text, (sw // 2 - hint_text.get_width() // 2, sh - 40))
