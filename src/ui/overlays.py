import pygame
from src.config import WHITE, BLACK, CYAN, YELLOW, GREEN, LIGHT_GRAY


class GameOverlay:
    def __init__(self, screen):
        self.screen = screen
        self.active = None
        self.font_title = pygame.font.Font(None, 42)
        self.font_heading = pygame.font.Font(None, 28)
        self.font_text = pygame.font.Font(None, 22)
        self.font_small = pygame.font.Font(None, 18)
        self.font_tiny = pygame.font.Font(None, 15)
        self.scroll_y = 0
        self.max_scroll = 0

    def open(self, name):
        self.active = name
        self.scroll_y = 0
        self.max_scroll = 0

    def close(self):
        self.active = None

    def is_open(self):
        return self.active is not None

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.close()
                return True
            if event.key == pygame.K_UP:
                self.scroll_y = min(self.scroll_y + 30, 0)
            if event.key == pygame.K_DOWN:
                self.scroll_y = max(self.scroll_y - 30, -self.max_scroll)
        return False

    def render(self, game):
        if not self.active:
            return
        sw, sh = self.screen.get_width(), self.screen.get_height()
        overlay = pygame.Surface((sw, sh))
        overlay.set_alpha(200)
        overlay.fill((10, 10, 30))
        self.screen.blit(overlay, (0, 0))
        if self.active == "player_info":
            self._render_player_info(game, sw, sh)
        elif self.active == "map":
            self._render_map(game, sw, sh)
        elif self.active == "missions":
            self._render_missions(game, sw, sh)
        elif self.active == "calendar":
            self._render_calendar(game, sw, sh)
        elif self.active == "reputation":
            self._render_reputation(game, sw, sh)
        close_hint = self.font_tiny.render("ESC to close  |  UP/DOWN to scroll", True, (120, 120, 140))
        self.screen.blit(close_hint, (sw // 2 - close_hint.get_width() // 2, sh - 25))

    def _render_player_info(self, game, sw, sh):
        player = game.player
        y = 40 + self.scroll_y
        title = self.font_title.render("STUDENT PROFILE", True, CYAN)
        self.screen.blit(title, (sw // 2 - title.get_width() // 2, y))
        y += 50

        panel_w = min(500, sw - 80)
        px = (sw - panel_w) // 2
        pygame.draw.rect(self.screen, (20, 20, 50), (px, y, panel_w, 280), border_radius=8)
        pygame.draw.rect(self.screen, (60, 60, 100), (px, y, panel_w, 280), 2, border_radius=8)
        y += 15

        fields = [
            ("Name", player.name),
            ("Student ID", player.student_id or "Not assigned"),
            ("Registration", player.registration_number or "Not assigned"),
            ("Faculty", player.faculty or "Not assigned"),
            ("Department", player.department or "Not assigned"),
            ("Academic Year", player.academic_year),
            ("Email", player.email or "Not assigned"),
            ("Attendance", f"{player.attendance}%"),
            ("Marks", str(player.marks)),
            ("Scholarship", "Yes" if player.scholarship else "No"),
        ]
        for label, value in fields:
            lbl = self.font_text.render(f"{label}:", True, LIGHT_GRAY)
            val = self.font_text.render(str(value), True, WHITE)
            self.screen.blit(lbl, (px + 20, y))
            self.screen.blit(val, (px + 200, y))
            y += 26

        y += 10
        inv = self.font_text.render(f"Inventory Items: {len(player.inventory)}", True, CYAN)
        self.screen.blit(inv, (px + 20, y))
        y += 24
        disc = self.font_text.render(f"Discovered Locations: {len(player.discovered_locations)}", True, CYAN)
        self.screen.blit(disc, (px + 20, y))
        self.max_scroll = max(0, y + 40 - sh)

    def _render_map(self, game, sw, sh):
        campus = game.campus
        y = 30 + self.scroll_y
        title = self.font_title.render("MUST CAMPUS MAP", True, CYAN)
        self.screen.blit(title, (sw // 2 - title.get_width() // 2, y))
        y += 15

        legend_y = y
        lx = sw - 180
        legend_items = [
            ("admin", "#8B4513", "Admin"), ("library", "#663399", "Library"),
            ("lecture", "#555555", "Lecture"), ("hub", "#0096c7", "Hub"),
            ("lab", "#3366cc", "Lab"), ("social", "#2d8a2d", "Social"),
            ("health", "#cc3333", "Health"), ("dining", "#c8962e", "Dining"),
            ("hostel", "#996633", "Hostel"), ("sports", "#2d6a2d", "Sports"),
            ("entrance", "#8B4513", "Entrance"),
        ]
        leg_title = self.font_small.render("Legend", True, WHITE)
        self.screen.blit(leg_title, (lx, legend_y))
        legend_y += 22
        for _, color, name in legend_items:
            pygame.draw.rect(self.screen, pygame.Color(color), (lx + 4, legend_y + 2, 12, 12))
            lbl = self.font_tiny.render(name, True, LIGHT_GRAY)
            self.screen.blit(lbl, (lx + 22, legend_y))
            legend_y += 16

        map_area_w = sw - 220
        map_area_h = sh - 120
        map_area_x = 20
        map_area_y = y + 10

        pygame.draw.rect(self.screen, (30, 30, 50), (map_area_x, map_area_y, map_area_w, map_area_h), border_radius=6)
        pygame.draw.rect(self.screen, (60, 60, 80), (map_area_x, map_area_y, map_area_w, map_area_h), 2, border_radius=6)

        scale = min((map_area_w - 20) / max(campus.width, 1), (map_area_h - 20) / max(campus.height, 1))
        offset_x = map_area_x + 10
        offset_y = map_area_y + 10

        player_sx = offset_x + game.player.x * scale
        player_sy = offset_y + game.player.y * scale
        pygame.draw.circle(self.screen, YELLOW, (int(player_sx), int(player_sy)), 5)
        pygame.draw.circle(self.screen, WHITE, (int(player_sx), int(player_sy)), 5, 1)

        colors = {
            "admin": "#8B4513", "library": "#663399", "lecture": "#555555",
            "hub": "#0096c7", "lab": "#3366cc", "workshop": "#b5651d",
            "social": "#2d8a2d", "health": "#cc3333", "dining": "#c8962e",
            "shop": "#6699cc", "bank": "#999933", "hostel": "#996633",
            "sports": "#2d6a2d", "transport": "#666666", "parking": "#555555",
            "entrance": "#8B4513"
        }
        for loc in campus.locations:
            sx = offset_x + loc.x * scale
            sy = offset_y + loc.y * scale
            sw2 = max(loc.width * scale, 6)
            sh2 = max(loc.height * scale, 6)
            color = colors.get(loc.type, "#999")
            pygame.draw.rect(self.screen, pygame.Color(color), (sx, sy, sw2, sh2))
            pygame.draw.rect(self.screen, WHITE, (sx, sy, sw2, sh2), 1)
            if sw2 > 30:
                txt = self.font_tiny.render(loc.name[:12], True, WHITE)
                self.screen.blit(txt, (sx + sw2 // 2 - txt.get_width() // 2, sy + sh2 // 2 - txt.get_height() // 2))

        self.max_scroll = 0

    def _render_missions(self, game, sw, sh):
        ms = game.mission_system
        y = 40 + self.scroll_y
        title = self.font_title.render("MISSIONS", True, CYAN)
        self.screen.blit(title, (sw // 2 - title.get_width() // 2, y))
        y += 50

        panel_w = min(700, sw - 80)
        px = (sw - panel_w) // 2

        active_title = self.font_heading.render(f"Active Missions ({len(ms.active_missions)})", True, YELLOW)
        self.screen.blit(active_title, (px, y))
        y += 35

        if ms.active_missions:
            for mission in ms.active_missions:
                y += 5
                pygame.draw.rect(self.screen, (25, 25, 55), (px, y, panel_w, 80), border_radius=6)
                pygame.draw.rect(self.screen, (60, 60, 90), (px, y, panel_w, 80), 1, border_radius=6)
                m_title = self.font_text.render(mission.title, True, CYAN)
                self.screen.blit(m_title, (px + 12, y + 8))
                m_desc = self.font_small.render(mission.description[:60], True, LIGHT_GRAY)
                self.screen.blit(m_desc, (px + 12, y + 32))
                prog = self.font_small.render(f"Progress: {mission.progress}/{len(mission.objectives)}", True, GREEN)
                self.screen.blit(prog, (px + 12, y + 52))
                bar_w = panel_w - 160
                bar_x = px + panel_w - bar_w - 12
                pygame.draw.rect(self.screen, (40, 40, 40), (bar_x, y + 52, bar_w, 12), border_radius=4)
                fill = (mission.progress / max(len(mission.objectives), 1)) * bar_w
                if fill > 0:
                    pygame.draw.rect(self.screen, GREEN, (bar_x, y + 52, int(fill), 12), border_radius=4)
                y += 90
        else:
            empty = self.font_text.render("No active missions. Explore campus!", True, LIGHT_GRAY)
            self.screen.blit(empty, (px + 12, y))
            y += 30

        y += 15
        comp_title = self.font_heading.render(f"Completed ({len(ms.completed_missions)})", True, GREEN)
        self.screen.blit(comp_title, (px, y))
        y += 30

        if ms.completed_missions:
            for mission in ms.completed_missions:
                done = self.font_small.render(f"[DONE] {mission.title}", True, (100, 180, 100))
                self.screen.blit(done, (px + 12, y))
                y += 22
        else:
            empty = self.font_small.render("None yet.", True, (80, 80, 100))
            self.screen.blit(empty, (px + 12, y))
            y += 22

        self.max_scroll = max(0, y + 40 - sh)

    def _render_calendar(self, game, sw, sh):
        cal = game.calendar
        tt = game.timetable
        y = 40 + self.scroll_y

        title = self.font_title.render("ACADEMIC CALENDAR", True, CYAN)
        self.screen.blit(title, (sw // 2 - title.get_width() // 2, y))
        y += 50

        panel_w = min(600, sw - 80)
        px = (sw - panel_w) // 2

        pygame.draw.rect(self.screen, (20, 20, 50), (px, y, panel_w, 180), border_radius=8)
        pygame.draw.rect(self.screen, (60, 60, 100), (px, y, panel_w, 180), 2, border_radius=8)
        y += 15

        fields = [
            ("Academic Year", f"Year {cal.year}"),
            ("Semester", f"Semester {cal.semester}"),
            ("Current Event", cal.get_current_event()),
            ("Day", cal.get_day_name()),
            ("Progress", cal.get_semester_progress()),
        ]
        for label, value in fields:
            lbl = self.font_text.render(f"{label}:", True, LIGHT_GRAY)
            val = self.font_text.render(value, True, WHITE)
            self.screen.blit(lbl, (px + 20, y))
            self.screen.blit(val, (px + 220, y))
            y += 28

        y += 15
        tt_title = self.font_heading.render(f"Today's Timetable ({cal.get_day_name()})", True, CYAN)
        self.screen.blit(tt_title, (px, y))
        y += 30

        entries = tt.get_today_entries()
        if entries:
            for entry in entries[:8]:
                status = "[X]" if entry["attended"] else "[ ]"
                color = GREEN if entry["attended"] else LIGHT_GRAY
                line = f"{status}  {entry['time']}  -  {entry['course']}  @ {entry['location']}"
                txt = self.font_small.render(line, True, color)
                self.screen.blit(txt, (px + 12, y))
                y += 22
        else:
            txt = self.font_text.render("No lectures scheduled today.", True, LIGHT_GRAY)
            self.screen.blit(txt, (px + 12, y))
            y += 24

        self.max_scroll = max(0, y + 40 - sh)

    def _render_reputation(self, game, sw, sh):
        rep = game.reputation
        y = 40 + self.scroll_y

        title = self.font_title.render("REPUTATION", True, CYAN)
        self.screen.blit(title, (sw // 2 - title.get_width() // 2, y))
        y += 50

        panel_w = min(600, sw - 80)
        px = (sw - panel_w) // 2

        pygame.draw.rect(self.screen, (20, 20, 50), (px, y, panel_w, 320), border_radius=8)
        pygame.draw.rect(self.screen, (60, 60, 100), (px, y, panel_w, 320), 2, border_radius=8)
        y += 15

        for faction, rep_val in rep.get_all_reputations().items():
            lbl = self.font_text.render(faction, True, WHITE)
            self.screen.blit(lbl, (px + 20, y))

            bar_w = panel_w - 280
            bar_x = px + 200
            pygame.draw.rect(self.screen, (40, 40, 40), (bar_x, y + 4, bar_w, 16), border_radius=4)
            fill_w = int((rep_val / 100) * bar_w)
            if fill_w > 0:
                color = self._rep_color(rep_val)
                pygame.draw.rect(self.screen, color, (bar_x, y + 4, fill_w, 16), border_radius=4)

            pct = self.font_small.render(f"{int(rep_val)}%", True, self._rep_color(rep_val))
            self.screen.blit(pct, (bar_x + bar_w + 12, y))
            y += 28

        avg = rep.get_average_reputation()
        y += 10
        avg_lbl = self.font_heading.render(f"Average Reputation: {int(avg)}%", True, self._rep_color(avg))
        self.screen.blit(avg_lbl, (px + 20, y))
        y += 35

        standing_lbl = self.font_small.render(f"Overall Standing: {int(avg)}%", True, LIGHT_GRAY)
        self.screen.blit(standing_lbl, (px + 20, y))

        self.max_scroll = max(0, y + 40 - sh)

    def _rep_color(self, value):
        if value >= 80: return (45, 138, 45)
        if value >= 60: return (90, 158, 62)
        if value >= 40: return (204, 153, 0)
        if value >= 20: return (204, 102, 0)
        return (204, 51, 51)
