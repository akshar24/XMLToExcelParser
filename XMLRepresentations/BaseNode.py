from DataStructures.BaseCollection import Collection
class Node:
    def __init__(self, name: str):
        self.name = name
        self._parent: Node = None
        self.children: Collection = Collection()
    def add(self, child):
        if not isinstance(child, Node):
            raise TypeError("Child must be of type node")
        if child._parent:
            raise ValueError("Child must be orphaned to be linked to parent")
        child._parent = self
        self.children.add(child)
    def __iter__(self):
        return iter(self.children)
        


    
