import xml.etree.ElementTree as et

from pydantic import CallableError
from DataStructures.AttributesCollection import AttributesCollection
from DataStructures.BaseCollection import Collection
from DataStructures.Group import Groups, Group
from DataStructures.ChildrenCollection import ChildrenCollection
from Constants import XMLDataNodeConstants
from .BaseNode import Node
from DataStructures.LinearCollection import LinearCollection
from collections import deque
class XMLDataNode(Node):
    def __init__(self, xmlElement: et.Element = None, columnName: str = None):
        super().__init__(xmlElement.tag if xmlElement is not None else "")
        
        self.xmlElement: et.Element = xmlElement
        self.children = ChildrenCollection()
        self.attributes: AttributesCollection = AttributesCollection()
        self.groups: Groups = Groups()
        self.text = self.xmlElement.text if self.xmlElement is not None else ""
        self.columnName = columnName
        self.__addToGroups(self)
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, value):
        self._text = value 
    @property
    def columnName(self):
        return self._columnName
    @columnName.setter
    def columnName(self, columnName):
        self._columnName = columnName
        self.__extractAttributes()

    def __extractAttributes(self):
        if not self.columnName: return
        if self.xmlElement is None: return
        
        if XMLDataNodeConstants.ATTRIBUTE_LABEL in self.groups:
            self.groups[XMLDataNodeConstants.ATTRIBUTE_LABEL].clear()
        for attributeName, attributeValue in self.xmlElement.attrib.items():
            
            attributeNode = XMLDataNode(columnName=self.columnName + XMLDataNodeConstants.PATH_SEP + XMLDataNodeConstants.ATTRIBUTE_LABEL + attributeName)
            attributeNode.name = XMLDataNodeConstants.ATTRIBUTE_LABEL
            attributeNode._text = attributeValue
            self.__addToGroups(attributeNode)
    def add(self, child: Node):
        super().add(child)
        if self.columnName:
            child.columnName = self.columnName + XMLDataNodeConstants.PATH_SEP + child.name
        self.__addToGroups(child)
    def __addToGroups(self, child):
        nodeTagOrName = child.name
        group: Group = None
        if nodeTagOrName not in self.groups:
            group = Group(nodeTagOrName)
            self.groups.add(nodeTagOrName, group)
        else:
            group = self.groups[nodeTagOrName]
        group.add(child)
    def __getitem__(self, index):
        if isinstance(index, int):
            return self.children[index]
        elif self.xmlElement is not None and isinstance(index, str):
            return self.xmlElement.attrib.get(index, None)
        return None
    def __getattr__(self, name: str):
        return self.__getitem__(name)
    def __call__(self, name: str):
        return self.__getitem__(name)
    def __str__(self) -> str:
        return self.columnName
    def filter(self, condition) -> Collection:
        stack = deque()
        stack.append(self)
        matchedNodes = LinearCollection()
        while stack:
            node = stack.pop() 
            if condition(node): 
                matchedNodes.add(node)
            for child in reversed(node.children):
                stack.append(child)
        return matchedNodes
    def first(self, condition):
        stack = deque()
        stack.append(self)
        while stack:
            node = stack.pop() 
            if condition(node): 
                return node
            for child in reversed(node.children):
                stack.append(child)
        return None
   
    
        


