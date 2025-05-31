from typing import Optional, Dict
import json

class WorldNode:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.children: Dict[str, 'WorldNode'] = {}
        self.clue = None
        self.description = description

    def add_child(self, child_name: str, description: str = "") -> 'WorldNode':
        if child_name not in self.children:
            self.children[child_name] = WorldNode(child_name, description)
        return self.children[child_name]

    def find_node_by_path(self, path: list[str]) -> Optional['WorldNode']:
        if not path:
            return self
        first, *rest = path
        child = self.children.get(first)
        if not child:
            return None
        return child.find_node_by_path(rest)

    def get_all_clues(self) -> list[dict]:
        clues = []
        if self.clue:
            clues.append(self.clue)
        for child in self.children.values():
            clues.extend(child.get_all_clues())
        return clues

    def __repr__(self, level=0):
        indent = "  " * level
        s = f"{indent}- {self.name}"
        if self.description:
            s += f" ({self.description})"
        if self.clue:
            s += f" [Clue: {self.clue['name']}]"
        for child in self.children.values():
            s += "\n" + child.__repr__(level + 1)
        return s


def create_world_from_clues(file_path: str) -> WorldNode:
    with open(file_path, 'r', encoding='utf-8') as f:
        clues = json.load(f)

    root = WorldNode("Train")

    for clue in clues:
        path = clue['location']
        node = root
        for p in path[1:]:
            node = node.add_child(p)
        node.clue = clue

    return root


def add_non_clue_node(root: WorldNode, path: list[str], node_name: str, description: str = ""):
    # 跳过根节点名称
    parent_node = root.find_node_by_path(path[1:])
    if parent_node is None:
        raise ValueError(f"路径{' -> '.join(path)}未找到，无法添加节点。")
    parent_node.add_child(node_name, description)

def add_non_clue_nodes_batch(root: WorldNode, nodes: list[dict]):
    """
    nodes is a list of dictionaries, each containing:
    {
        "path": [...],          # Parent node path, e.g. ["Train", "Carriage 9", "Room 5"]
        "node_name": "Desk",    # Name of the new node
        "description": "Description text"  # Optional description
    }
    """
    for node_info in nodes:
        path = node_info["path"]
        name = node_info["node_name"]
        desc = node_info.get("description", "")
        try:
            add_non_clue_node(root, path, name, desc)
        except ValueError as e:
            print(f"fail to add node: {e}")


if __name__ == "__main__":
    world = create_world_from_clues("clue_data/clues.json")

    nodes_to_add = [
        {
            "path": ["Train", "Carriage 9", "Room 5"],
            "node_name": "Desk",
            "description": "An old wooden desk covered in dust, nothing unusual."
        },
        {
            "path": ["Train", "Carriage 9", "Room 5", "Desk"],
            "node_name": "Drawer",
            "description": "A small drawer with a faded lock, it seems empty."
        }
    ]

    add_non_clue_nodes_batch(world, nodes_to_add)

    print(world)

