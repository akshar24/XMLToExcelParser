from .Iterator import BaseIterator
from collections import deque, defaultdict
from XMLRepresentations.BaseNode import Node
class DepthFirstIteratorElement:
    def __init__(self, ele, depth, subtreeExplored = False) -> None:
        self.element = ele
        self.depth = depth
        self.subtreeExplored = subtreeExplored
class DepthFirstOrderIterator(BaseIterator):
    def __init__(self, root: Node) -> None:
        self.root = root
        super().__init__(self.__iterator__)
        
    def __shouldYield__(self, currNode: DepthFirstIteratorElement):
        return not currNode.subtreeExplored
    def __iterator__(self):
        stack = deque() 
        iterators = dict()
        stack.append(DepthFirstIteratorElement(self.root, 0, False))
        while stack:
            currNode: DepthFirstIteratorElement = stack[-1]
            iterator = None
            if currNode.element not in iterators:
                if self.__shouldYield__(currNode):
                    yield currNode
                iterator = iter(currNode.element)
                iterators[currNode.element] = iterator
            else: iterator = iterators[currNode.element]
            child = next(iterator, None)
            while child in iterators:
                child = next(iterator, None)
            if child is None:
                currNode.subtreeExplored = True
                if self.__shouldYield__(currNode):
                    yield currNode
                stack.pop()
            else:
                stack.append(DepthFirstIteratorElement(child,currNode.depth + 1))
            

class PostOrderIterator(DepthFirstOrderIterator):
    def __init__(self, root: Node) -> None:
        super().__init__(root)
    def __shouldYield__(self, currNode: DepthFirstIteratorElement):
        return currNode.subtreeExplored
class PrePostOrderIterator(DepthFirstOrderIterator):
    def __init__(self, root: Node) -> None:
        super().__init__(root)
    def __shouldYield__(self, currNode: DepthFirstIteratorElement):
        return True