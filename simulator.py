import random
from memory import add_memory_entry, MemoryEntry
from generate_chatgpt import generate_npc_daily_plan_with_schedule_and_time, generate_npc_action_reaction, generate_npc_exploration_reaction

def simulate_day(day: int, npcs: list, world) -> list[dict]:
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
            event, reaction = generate_npc_action_reaction(npc, action)
            logs.append({
                "npc": npc.name,
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

            npc.memory.append({
                "id": len(npc.memory) + 1,
                "day": day,
                "time": action_time,
                "event": event,
                "reaction": reaction
            })

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


