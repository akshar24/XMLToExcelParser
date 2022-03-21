from .BaseReader import Reader
from Configuration.FileConfigurationOptions import FileConfigurationOptions
from XMLRepresentations.XMLDataNode import XMLDataNode
from DataStructures.BaseCollection import Collection
import xml.etree.ElementTree as et
from collections import deque

class XMLFileReader(Reader):
    def __init__(self, options: FileConfigurationOptions) -> None:
        super().__init__(options)
        self.options = options

    def read(self,  collect: Collection = None) -> XMLDataNode:
        xmlTree = et.parse(self.options.path)
        xmlRoot = xmlTree.getroot()
        convertedRoot = XMLDataNode(xmlRoot, xmlRoot.tag)
        if collect is not None: collect.add(xmlRoot, convertedRoot)
        queue = deque([convertedRoot])
        while queue:
            convertedNode = queue.popleft()
            for child in convertedNode.xmlElement:
                convertedChildNode = XMLDataNode(child)
                if collect is not None: collect.add(child, convertedChildNode)
                convertedNode.add(convertedChildNode)
                queue.append(convertedChildNode)
        return convertedRoot

