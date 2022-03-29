class BaseIterator:
    def __init__(self, creator, default = None) -> None:
        self.iteratorCreator = creator
        self.iterator = self.iteratorCreator()
        self.initial = True
        self.default = default
        self.curr = self.default
        self.next()
    def next(self):
        if not self.hasNext():
            return self.curr
        currElement = self.curr
        self.curr = next(self.iterator, self.default)
        self.initial =  False
        return currElement
    def hasNext(self):
        if self.initial:
            return True
        return not (self.curr is self.default or self.curr == self.default)
    def __iter__(self):
        yield self.next() 
        while self.hasNext():
            yield self.next()
    def reset(self):
        self.iterator = self.iteratorCreator()
        self.curr = next(self.iterator, self.default)
    def __next__(self):
        return self.next()