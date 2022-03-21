from .FileConfigurationOptions import FileConfigurationOptions
from Readers.XMLFileReader import XMLFileReader
from XMLRepresentations.XMLDataNode import XMLDataNode
from DataStructures.BaseCollection import Collection
class XMLFileBasedConfigurationOptions(FileConfigurationOptions):

   def __init__(self, inputFilePath: str = ".", inputFileName: str = "parserconfig.xml") -> None:
       super().__init__(inputFilePath, inputFileName)
       self.options: XMLDataNode = XMLFileReader(self).read()
   def first(self, condition) -> XMLDataNode:
        return self.options.first(condition)
   def filter(self, condition) -> Collection:
       return  self.options.filter(condition)
