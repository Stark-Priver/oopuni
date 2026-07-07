import pygame
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, SAVE_SLOTS, WHITE, BLACK, BLUE, CYAN, GREEN, YELLOW, RED, LIGHT_GRAY, DARK_GRAY


class SaveMenu:
    def __init__(self, screen, save_system):
        self.screen = screen
        self.save_system = save_system
        self.font = pygame.font.Font(None, 28)
        self.small_font = pygame.font.Font(None, 20)
        self.title_font = pygame.font.Font(None, 42)
        self.selected_slot = 0
        self.mode = "save"
        self.slots = []
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
        self.screen.fill((20, 20, 40))

        title_text = self.title_font.render(
            f"{'Save Game' if self.mode == 'save' else 'Load Game'}", True, CYAN)
        self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 40))

        info_text = self.small_font.render(
            "Use UP/DOWN to select, ENTER to confirm, ESC to go back, DEL to delete save",
            True, LIGHT_GRAY)
        self.screen.blit(info_text, (SCREEN_WIDTH // 2 - info_text.get_width() // 2, 90))

        for i in range(SAVE_SLOTS):
            slot_y = 140 + i * 90
            is_selected = i == self.selected_slot
            slot_info = self.slots[i]

            bg_color = (30, 30, 60) if not is_selected else (50, 50, 100)
            border_color = CYAN if is_selected else (80, 80, 120)
            pygame.draw.rect(self.screen, bg_color, (100, slot_y, SCREEN_WIDTH - 200, 80))
            pygame.draw.rect(self.screen, border_color, (100, slot_y, SCREEN_WIDTH - 200, 80), 2)

            slot_label = self.font.render(f"Slot {i + 1}", True, YELLOW if is_selected else LIGHT_GRAY)
            self.screen.blit(slot_label, (120, slot_y + 8))

            if slot_info:
                name_text = self.small_font.render(
                    f"{slot_info['player_name']} | {slot_info['academic_year']} | {slot_info['department']}",
                    True, WHITE)
                time_text = self.small_font.render(
                    f"Saved: {slot_info['saved_at'][:19]}", True, LIGHT_GRAY)
                self.screen.blit(name_text, (120, slot_y + 36))
                self.screen.blit(time_text, (120, slot_y + 56))
            else:
                empty_text = self.small_font.render("Empty Slot", True, (100, 100, 100))
                self.screen.blit(empty_text, (120, slot_y + 40))

        hint_text = self.small_font.render(
            "TIP: Quick Save with F5, Quick Load with F9 during gameplay", True, (100, 120, 100))
        self.screen.blit(hint_text, (SCREEN_WIDTH // 2 - hint_text.get_width() // 2, SCREEN_HEIGHT - 30))
