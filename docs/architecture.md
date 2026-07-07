# OOP UNI — System Architecture

## Overview

OOP UNI is built using a **modular component-based architecture** with clear separation of concerns. The game engine runs on Pygame for rendering and input, with Tkinter providing rich overlay windows for data-heavy screens.

## Core Architecture Diagram

```
main.py
   │
   └──→ Game (engine/game.py)
            │
            ├──→ Engine Layer
            │       ├── Camera
            │       ├── Timer
            │       └── Event System
            │
            ├──→ Entities Layer
            │       ├── Player
            │       ├── NPC (base)
            │       ├── Lecturer (extends NPC)
            │       └── Student (extends NPC)
            │
            ├──→ Systems Layer
            │       ├── SaveSystem (JSON persistence)
            │       ├── AcademicCalendar
            │       ├── Timetable
            │       ├── ReputationSystem
            │       ├── MissionSystem
            │       └── EventSystem
            │
            ├──→ World Layer
            │       ├── Campus (tile-based map)
            │       ├── Building
            │       ├── Location
            │       └── NPCScheduler
            │
            ├──→ UI Layer
            │       ├── Renderer (Pygame)
            │       ├── HUD
            │       ├── MainMenu
            │       ├── DialogSystem
            │       ├── SaveMenu
            │       └── TkinterGUI
            │
            └──→ OOP Concepts Layer
                    ├── Classes & Objects
                    ├── Inheritance
                    ├── Polymorphism
                    ├── Encapsulation
                    ├── Abstraction
                    └── Design Patterns
```

## Layer Descriptions

### 1. Engine Layer (`src/engine/`)

The foundation of the game loop and core systems.

| Module | Responsibility |
|--------|---------------|
| `game.py` | Main game loop, state management, input routing, system coordination |
| `camera.py` | Viewport offset calculation, screen-space coordinate transformation |
| `timer.py` | Game time tracking with configurable time scale, day/night cycle |

**Key Design Decision**: The Game class acts as a **Facade** — it coordinates all subsystems without exposing their internal complexity to each other.

### 2. Entities Layer (`src/entities/`)

Represents all living and interactive objects in the game world.

| Module | Responsibility |
|--------|---------------|
| `player.py` | Player state, movement, inventory, serialization |
| `npc.py` | Base NPC class with scheduling, dialogue, and serialization |
| `lecturer.py` | Lecturer specialization — department, courses, office hours |
| `student.py` | Student NPC — year, department, club membership, mood |

**Inheritance Chain**: `NPC` → `Lecturer` / `Student` — demonstrates OOP inheritance in the engine itself.

### 3. Systems Layer (`src/systems/`)

Independent game systems that manage specific aspects of gameplay.

| System | File | Features |
|--------|------|----------|
| Save System | `save_system.py` | JSON persistence, 5 slots, quick save/load, autosave, chapter saves |
| Calendar | `calendar.py` | 4 academic years, 2 semesters each, weekly events, day tracking |
| Timetable | `timetable.py` | Per-day lecture schedule, attendance tracking, location assignment |
| Reputation | `reputation.py` | 8 faction reputations (0-100), standing levels, dynamic unlocks |
| Missions | `mission.py` | Mission lifecycle (available → active → completed), objective tracking |
| Events | `event_system.py` | Trigger-based event system, conditional effects |

### 4. World Layer (`src/world/`)

The spatial and environmental representation of the game.

| Module | Responsibility |
|--------|---------------|
| `campus.py` | 3200x2400 tile-based campus map, walkable areas, building/location registry |
| `building.py` | Building properties, entrance coordinates, floor management |
| `location.py` | Named interactable areas within buildings, visit tracking |
| `npc_scheduler.py` | NPC generation, schedule management, routine updates |

### 5. UI Layer (`src/ui/`)

All visual output, rendered through two parallel systems.

| Module | Framework | Features |
|--------|-----------|----------|
| `renderer.py` | Pygame | Campus rendering, entity drawing, dialog boxes, pause overlay, text wrapping |
| `hud.py` | Pygame | Top info bar, active mission tracker, progress bars |
| `menu.py` | Pygame | Main menu with animated background, keyboard navigation |
| `dialog.py` | Pygame | Queue-based dialogue system, message history |
| `save_menu.py` | Pygame | Slot-based save/load screen with metadata display |
| `tkinter_gui.py` | Tkinter | Rich overlays: player profile, campus map, missions, calendar, reputation bars |

**Dual UI Strategy**: Pygame handles real-time rendering (campus, movement, HUD), while Tkinter provides information-dense overlays that would be difficult to implement in raw Pygame.

### 6. OOP Concepts Layer (`src/oop_concepts/`)

Educational content that ties game mechanics to OOP theory.

| Module | Concept | In-Game Example |
|--------|---------|-----------------|
| `classes_objects.py` | Classes, Objects, Constructors, Attributes, Methods | Student registration, Library books |
| `inheritance.py` | Inheritance, Composition | Department hierarchy, Hostel rooms |
| `polymorphism.py` | Polymorphism | Different lecturers teaching styles |
| `encapsulation.py` | Encapsulation | Bank account privacy, Exam results |
| `abstraction.py` | Abstraction | Timetable system |
| `patterns.py` | Design Patterns | Singleton University, Observer announcements |

## Save System Architecture

```
SaveSystem
    │
    ├── save(slot, data)       → saves/save_{slot}.json
    ├── load(slot)              → reads saves/save_{slot}.json
    ├── quick_save(data)        → saves/quicksave.json
    ├── quick_load()            → reads saves/quicksave.json
    ├── autosave(data)          → saves/autosave.json
    ├── delete(slot)            → removes save file
    └── get_all_slots()         → metadata for all 5 slots

Save Data Structure:
{
    "player": { ... },
    "calendar": { ... },
    "timetable": { ... },
    "reputation": { ... },
    "missions": { ... },
    "campus": { ... },
    "npc_scheduler": { ... },
    "game_timer": { ... },
    "dialogue_history": [ ... ],
    "saved_at": "2026-07-07T...",
    "version": "1.0.0"
}
```

All game entities implement `serialize()` / `deserialize()` static methods for JSON round-tripping.

## Data Flow

### Game Loop Cycle

```
1. Process Input (pygame events + keyboard state)
2. Update Systems:
   a. Player movement (collision with campus walkable tiles)
   b. NPC schedules (follow waypoint-based routines)
   c. Game timer (advance clock)
   d. Academic calendar (advance days/events)
   e. Timetable (check current lectures)
   f. Mission system (check triggers, progress)
   g. Dialog system (advance queued messages)
3. Render:
   a. Clear screen
   b. Draw campus tiles (grass, paths, buildings)
   c. Draw NPCs with name labels
   d. Draw player with direction indicator
   e. Draw active dialog box
   f. Draw HUD overlay
   g. Draw pause menu if paused
4. Flip display buffer
```

## Threading Model

- Main game loop runs on the **main thread** (Pygame)
- Tkinter runs on the **same thread**, using `update_idletasks()` and `update()` calls within the game loop
- No background threads are used — all updates are synchronous per frame

## Configuration

All game constants are defined in `src/config.py`:
- Screen dimensions: 1280x720
- Tile size: 32x32 pixels
- FPS cap: 60
- Player speed: 3 pixels/frame
- Save slots: 5
- Autosave interval: 300 seconds
