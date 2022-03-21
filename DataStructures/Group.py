from .BaseCollection import Collection
from .AttributesCollection import AttributesCollection
class MergeableGroup:
    def __init__(self) -> None:
        pass
    def merge(self):
        pass
class Group(Collection, MergeableGroup):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.members = list()
    def add(self, xmlDataNode):
        self.members.append(xmlDataNode)
    def get(self, index: int):
        return self.members[index]
    def contains(self, xmlDataNode):
        return xmlDataNode in self.members
    def merge(self):
        return super().merge()
    def clear(self):
        self.members = list()
    def __iter__(self):
        return iter(self.members)
    def size(self):
        return len(self.members)
class Groups(AttributesCollection, MergeableGroup):
    def __init__(self):
        super().__init__()
    def merge(self):
        return super().merge()
    def get(self, attributeName: str, default  = None) -> Group:
        return super().get(attributeName)
    