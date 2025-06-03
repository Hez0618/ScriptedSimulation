import json

class Clue:
    """
    Clue Instance
    A clue contains identifying information, a description,
    locations, its current owner, and the owner's memory or interpretation.
    
    Args:
    clue_id: Unique identifier for the clue
    name: Name of the Clue
    description: Detailed explanation of what the clue is
    location: List of possible locations related to the clue.
    owner: Name of the character currently holding the clue.
    owner_memory: Description of the owner's memory or perspective of the clue.
    """
    def __init__(self, clue_id, name, description, location, owner, owner_memory):
        self.clue_id = clue_id
        self.name = name
        self.description = description
        self.location = location
        self.owner = owner
        self.owner_memory = owner_memory

    def to_dict(self):
        return {
            "clue_id": self.clue_id,
            "name": self.name,
            "description": self.description,
            "location": self.location, #List[str]
            "owner": self.owner,
            "owner_memory": self.owner_memory
        }

    def save_to_file(self, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_file(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return Clue(
            clue_id=data["clue_id"],
            name=data["name"],
            description=data["description"],
            location=data["location"],
            owner=data["owner"],
            owner_memory=data["owner_memory"]
        )
