import os
import json
from npc import NPC
from world_structure import create_world_from_clues
from simulator import simulate_day

def load_all_npcs(npc_folder="npc_data"):
    npcs = []
    for filename in os.listdir(npc_folder):
        if filename.endswith(".json"):
            with open(os.path.join(npc_folder, filename), "r", encoding="utf-8") as f:
                data = json.load(f)
            npc = NPC(
                name=data.get("name", ""),
                age=data.get("age", 0),
                background=data.get("background", []),
                memory=data.get("memory", [])
            )
            npcs.append(npc)
    return npcs

if __name__ == "__main__":
    # 1. Load world
    world = create_world_from_clues("clue_data/clues.json")

    # 2. Load NPCs
    npcs = load_all_npcs()

    # 3. Simulate Day 2
    day = 2
    logs = simulate_day(day, npcs, world)

    # 4. Print logs
    print(f"\n--- Day {day} Simulation Log ---\n")
    for entry in logs:
        if "system" in entry:
            print(entry["system"])
        else:
            print(f"{entry['npc']} at {entry['time']}:")
            print(f"  Event: {entry['event']}")
            print(f"  Reaction: {entry['reaction']}")
            print()
