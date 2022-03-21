from .BaseCollection import Collection
class AttributesCollection(Collection):
    def __init__(self, default = None) -> None:
        super().__init__()
        self.members = dict()
        self.default = default
    def add(self, attributeName: str, attributeValue):
        self.members[attributeName]  = attributeValue
    def get(self, attributeName: str, default = None):
        return self.members.get(attributeName, self.default if default is None else default)
    def contains(self, attributeName: str):
        return attributeName in self.members
    def __setitem__(self, attributeName, attributeValue):
        self.add(attributeName, attributeValue)
    def __getitem__(self, attributeName):
        return self.get(attributeName = attributeName, default = self.default)
    def __getattr__(self, name: str):
        return self.get(attributeName = name, default = self.default)


    def __contains__(self, attributeName):
        return self.contains(attributeName)
    def size(self):
        return len(self.members)
    def clear(self):
        self.members = dict()
    def __iter__(self):
        return iter(self.members.items())
    def __call__(self, attributeName):
        return self.get(attributeName)
        
     

    
    
