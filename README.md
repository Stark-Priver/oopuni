# OOP UNI: The Journey Through MUST

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/pygame-2.0.0%2B-green)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)
[![Status](https://img.shields.io/badge/status-alpha-orange)]()

> A story-driven, open-world educational adventure game that transforms the university experience into an interactive journey for mastering Object-Oriented Programming (OOP).

---

## Overview

**OOP UNI** is a premium educational adventure game set at **Mbeya University of Science and Technology (MUST)**. Unlike traditional educational tools that teach through quizzes or coding challenges, this game lets you *live* the life of a university student while naturally discovering OOP concepts through exploration, interaction, missions, and simulations.

### The Story

For decades, the digital systems running MUST have been maintained by an invisible architecture called **The Object Framework**. When an unknown corruption called **The Chaos Bug** begins spreading through the systems — corrupting student records, overlapping timetables, and corrupting exam results — only one student has the ability to see and repair both worlds. That student is you.

### Key Features

- **Open World Campus**: Freely explore a fully realized university campus with 20+ interactive locations
- **Story-Driven**: Four academic years of narrative, from admission to graduation
- **OOP Integration**: Every game mechanic naturally demonstrates an OOP concept
- **Dynamic Calendar**: Real-time academic calendar with semesters, exams, and events
- **Living NPCs**: Lecturers, students, and staff follow realistic daily routines
- **Reputation System**: Build relationships with departments and factions across campus
- **Persistent Save System**: Multiple save slots, quick save/load, autosave, and checkpoint saves
- **Tkinter GUI**: Full-featured overlay windows for player info, maps, missions, and more
- **Chapter Structure**: Year 1 (Objects) → Year 2 (Relationships) → Year 3 (Architecture) → Year 4 (Design Patterns)

---

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/Stark-Priver/oopuni.git
cd oopuni

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
```

### Controls

| Key | Action |
|-----|--------|
| **WASD / Arrow Keys** | Move player |
| **ESC** | Pause/Resume |
| **F5** | Quick Save |
| **F9** | Quick Load |
| **TAB** | Save/Load Menu |
| **I** | Player Info (Tkinter) |
| **M** | Campus Map (Tkinter) |
| **J** | Missions (Tkinter) |
| **C** | Calendar & Timetable (Tkinter) |
| **R** | Reputation (Tkinter) |
| **SPACE** | Advance dialogue |
| **ENTER** | Confirm menu selection |
| **DELETE** | Delete save file |

---

## Game Architecture

```
oopuni/
├── main.py                    # Entry point
├── setup.py                   # Package configuration
├── requirements.txt           # Dependencies
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
├── assets/                    # Game assets
│   ├── fonts/                 # Font files
│   ├── images/                # Image files
│   └── sounds/                # Audio files
├── saves/                     # Save file directory
├── src/                       # Source code
│   ├── config.py              # Game configuration
│   ├── chapter_one.py         # Chapter 1 storyline
│   ├── engine/                # Core engine
│   │   ├── game.py            # Main game loop
│   │   ├── camera.py          # Camera system
│   │   └── timer.py           # Game time
│   ├── entities/              # Game entities
│   │   ├── player.py          # Player class
│   │   ├── npc.py             # Base NPC class
│   │   ├── lecturer.py        # Lecturer (inherits NPC)
│   │   └── student.py         # Student (inherits NPC)
│   ├── systems/               # Game systems
│   │   ├── save_system.py     # Save/Load (JSON)
│   │   ├── calendar.py        # Academic calendar
│   │   ├── timetable.py       # Lecture timetable
│   │   ├── reputation.py      # Faction reputation
│   │   ├── mission.py         # Mission management
│   │   └── event_system.py    # Event triggers
│   ├── oop_concepts/          # Educational content
│   │   ├── classes_objects.py # Classes & Objects
│   │   ├── inheritance.py     # Inheritance & Composition
│   │   ├── polymorphism.py    # Polymorphism
│   │   ├── encapsulation.py   # Encapsulation
│   │   ├── abstraction.py     # Abstraction
│   │   └── patterns.py        # Design Patterns
│   ├── ui/                    # User interface
│   │   ├── renderer.py        # Pygame renderer
│   │   ├── hud.py             # Heads-up display
│   │   ├── menu.py            # Main menu
│   │   ├── dialog.py          # Dialogue system
│   │   ├── save_menu.py       # Save/Load screen
│   │   └── tkinter_gui.py     # Tkinter overlays
│   └── world/                 # Game world
│       ├── campus.py          # Campus map
│       ├── building.py        # Building class
│       ├── location.py        # Location class
│       └── npc_scheduler.py   # NPC routines
└── docs/                      # Documentation
    ├── architecture.md        # System architecture
    ├── api_reference.md       # API documentation
    └── user_guide.md          # User manual
```

---

## Educational Design

### How OOP Concepts Map to Gameplay

| OOP Concept | In-Game Representation |
|-------------|----------------------|
| **Classes** | University blueprint (Student class, Lecturer class) |
| **Objects** | You, as an instance of Student |
| **Constructors** | Registration desk creating your profile |
| **Attributes** | Your name, ID, department, GPA |
| **Methods** | attend_lecture(), submit_assignment() |
| **Encapsulation** | Bank account — data access controlled via methods |
| **Inheritance** | Departments inherit from a base Department class |
| **Polymorphism** | Different lecturers teach the same course differently |
| **Abstraction** | Timetable hides scheduling complexity |
| **Composition** | University is composed of departments, buildings, students |
| **Observer Pattern** | University announcement system notifies subscribers |
| **Singleton** | The University itself — only one instance |
| **Factory Pattern** | Registration Office creates Student objects |

### Year-by-Year Progression

| Year | Theme | Concepts Introduced |
|------|-------|-------------------|
| **Year 1** | Becoming an Object | Classes, Objects, Constructors, Attributes, Methods, Encapsulation |
| **Year 2** | Relationships | Inheritance, Composition, Aggregation, Association, Polymorphism |
| **Year 3** | Advanced Architecture | Abstract Classes, Interfaces, Duck Typing, Packages, Exception Handling |
| **Year 4** | Software Engineer | Design Patterns, Factory, Singleton, Observer, Strategy, MVC |

---

## Save System

The game includes a complete progress-saving system:

- **Manual Save**: Save at any safe location or via pause menu (F5 quick save)
- **Autosave**: Automatically after major missions, exams, story events
- **Checkpoint Save**: Before difficult missions or major story branches
- **Chapter Save**: Permanent backup at end of each chapter/semester
- **5 Save Slots**: Multiple playthroughs or alternate choices
- **Session Resume**: Continue exactly where you left off

Saved data includes: player identity, academic progress, mission status, inventory, reputation, attendance, timetable, discovered locations, dialogue history, world state, and more.

---

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Building Distribution

```bash
python setup.py sdist bdist_wheel
```

### Project Status

This project is in **alpha** stage. Core gameplay systems are functional, including movement, NPC interaction, save/load, OOP tutorials, and the Tkinter GUI overlay system. Future releases will add full sprite art, audio, and expanded mission content.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Mbeya University of Science and Technology (MUST)** — Institutional inspiration
- **Professor Object** — Fictional AI mentor and guide through the Object Framework
- The open-source community for Pygame and Python ecosystem tools

---

*"You did not simply graduate. You learned to think like a software engineer."*
