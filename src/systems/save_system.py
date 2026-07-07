import json
import os
import datetime
from src.config import SAVES_DIR, SAVE_SLOTS


class SaveSystem:
    def __init__(self):
        self.save_dir = SAVES_DIR
        os.makedirs(self.save_dir, exist_ok=True)

    def save(self, slot, data):
        if slot < 0 or slot >= SAVE_SLOTS:
            return False
        data["saved_at"] = datetime.datetime.now().isoformat()
        data["slot"] = slot
        filepath = os.path.join(self.save_dir, f"save_{slot}.json")
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        return True

    def load(self, slot):
        if slot < 0 or slot >= SAVE_SLOTS:
            return None
        filepath = os.path.join(self.save_dir, f"save_{slot}.json")
        if not os.path.exists(filepath):
            return None
        with open(filepath, "r") as f:
            return json.load(f)

    def delete(self, slot):
        if slot < 0 or slot >= SAVE_SLOTS:
            return False
        filepath = os.path.join(self.save_dir, f"save_{slot}.json")
        if os.path.exists(filepath):
            os.remove(filepath)
            return True
        return False

    def get_slot_info(self, slot):
        data = self.load(slot)
        if not data:
            return None
        return {
            "slot": slot,
            "player_name": data.get("player", {}).get("name", "Unknown"),
            "academic_year": data.get("player", {}).get("academic_year", "Unknown"),
            "department": data.get("player", {}).get("department", "Unknown"),
            "saved_at": data.get("saved_at", "Unknown"),
            "playtime": data.get("game_timer", {}).get("total_seconds", 0)
        }

    def get_all_slots(self):
        slots = []
        for i in range(SAVE_SLOTS):
            info = self.get_slot_info(i)
            slots.append(info)
        return slots

    def quick_save(self, data):
        data["saved_at"] = datetime.datetime.now().isoformat()
        data["slot"] = "quicksave"
        filepath = os.path.join(self.save_dir, "quicksave.json")
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        return True

    def quick_load(self):
        filepath = os.path.join(self.save_dir, "quicksave.json")
        if not os.path.exists(filepath):
            return None
        with open(filepath, "r") as f:
            return json.load(f)

    def autosave(self, data):
        data["saved_at"] = datetime.datetime.now().isoformat()
        data["slot"] = "autosave"
        filepath = os.path.join(self.save_dir, "autosave.json")
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        return True

    def autoload(self):
        filepath = os.path.join(self.save_dir, "autosave.json")
        if not os.path.exists(filepath):
            return None
        with open(filepath, "r") as f:
            return json.load(f)

    def get_save_count(self):
        count = 0
        for fname in os.listdir(self.save_dir):
            if fname.endswith(".json"):
                count += 1
        return count
