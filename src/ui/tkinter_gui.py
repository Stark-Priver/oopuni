import tkinter as tk
from tkinter import ttk
import threading
from src.config import DEPARTMENTS


class TkinterGUI:
    def __init__(self, game):
        self.game = game
        self.root = None
        self._windows = {}

    def _ensure_root(self):
        if self.root is None:
            self.root = tk.Tk()
            self.root.withdraw()
            self.root.title("OOP UNI")
            self.root.geometry("600x500+1380+100")

    def process_events(self):
        if self.root:
            try:
                self.root.update_idletasks()
                self.root.update()
            except tk.TclError:
                self.root = None

    def show_player_info(self, player):
        self._ensure_root()
        self._clear_window()
        self.root.deiconify()
        self.root.title("Player Profile")
        self.root.geometry("500x600+1380+100")

        frame = ttk.Frame(self.root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        title = tk.Label(frame, text="STUDENT PROFILE", font=("Arial", 18, "bold"), fg="#1a5276")
        title.pack(pady=(0, 20))

        fields = [
            ("Name", player.name),
            ("Student ID", player.student_id or "Not assigned"),
            ("Registration Number", player.registration_number or "Not assigned"),
            ("Faculty", player.faculty or "Not assigned"),
            ("Department", player.department or "Not assigned"),
            ("Academic Year", player.academic_year),
            ("Email", player.email or "Not assigned"),
            ("Attendance", f"{player.attendance}%"),
            ("Marks", str(player.marks)),
            ("Scholarship", "Yes" if player.scholarship else "No"),
        ]

        canvas = tk.Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for label, value in fields:
            row = ttk.Frame(scrollable_frame)
            row.pack(fill=tk.X, pady=4)
            lbl = tk.Label(row, text=f"{label}:", font=("Arial", 11, "bold"), width=20, anchor="w")
            lbl.pack(side=tk.LEFT)
            val = tk.Label(row, text=value, font=("Arial", 11), anchor="w")
            val.pack(side=tk.LEFT, padx=(10, 0))

        inventory_label = tk.Label(scrollable_frame, text=f"\nInventory Items: {len(player.inventory)}",
                                   font=("Arial", 11))
        inventory_label.pack(anchor="w", pady=(10, 0))

        discovered = tk.Label(scrollable_frame,
                              text=f"Discovered Locations: {len(player.discovered_locations)}",
                              font=("Arial", 11))
        discovered.pack(anchor="w")

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        close_btn = ttk.Button(frame, text="Close (ESC)", command=self._hide_window)
        close_btn.pack(pady=10)

    def show_map(self, campus):
        self._ensure_root()
        self._clear_window()
        self.root.deiconify()
        self.root.title("Campus Map")
        self.root.geometry("700x600+1380+100")

        frame = ttk.Frame(self.root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        title = tk.Label(frame, text="MUST CAMPUS MAP", font=("Arial", 18, "bold"), fg="#1a5276")
        title.pack(pady=(0, 10))

        canvas = tk.Canvas(frame, bg="#f0f0f0", highlightthickness=1, highlightbackground="#ccc")
        canvas.pack(fill=tk.BOTH, expand=True)

        colors = {
            "admin": "#8B4513", "library": "#663399", "lecture": "#555555",
            "hub": "#0096c7", "lab": "#3366cc", "workshop": "#b5651d",
            "social": "#2d8a2d", "health": "#cc3333", "dining": "#c8962e",
            "shop": "#6699cc", "bank": "#999933", "hostel": "#996633",
            "sports": "#2d6a2d", "transport": "#666666", "parking": "#555555",
            "entrance": "#8B4513"
        }

        scale = min(650 / max(campus.width, 1), 500 / max(campus.height, 1))

        for loc in campus.locations:
            scaled_x = 25 + loc.x * scale
            scaled_y = 25 + loc.y * scale
            scaled_w = max(loc.width * scale, 8)
            scaled_h = max(loc.height * scale, 8)
            color = colors.get(loc.type, "#999")
            canvas.create_rectangle(scaled_x, scaled_y, scaled_x + scaled_w, scaled_y + scaled_h,
                                    fill=color, outline="white", width=1)
            if scaled_w > 30:
                canvas.create_text(scaled_x + scaled_w / 2, scaled_y + scaled_h / 2,
                                   text=loc.name[:12], fill="white", font=("Arial", 7, "bold"))

        close_btn = ttk.Button(frame, text="Close (ESC)", command=self._hide_window)
        close_btn.pack(pady=10)

    def show_missions(self, mission_system):
        self._ensure_root()
        self._clear_window()
        self.root.deiconify()
        self.root.title("Missions")
        self.root.geometry("600x500+1380+100")

        frame = ttk.Frame(self.root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        title = tk.Label(frame, text="MISSIONS", font=("Arial", 18, "bold"), fg="#1a5276")
        title.pack(pady=(0, 10))

        notebook = ttk.Notebook(frame)
        notebook.pack(fill=tk.BOTH, expand=True)

        active_frame = ttk.Frame(notebook, padding="10")
        completed_frame = ttk.Frame(notebook, padding="10")
        notebook.add(active_frame, text=f"Active ({len(mission_system.active_missions)})")
        notebook.add(completed_frame, text=f"Completed ({len(mission_system.completed_missions)})")

        if mission_system.active_missions:
            for mission in mission_system.active_missions:
                m_frame = ttk.LabelFrame(active_frame, text=mission.title, padding="10")
                m_frame.pack(fill=tk.X, pady=5)
                desc = tk.Label(m_frame, text=mission.description, wraplength=500, justify=tk.LEFT)
                desc.pack(anchor="w")
                progress_text = tk.Label(m_frame,
                    text=f"Progress: {mission.progress}/{len(mission.objectives)}",
                    fg="#2d8a2d")
                progress_text.pack(anchor="w")
        else:
            tk.Label(active_frame, text="No active missions. Explore campus to start new missions!",
                     wraplength=500).pack()

        if mission_system.completed_missions:
            for mission in mission_system.completed_missions:
                m_frame = ttk.LabelFrame(completed_frame, text=mission.title, padding="5")
                m_frame.pack(fill=tk.X, pady=3)
                tk.Label(m_frame, text=f"✓ Completed", fg="green").pack(anchor="w")
        else:
            tk.Label(completed_frame, text="No completed missions yet.",
                     wraplength=500).pack()

        close_btn = ttk.Button(frame, text="Close (ESC)", command=self._hide_window)
        close_btn.pack(pady=10)

    def show_calendar(self, calendar, timetable):
        self._ensure_root()
        self._clear_window()
        self.root.deiconify()
        self.root.title("Academic Calendar")
        self.root.geometry("550x500+1380+100")

        frame = ttk.Frame(self.root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        title = tk.Label(frame, text="ACADEMIC CALENDAR", font=("Arial", 18, "bold"), fg="#1a5276")
        title.pack(pady=(0, 20))

        info_frame = ttk.LabelFrame(frame, text="Current Status", padding="15")
        info_frame.pack(fill=tk.X, pady=10)

        fields = [
            ("Academic Year", f"Year {calendar.year}"),
            ("Semester", f"Semester {calendar.semester}"),
            ("Current Event", calendar.get_current_event()),
            ("Day", calendar.get_day_name()),
            ("Progress", calendar.get_semester_progress()),
        ]

        for label, value in fields:
            row = ttk.Frame(info_frame)
            row.pack(fill=tk.X, pady=2)
            tk.Label(row, text=f"{label}:", font=("Arial", 11, "bold"), width=15, anchor="w").pack(side=tk.LEFT)
            tk.Label(row, text=value, font=("Arial", 11), anchor="w").pack(side=tk.LEFT, padx=(10, 0))

        timetable_frame = ttk.LabelFrame(frame, text=f"Today's Timetable ({calendar.get_day_name()})",
                                          padding="10")
        timetable_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        entries = timetable.get_today_entries()
        if entries:
            for entry in entries[:6]:
                entry_row = ttk.Frame(timetable_frame)
                entry_row.pack(fill=tk.X, pady=2)
                status = "✓" if entry["attended"] else "○"
                tk.Label(entry_row, text=f"{status}  {entry['time']}  -  {entry['course']}",
                        font=("Arial", 10)).pack(side=tk.LEFT)
                tk.Label(entry_row, text=f"  @ {entry['location']}",
                        font=("Arial", 9), fg="#666").pack(side=tk.LEFT)
        else:
            tk.Label(timetable_frame, text="No lectures scheduled today.").pack()

        close_btn = ttk.Button(frame, text="Close (ESC)", command=self._hide_window)
        close_btn.pack(pady=10)

    def show_reputation(self, reputation):
        self._ensure_root()
        self._clear_window()
        self.root.deiconify()
        self.root.title("Reputation")
        self.root.geometry("500x500+1380+100")

        frame = ttk.Frame(self.root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        title = tk.Label(frame, text="REPUTATION", font=("Arial", 18, "bold"), fg="#1a5276")
        title.pack(pady=(0, 20))

        rep_frame = ttk.LabelFrame(frame, text="Faction Standing", padding="15")
        rep_frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(rep_frame)
        scrollbar = ttk.Scrollbar(rep_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for faction, rep in reputation.get_all_reputations().items():
            row = ttk.Frame(scrollable_frame)
            row.pack(fill=tk.X, pady=6)
            tk.Label(row, text=faction, font=("Arial", 11, "bold"), width=20, anchor="w").pack(side=tk.LEFT)

            bar_frame = ttk.Frame(row, width=200, height=20)
            bar_frame.pack(side=tk.LEFT, padx=(10, 0))
            bar_frame.pack_propagate(False)

            bar = tk.Frame(bar_frame, bg=self._rep_color(rep), width=int(rep * 2))
            bar.pack(side=tk.LEFT, fill=tk.Y)

            if rep < 100:
                empty = tk.Frame(bar_frame, bg="#e0e0e0", width=int((100 - rep) * 2))
                empty.pack(side=tk.LEFT, fill=tk.Y)

            standing = reputation.get_standing(faction)
            tk.Label(row, text=f"{int(rep)}% ({standing})",
                    font=("Arial", 10), fg=self._rep_color(rep)).pack(side=tk.LEFT, padx=(10, 0))

        avg_rep = reputation.get_average_reputation()
        tk.Label(frame, text=f"\nAverage Reputation: {int(avg_rep)}%",
                font=("Arial", 12, "bold"), fg=self._rep_color(avg_rep)).pack()

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        close_btn = ttk.Button(frame, text="Close (ESC)", command=self._hide_window)
        close_btn.pack(pady=10)

    def _rep_color(self, value):
        if value >= 80:
            return "#2d8a2d"
        elif value >= 60:
            return "#5a9e3e"
        elif value >= 40:
            return "#cc9900"
        elif value >= 20:
            return "#cc6600"
        else:
            return "#cc3333"

    def _clear_window(self):
        if self.root:
            for widget in self.root.winfo_children():
                widget.destroy()

    def _hide_window(self):
        if self.root:
            self.root.withdraw()
