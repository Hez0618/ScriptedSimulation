import random
import os
import json
from memory import add_memory_entry, MemoryEntry, save_npc_memory
from generate_chatgpt import generate_npc_daily_plan_with_schedule_and_time, generate_npc_action_reaction, generate_npc_exploration_reaction

def initialize_npc_memory(npc, npc_data_folder="npc_data", memory_folder="memory_data"):

    mem_path = os.path.join(memory_folder, f"{npc.name}.json")
    if os.path.exists(mem_path):
        print(f"[init] Memory file exists for {npc.name}, skipping initialization.")
        return

    npc_file = os.path.join(npc_data_folder, f"{npc.name}.json")
    if not os.path.exists(npc_file):
        print(f"[init] NPC data file not found for {npc.name} at {npc_file}")
        return

    with open(npc_file, "r", encoding="utf-8") as f:
        npc_data = json.load(f)

    initial_memory = npc_data.get("memory", [])

    memory_list = []
    for i, mem in enumerate(initial_memory):
        entry = MemoryEntry(
            entry_id=mem.get("id", i + 1),
            day=mem.get("day", 0),
            time=mem.get("time", "00:00"),
            event=mem.get("event", ""),
            reaction=mem.get("reaction", "")
        )
        memory_list.append(entry)

    save_npc_memory(npc.name, memory_list, folder=memory_folder)
    print(f"[init] Initialized memory for {npc.name} with {len(memory_list)} entries.")

def simulate_day(day: int, npcs: list, world) -> list[dict]:
    for npc in npcs:
        initialize_npc_memory(npc)
    logs = []
    all_clues = world.get_all_clues()
    # 先记录一天开始的事件
    for npc in npcs:
        logs.append({
            "npc": npc.name,
            "time": "start",
            "event": "Start day",
            "reaction": ""
        })

        # 生成每日计划，带时间点（如你之前想要的“早餐后探索”“午餐后探索”）
        plan = generate_npc_daily_plan_with_schedule_and_time(npc)
        # 假设计划对应的时间点（可根据需要改）
        times = ["08:00", "12:00", "18:00"]

        for action, action_time in zip(plan, times):
            print(action)
            event, reaction = generate_npc_action_reaction(npc, action)
            print(event)
            print(reaction)
            logs.append({
                "npc": npc.name,
                "time": action_time,
                "event": event,
                "reaction": reaction
            })

            npc.memory.append({
                "id": len(npc.memory) + 1,
                "day": day,
                "time": action_time,
                "event": event,
                "reaction": reaction
            })

            add_memory_entry(
                name=npc.name,
                day=day,
                time=action_time,
                raw_event=event,
                raw_reaction=reaction
            )

            # 每次活动后，模拟探索（假设探索和活动交替进行）
            if all_clues:
                clue = random.choice(all_clues)
                is_owner = clue.get("owner") == npc.name
                reaction = generate_npc_exploration_reaction(npc, clue, owner=is_owner)

                logs.append({
                    "npc": npc.name,
                    "time": f"{action_time} + exploration",
                    "event": f"Explored {clue.get('location', 'unknown location')} and found clue: {clue['name']}",
                    "reaction": reaction
                })

                npc.memory.append({
                    "id": len(npc.memory) + 1,
                    "day": day,
                    "time": f"{action_time} + exploration",
                    "event": f"Explored {clue.get('location', 'unknown location')} and found clue: {clue['name']}",
                    "reaction": reaction
                })

                add_memory_entry(
                    name=npc.name,
                    day=day,
                    time=f"{action_time} + exploration",
                    raw_event="default event",
                    raw_reaction=reaction
                )

    return logs


