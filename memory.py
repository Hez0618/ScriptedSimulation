import json
import os
from typing import List
from generate_chatgpt import simplify_memory_with_gpt

class MemoryEntry:
    def __init__(self, day, time, event, reaction, entry_id=None):
        self.entry_id = entry_id
        self.day = day
        self.time = time
        self.event = event
        self.reaction = reaction

    def to_dict(self):
        return {
            "entry_id": self.entry_id,
            "day": self.day,
            "time": self.time,
            "event": self.event,
            "reaction": self.reaction
        }

    @staticmethod
    def from_dict(data):
        return MemoryEntry(
            entry_id=data["entry_id"],
            day=data["day"],
            time=data["time"],
            event=data["event"],
            reaction=data["reaction"]
        )

def load_npc_memory(name: str, folder="memory_data") -> List[MemoryEntry]:
    path = os.path.join(folder, f"{name}.json")
    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [MemoryEntry.from_dict(entry) for entry in data]

def save_npc_memory(name: str, memory_list: List[MemoryEntry], folder="memory_data"):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{name}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump([entry.to_dict() for entry in memory_list], f, indent=4, ensure_ascii=False)
    print(f"[✓] Memory saved for {name} at {path}")

def get_next_entry_id(memory_list: List[MemoryEntry]) -> int:
    ids = []
    for entry in memory_list:
        try:
            ids.append(int(entry.entry_id))
        except (ValueError, TypeError):
            continue
    if not ids:
        return 1
    return max(ids) + 1

def add_memory_entry(name: str, day: int, time: str, raw_event: str, raw_reaction: str, folder="memory_data"):
    memory_list = load_npc_memory(name, folder)
    entry_id = get_next_entry_id(memory_list)
    event, reaction = simplify_memory_with_gpt(raw_event, raw_reaction)
    new_entry = MemoryEntry(entry_id, day, time, event, reaction)
    memory_list.append(new_entry)
    save_npc_memory(name, memory_list, folder)


class Memory:
    def __init__(self, filename=None):
        self.entries = []
        self.filename = filename
        self.entry_counter = 1
        if filename:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            self.load_from_file()

    def add(self, entry):
        entry.entry_id = self.entry_counter
        self.entries.append(entry)
        self.entry_counter += 1
        if self.filename:
            self.save_to_file()

    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump([entry.to_dict() for entry in self.entries], f, indent=4)

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.entries = [MemoryEntry(**entry) for entry in data]
                self.entry_counter = len(self.entries) + 1

    def pretty_print(self):
        for entry in self.entries:
            print(f"ID: {entry.entry_id} | Day: {entry.day} | Event: {entry.event} | Reaction: {entry.reaction}")

