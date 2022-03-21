from XMLRepresentations.XMLDataNode import XMLDataNode
from Configuration.XMLFileBasedConfigurationOptions import XMLFileBasedConfigurationOptions
from Readers.XMLFileReader import XMLFileReader
from Constants.XMLDataNodeConstants import ATTRIBUTE_LABEL
from Configuration.XMLFileReaderConfigurationOptions import XMLFileReaderConfigurationOptions
from DataStructures.AttributesCollection import AttributesCollection
path = "/Users/akshar/Desktop/Desktop - Akshar’s MacBook Pro/XMLToExcelParser"
filename  = "test.xml"
options = XMLFileBasedConfigurationOptions()
readeroptions = XMLFileReaderConfigurationOptions(options)
print(readeroptions.path)