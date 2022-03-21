from .BaseCollection import Collection
class LinearCollection(Collection):
    def __init__(self) -> None:
        super().__init__()
        self.members = list()
    def add(self, node):
        self.members.append(node)
    def contains(self, node):
        return node in self.members
    def __contains__(self, node):
        return self.contains(node)
    def size(self):
        return len(self.members)
    def clear(self):
        self.members = list()
    def get(self, index: int):
        return self.members[index]
    def __getitem__(self, index: int):
        return self.members[index]