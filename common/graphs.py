# Graph as dict
graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


# Graph as set of nodes
class Node:

    def __init__(self, name: str):
        self.name = name
        self.parent = None
        self.children = list()

    def set_parent(self, parent):
        self.parent = parent

    def set_children(self, children):
        for child in children:
            self.children.append(child)
            child.set_parent(self)

    def __str__(self):
        return self.name


mega_root = Node(name="mega_root")
root = Node(name="root")

ch1 = Node(name="ch1")
ch2 = Node(name="ch2")

root.set_children(children=[ch1, ch2])
root.set_parent(parent=mega_root)

print(root.children, root.parent, ch1.parent)
