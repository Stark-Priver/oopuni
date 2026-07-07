# OOP UNI — User Guide

## Getting Started

### Installation

1. Ensure Python 3.8+ is installed: `python --version`
2. Install Pygame: `pip install pygame`
3. Run the game: `python main.py`

### Main Menu

When you launch the game, you will see the main menu with three options:

- **New Game** — Start a fresh journey from the beginning
- **Load Game** — Continue from a previously saved game
- **Quit** — Exit the game

Use the **UP/DOWN arrow keys** to navigate and **ENTER** to select.

---

## Gameplay

### Movement

Use the **WASD** or **Arrow Keys** to move your character around the campus. The camera follows your character automatically.

### Campus Layout

The campus is a large open world with the following key locations:

| Location | Purpose |
|----------|---------|
| **Administration** | Student registration, profile creation |
| **Library** | Books, OOP tutorials, quiet study |
| **Lecture Theatres** | Attend lectures, meet lecturers |
| **Innovation Hub** | Advanced projects, design patterns |
| **Computer Lab** | Programming practice |
| **Laboratories** | Scientific experiments |
| **Student Centre** | Social hub, clubs, student government |
| **Cafeteria** | Food, social interactions |
| **Bank** | Encapsulation tutorial |
| **Hostel Blocks** | Rest, save, composition tutorial |
| **Bookshop** | Buy supplies |
| **Health Centre** | Medical services |
| **Sports Complex** | Athletics, recreation |
| **Engineering Workshop** | Practical engineering |
| **Main Gate** | Campus entrance |

### Controls Reference

| Key | Action |
|-----|--------|
| **W / Arrow Up** | Move up |
| **S / Arrow Down** | Move down |
| **A / Arrow Left** | Move left |
| **D / Arrow Right** | Move right |
| **ESC** | Pause / Unpause |
| **F5** | Quick Save |
| **F9** | Quick Load |
| **TAB** | Open Save/Load Menu |
| **I** | Open Player Info window |
| **M** | Open Campus Map window |
| **J** | Open Missions window |
| **C** | Open Calendar window |
| **R** | Open Reputation window |
| **SPACE** | Advance dialogue |
| **ENTER** | Confirm selection |
| **DELETE** | Delete selected save |

---

## Game Systems

### Save System

The game offers multiple ways to preserve your progress:

**Quick Save (F5):** Saves instantly to a dedicated quicksave slot. Load with **F9**.

**Save Menu (TAB):** Open the save/load menu to manage 5 save slots. Each slot shows:
- Player name
- Academic year and department
- Date and time of save

**Autosave:** The game automatically saves after:
- Completing major missions
- Finishing exams
- Reaching story milestones
- Discovering important locations

**Tips:**
- Save before entering unknown areas
- Use different slots to experiment with choices
- Quick Save is fastest for frequent saving

### Mission System

Missions guide your journey through the university. Each mission has:
- **Title** and **Description**
- **Objectives** to complete
- **Progress tracker** showing steps completed
- **Reputation rewards** upon completion

Access your missions with **J** key to see:
- Active missions (current tasks)
- Completed missions (achievements)

### Academic Calendar

The game follows a realistic university timeline:

- **4 Academic Years**, each with 2 semesters
- Each semester has events: Registration → Classes → Assessments → Exams → Break
- Your actions during each semester affect your academic standing

Press **C** to view the current calendar status and today's timetable.

### Reputation System

Build relationships with 8 campus factions:

| Faction | How to Improve |
|---------|----------------|
| **Lecturers** | Attend lectures, complete assignments |
| **Departments** | Visit departments, complete departmental missions |
| **Student Government** | Participate in student activities |
| **Library** | Borrow and return books |
| **Innovation Hub** | Work on innovative projects |
| **Sports** | Participate in sports activities |
| **Research Office** | Conduct research |
| **Career Centre** | Attend career workshops |

Higher reputation unlocks exclusive missions, dialogue options, and academic opportunities.

Press **R** to view your reputation standing with all factions.

---

## Chapter 1 Walkthrough

### Admission Sequence

1. Start a **New Game** from the main menu
2. Watch the admission cinematic (dialogue will appear automatically)
3. You will receive your **Student ID**, **Registration Number**, and other items
4. **Professor Object** introduces himself and explains the Chaos Bug
5. Your first mission, "The Admission Letter," begins

### Orientation

1. Explore the campus freely
2. Visit key locations like the **Library**, **Student Centre**, and **Cafeteria**
3. Talk to NPCs by walking near them
4. Complete the "Orientation Week" mission by visiting all required locations

### First Lecture

1. Check your timetable with **C**
2. Find **Lecture Theatre A** on the map (**M**)
3. Attend the OOP Principles lecture
4. Meet the lecturer and learn about classes and objects

### Save Often!

After completing the admission sequence, use **F5** to quick save. This ensures you never lose your progress.

---

## OOP Learning Guide

### Year One: Becoming an Object

Focus on understanding:
- What makes you a **Student object**
- How the **registration desk** acts as a constructor
- Your **attributes**: name, ID, department
- Your **methods**: walking, talking, studying

Visit these locations in order:
1. **Administration** — Classes and Objects tutorial
2. **Library** — Attributes and Methods tutorial
3. **Bank** — Encapsulation tutorial

### Year Two: Relationships

Observe how:
- Different **departments** inherit from a base structure
- **Lecturers** demonstrate polymorphism through different teaching styles
- The **hostel** demonstrates composition (rooms inside a building)

### Year Three: Advanced Architecture

Experience:
- **Industrial training** at companies in Mbeya
- **Abstract systems** like the timetable and scheduling
- **Exception handling** when things go wrong

### Year Four: Software Engineer

Master:
- **Design patterns** at the Innovation Hub
- The **Observer pattern** through the university notification system
- Your **Final Year Project** — the ultimate challenge

---

## Troubleshooting

### Game won't start

```bash
# Ensure Pygame is installed
pip install pygame
# Run directly
python main.py
```

### Tkinter windows not showing

Tkinter is included with Python by default. If windows don't appear:
- Ensure you're not running in a headless environment
- On Linux: `sudo apt-get install python3-tk`

### Save files not loading

- Check that the `saves/` directory exists
- Verify save files are valid JSON (can open in text editor)
- Save files are stored in: `C:\Users\Priver\oopuni\saves\`

### Performance issues

- Close other applications
- Reduce the game resolution in `src/config.py`
- Ensure graphics drivers are up to date

---

## Support

For issues, feature requests, or contributions:
- GitHub: https://github.com/Stark-Priver/oopuni
- Report issues: https://github.com/Stark-Priver/oopuni/issues

---

*"The university you know is only the interface. Beneath it lies the architecture that keeps everything alive."* — Professor Object
