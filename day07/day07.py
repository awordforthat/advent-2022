with open("input.txt") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

MAX_DISK_SPACE = 70000000
NEEDED_SPACE = 30000000
tree = {}


class Node:
    def __init__(self, path, parent_id=None):
        assert type(parent_id) == str or parent_id == None
        self._path = path
        self._parent = parent_id
        self._contents = {}
        self._children = set()

    def __str__(self):
        return f"Node {self._path} has parent {self._parent}, children {self._children}, and contents {self._contents}"

    def get_contents(self):
        return self._contents

    def get_children(self):
        return self._children

    def add_child(self, child_id):
        assert type(child_id) == str
        self._children.add(child_id)

    def add_content(self, file_name, file_size):
        assert file_name not in self._contents
        self._contents[file_name] = file_size

    def get_contents_size(self):
        return sum(self._contents.values())

    def get_id(self):
        return self._path


pointer = None
path = []
for index, line in enumerate(lines):
    if line.startswith("$ cd"):
        _, target = line.split("$ cd ")
        if target == "..":
            path = path[:-1]
        else:
            target_path = "".join(path) + target
            if target_path not in tree:
                tree[target_path] = Node(path=target_path, parent_id=pointer)
            path.append(target)
    elif line.startswith("dir "):
        _, target = line.split("dir ")
        current_path = "".join(path)
        target_path = "".join(path) + target
        if target_path not in tree:
            tree[target_path] = Node(path=target_path, parent_id=pointer)
        tree[current_path].add_child(target_path)
    elif not line.startswith("$ ls"):
        # raw files here
        current_node = tree["".join(path)]
        file_size, file_name = line.split(" ")
        current_node.add_content(file_name, int(file_size))


def get_size(node_id, current_size=0):
    node = tree[node_id]
    current_size += node.get_contents_size()
    for child in node.get_children():
        current_size = get_size(child, current_size)
    return current_size


def a():
    results = []
    for node_id in tree:
        node_size = get_size(node_id, 0)
        if node_size <= 100000:
            results.append(node_size)
    print(sum(results))


def b():
    free_space = MAX_DISK_SPACE - get_size("/")
    need_to_free = NEEDED_SPACE - free_space
    winning_node = ""
    winning_node_size = float("inf")
    for node_id in tree:
        node_size = get_size(node_id, 0)
        if node_size >= need_to_free and node_size < winning_node_size:
            winning_node = node_id
            winning_node_size = node_size
    print(winning_node, winning_node_size)


a()
b()
