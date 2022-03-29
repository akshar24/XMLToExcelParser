from lib2to3.pytree import Base
from XMLRepresentations.XMLDataNode import XMLDataNode
from Configuration.XMLFileBasedConfigurationOptions import XMLFileBasedConfigurationOptions
from Readers.XMLFileReader import XMLFileReader
from Constants.XMLDataNodeConstants import ATTRIBUTE_LABEL
from Configuration.XMLFileReaderConfigurationOptions import XMLFileReaderConfigurationOptions
from DataStructures.AttributesCollection import AttributesCollection
from Configuration.XMLToExcelParserOutputOptions import XMLToExcelParserOutputOptions
from Iterators.DepthFirstOrderIterator import *
from Iterators.Iterator import BaseIterator
import xml.etree.ElementTree as et
path = "/Users/akshar/Desktop/Desktop - Akshar’s MacBook Pro/XMLToExcelParser"
filename  = "test.xml"
options = XMLFileBasedConfigurationOptions()
readeroptions = XMLFileReaderConfigurationOptions(options)
parseroptions = XMLToExcelParserOutputOptions(options)
reader = XMLFileReader(readeroptions)
node = reader.read()
it = PrePostOrderIterator(node)
current = None
for node in it:
    print(node.element.name)

