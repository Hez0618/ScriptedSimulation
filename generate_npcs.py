import json
import os

os.makedirs("npc_data", exist_ok=True)

npc_profiles = [
    {
        "name": "Ethan",
        "age": 20,
        "background": [
            "I was born into a wealthy family in Riverton and lived in a luxurious villa on Rosewood Hill.",
            "My father passed away when I was young, leaving me to take care of my mother and younger sister, Angel.",
            "In 2007, my sister was kidnapped and killed after the ransom was paid. My mother fell into depression and committed suicide in 2008.",
            "I was sent to an orphanage and became rebellious, eventually joining underground boxing at 15.",
            "By 19, I became the undefeated champion in Riverton's underground fight scene.",
            "In December 2016, I received a tip that the man I was looking for, Marcus, was involved in illegal activities on the Siberian railway."
        ],
        "memory": [
            {
                "id": 1,
                "day": 1,
                "time": "22:00",
                "event": "The train departs. I sit in my cabin (Car 10, Room 2), waiting for the attendant to check rooms.",
                "reaction": "I'm planning to steal her passenger log after she passes."
            },
            {
                "id": 2,
                "day": 1,
                "time": "22:50",
                "event": "The attendant reaches my car. She looks familiar. I quietly follow her to see where she goes.",
                "reaction": "Is she connected to Angel’s case?"
            },
            {
                "id": 3,
                "day": 1,
                "time": "23:15",
                "event": "She leaves the attendant's room in Car 9. I sneak in and grab the passenger log.",
                "reaction": "No one saw me. I need to find Marcus."
            },
            {
                "id": 4,
                "day": 1,
                "time": "23:30",
                "event": "After some searching, I find Marcus’s cabin and take a photo of his info. I ditch the log in Car 10.",
                "reaction": "It’s time. I can’t let him get away."
            },
            {
                "id": 5,
                "day": 1,
                "time": "00:05",
                "event": "With my knife ready, I sneak into Marcus’s room and stab him in the chest three times while he sleeps.",
                "reaction": "One for Angel, one for Mom, and one for myself."
            },
            {
                "id": 6,
                "day": 1,
                "time": "00:08",
                "event": "I go to the restroom and wash the blood from the knife.",
                "reaction": "Stay calm. No one saw me."
            },
            {
                "id": 7,
                "day": 1,
                "time": "00:10",
                "event": "I return to my cabin and hide the knife.",
                "reaction": "It’s over. I just need to act normal now."
            },
            {
                "id": 8,
                "day": 1,
                "time": "00:15",
                "event": "Suddenly, a loud crash—then the train comes to a halt.",
                "reaction": "What happened? Did someone find the body already?"
            }
        ]
    },
    {
        "name": "Jax",
        "age": 27,
        "background": [
            "I grew up in a small village near Tieling.",
            "I dropped out of high school and became a street thug.",
            "I'm 27 now. Making money is my dream—but not dirty money.",
            "Six months ago, Marcus came to our village to buy rare herbs.",
            "I became his local guide and served him well.",
            "Two months ago, he invited me to work with him officially.",
            "I learned he’s using the railway to smuggle shady stuff.",
            "I hesitated, but his money was tempting.",
            "A week ago, he gave me two train tickets to Moscow.",
            "He refused to tell me what we’re transporting.",
            "I asked around—he’s hiding diamonds.",
            "There’s also a dangerous man on board—Uncle Li.",
            "I brought a disguise, tools, and my village’s sharpest sickle.",
            "I plan to kidnap Marcus and take the diamonds for myself."
    ],
        "memory": [
            {
                "entry_id": 1,
                "day": 1,
                "time": "22:00",
                "event": "I boarded the train with Marcus. He still didn't mention anything about the diamonds.",
                "reaction": "He's too cautious. He stayed in car 7, I stayed in car 9."
            },
            {
                "entry_id": 2,
                "day": 1,
                "time": "22:15",
                "event": "I left my room to check Marcus’s room and see if it was easy to access.",
                "reaction": "I needed to scout the area before acting."
            },
            {
                "entry_id": 3,
                "day": 1,
                "time": "22:18",
                "event": "Outside Marcus’s room, I saw a woman arguing with him.",
                "reaction": "Turns out she was 'Uncle Li'—they were fighting over territory and trust."
            },
            {
                "entry_id": 4,
                "day": 1,
                "time": "22:20",
                "event": "The woman left. Marcus saw me and pulled me into his room, furious.",
                "reaction": "He scolded me for sneaking around. I kept quiet."
            },
            {
                "entry_id": 5,
                "day": 1,
                "time": "22:30",
                "event": "Marcus said he wanted to rest, so I left and went to the dining car.",
                "reaction": "I ate a little, then set an alarm for 23:30 and went to sleep."
            },
            {
                "entry_id": 6,
                "day": 1,
                "time": "23:40",
                "event": "I woke up late. My stomach hurt—maybe the food was bad.",
                "reaction": "The plan was delayed, but I still had to act."
            },
            {
                "entry_id": 7,
                "day": 1,
                "time": "23:43",
                "event": "I brought my sickle and went to the restroom first.",
                "reaction": "Needed to prepare myself and check the corridor."
            },
            {
                "entry_id": 8,
                "day": 1,
                "time": "23:50",
                "event": "I sneaked into Marcus’s room. He looked asleep, so I took the diamonds.",
                "reaction": "He didn’t move at all... I grabbed them and ran."
            },
            {
                "entry_id": 9,
                "day": 1,
                "time": "23:54",
                "event": "I left the room quickly.",
                "reaction": "My heart was racing—I had the diamonds."
            },
            {
                "entry_id": 10,
                "day": 1,
                "time": "23:55",
                "event": "I bumped into the attendant Ou and the woman Lin.",
                "reaction": "I clutched the diamonds tightly and rushed off."
            },
            {
                "entry_id": 11,
                "day": 1,
                "time": "00:00",
                "event": "Back in my room, I realized my phone was missing.",
                "reaction": "Did I forget it? Or did someone take it?"
            },
            {
                "entry_id": 12,
                "day": 1,
                "time": "00:10",
                "event": "I stole a random passenger’s phone and texted my brother to pick me up.",
                "reaction": "Just then, a loud bang hit and I was thrown into the wall."
            },
            {
                "entry_id": 13,
                "day": 1,
                "time": "00:15",
                "event": "The train stopped. A broadcast said we were stuck and couldn’t move.",
                "reaction": "Perfect timing or bad luck?"
            }
        ]
    }
    # 可以继续添加更多NPC
]

for npc in npc_profiles:
    with open(f"npc_data/{npc['name'].lower()}.json", "w", encoding="utf-8") as f:
        json.dump(npc, f, indent=4, ensure_ascii=False)