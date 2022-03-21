class Collection:
    def __init__(self) -> None:
        self.members = None
        pass 
    def add(self, *args, **kwargs): 
        pass
    def get(self, *args, **kwargs):
        pass
    def contains(self, *args, **kawrgs):
        pass
    def size() -> int:
        pass
    def empty(self):
        return self.size() == 0
    def __len__(self):
        return self.size()
    def __iter__(self):
        return iter(self.members) if self.members is not None else None
    def clear(self):
        pass
    def __next__(self):
        pass
    def print(self):
        print(self.members)
    def __str__(self) -> str:
        return str(self.members)

