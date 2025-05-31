import os
import json
from clue import Clue

def main():
    os.makedirs("clue_data", exist_ok=True)

    clues = [
        Clue(
            clue_id=1,
            name="Boxing Champion Photo",
            description="A photo of Ethan with a boxing champion, showing his underground past.",
            location=["Train", "Carriage 10", "Room 2", "Ethan's Room"],
            owner="Ethan",
            owner_memory="This photo reminds me of my days fighting in underground boxing rings."
        ),
        Clue(
            clue_id=2,
            name="Secret Letter",
            description="A letter revealing hidden business between Jax and Marcus.",
            location=["Train", "Carriage 9", "Room 5", "Wardrobe"],
            owner="Jax",
            owner_memory="This letter made me realize Marcus is involved in shady deals."
        )
        # 可以继续添加更多Clue实例
    ]

    # 把Clue对象转换成dict列表
    clues_data = [clue.__dict__ for clue in clues]

    with open("clue_data/clues.json", "w", encoding="utf-8") as f:
        json.dump(clues_data, f, indent=4, ensure_ascii=False)

    print("All clues data saved to clue_data/clues.json")

if __name__ == "__main__":
    main()

