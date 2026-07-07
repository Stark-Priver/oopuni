# OOP UNI — API Reference

## Module: `src.engine.game`

### `class Game`

The central orchestrator of the game. Manages the main loop, state transitions, and coordinates all subsystems.

| Method | Description |
|--------|-------------|
| `__init__()` | Initializes Pygame, creates all subsystems, sets initial state to "menu" |
| `run()` | Main loop — delegates to state handlers based on `self.state` |
| `_handle_menu_state(dt)` | Processes menu input and renders main menu |
| `_handle_playing_state(dt)` | Main gameplay: input, update, render cycle |
| `_handle_save_menu_state(dt)` | Save/load menu input and rendering |
| `_start_new_game()` | Creates fresh player, resets systems, triggers welcome dialogue |
| `_open_load_menu()` | Switches to save menu in "load" mode |
| `_build_save_data()` | Gathers all system state into a serializable dictionary |
| `_restore_save_data(data)` | Deserializes save data back into game systems |
| `_quick_save()` | Saves to quicksave.json, shows confirmation dialog |
| `_quick_load()` | Loads from quicksave.json, restores full state |
| `_check_location_interactions()` | Detects location entry, triggers missions and dialogs |

### States

| State | Description |
|-------|-------------|
| `"menu"` | Main menu — New Game, Load Game, Quit |
| `"playing"` | Active gameplay with player movement and systems |
| `"save_menu"` | Save/Load slot selection |
| `"game_over"` | Final game completion screen |

---

## Module: `src.engine.camera`

### `class Camera`

Provides viewport offset for a scrolling world.

| Method | Description |
|--------|-------------|
| `__init__(width, height)` | Creates camera with viewport dimensions |
| `update(target)` | Centers camera on target entity (player) |
| `apply(entity)` | Converts world coordinates to screen coordinates |
| `apply_rect(rect)` | Converts world rectangle to screen rectangle |
| `get_offset()` | Returns current (x, y) offset |

---

## Module: `src.engine.timer`

### `class GameTimer`

Tracks in-game time with configurable speed.

| Method | Description |
|--------|-------------|
| `update(dt)` | Advances time by `dt * time_scale / 1000` seconds |
| `get_time_string()` | Returns formatted time (e.g., "10:30 AM") |
| `get_day_string()` | Returns "Day N" |
| `is_night()` | Returns True if hours < 6 or >= 18 |
| `serialize()` | Returns dictionary for JSON persistence |
| `deserialize(data)` | Static — restores timer from dictionary |

---

## Module: `src.entities.player`

### `class Player`

The player character — an instance of the Student class in the OOP framework.

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | str | Player name |
| `x, y` | int | World position |
| `speed` | int | Movement speed (pixels/frame) |
| `facing` | str | Direction: "up", "down", "left", "right" |
| `registration_number` | str | e.g., "MUST/CS/2026/001" |
| `faculty` | str | e.g., "Science and Technology" |
| `department` | str | e.g., "Computer Science" |
| `academic_year` | str | e.g., "Year One" |
| `student_id` | str | e.g., "MUST/2026/CS/001" |
| `inventory` | list | Items carried |
| `attendance` | int | Attendance percentage (0-100) |
| `marks` | int | Cumulative marks |
| `discovered_locations` | set | Explored campus locations |
| `story_flags` | dict | Story progression flags |

| Method | Description |
|--------|-------------|
| `update(keys, campus, dt)` | Processes WASD/arrow input, checks walkability |
| `add_item(item)` | Adds item to inventory |
| `has_item(item_name)` | Checks inventory for item by name |
| `discover_location(name)` | Marks location as discovered |
| `serialize()` | Returns full player state as dict |
| `deserialize(data)` | Static — restores player from dict |

---

## Module: `src.entities.npc`

### `class NPC`

Base class for all non-player characters.

| Method | Description |
|--------|-------------|
| `update(campus, dt)` | Follows schedule waypoints with wait timers |
| `set_dialogues(dialogues)` | Sets list of dialogue strings |
| `get_current_dialogue()` | Returns current dialogue string |
| `advance_dialogue()` | Moves to next dialogue index |
| `serialize()` | Returns NPC state as dict |
| `deserialize(data)` | Static — restores NPC from dict |

---

## Module: `src.systems.save_system`

### `class SaveSystem`

JSON-based persistence system with multiple slot support.

| Method | Description |
|--------|-------------|
| `save(slot, data)` | Saves to `save_{slot}.json` |
| `load(slot)` | Loads from `save_{slot}.json` |
| `delete(slot)` | Removes save file |
| `get_slot_info(slot)` | Returns metadata (name, year, date) |
| `get_all_slots()` | Returns info for all 5 slots |
| `quick_save(data)` | Saves to `quicksave.json` |
| `quick_load()` | Loads from `quicksave.json` |
| `autosave(data)` | Saves to `autosave.json` |

---

## Module: `src.systems.calendar`

### `class AcademicCalendar`

Tracks the university academic timeline.

| Method | Description |
|--------|-------------|
| `advance_day()` | Moves to next day, updates week/semester/year |
| `get_current_event()` | Returns current academic event string |
| `get_day_name()` | Returns day of week name |
| `get_semester_progress()` | Returns "Week X/Y" |
| `serialize()` | Returns calendar state as dict |
| `reset()` | Resets to Year 1, Semester 1 |

---

## Module: `src.systems.mission`

### `class Mission`

Represents a single story or side mission.

| Attribute | Type | Description |
|-----------|------|-------------|
| `mission_id` | str | Unique identifier |
| `title` | str | Display name |
| `description` | str | Mission briefing |
| `objectives` | list | Step-by-step goals |
| `completed` | bool | Completion status |
| `active` | bool | Currently active |
| `progress` | int | Steps completed |

### `class MissionSystem`

Manages all mission lifecycle.

| Method | Description |
|--------|-------------|
| `start_mission(mission_id)` | Moves mission from available to active |
| `complete_mission(mission_id)` | Marks mission as completed |
| `on_location_entered(name)` | Increments progress for location-based objectives |

---

## Module: `src.ui.tkinter_gui`

### `class TkinterGUI`

Rich overlay windows built with Tkinter for data-heavy displays.

| Method | Description |
|--------|-------------|
| `process_events()` | Must be called each frame to keep Tkinter responsive |
| `show_player_info(player)` | Displays full student profile |
| `show_map(campus)` | Renders scaled campus map with color-coded locations |
| `show_missions(mission_system)` | Tabbed active/completed mission viewer |
| `show_calendar(calendar, timetable)` | Academic calendar + today's timetable |
| `show_reputation(reputation)` | Faction reputation with colored bars |

---

## Module: `src.world.campus`

### `class Campus`

The tile-based world map.

| Method | Description |
|--------|-------------|
| `is_walkable(x, y, width, height)` | Checks 4 corners of entity bounds against walkable tiles |
| `get_location_at(x, y)` | Returns Location containing the point |
| `get_building_at(x, y)` | Returns Building containing the point |
| `serialize()` | Returns full campus state |
| `deserialize(data)` | Static — restores campus with all buildings and locations |
