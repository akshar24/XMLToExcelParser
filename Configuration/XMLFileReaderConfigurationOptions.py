from XMLRepresentations.XMLDataNode import XMLDataNode
from .FileConfigurationOptions import FileConfigurationOptions
from .XMLFileBasedConfigurationOptions import XMLFileBasedConfigurationOptions
class XMLFileReaderConfigurationOptions(FileConfigurationOptions):
    def __init__(self, options: XMLFileBasedConfigurationOptions) -> None:
        self.options = options
        findName= lambda value : lambda node: node['name'] == value
        section = self.options.first(findName("xmltoexcel")).first(findName("inputFileInformation"))
        matchedConfigs = section.filter(lambda node: node['name'] in ["inputFilePath", "inputFileName"])
        inputFilePathConfig = next(filter(lambda config: config['name'] == "inputFilePath", matchedConfigs), None)
        if not inputFilePathConfig:
            super().__init__(self.options.first(findName("workingDir")).text, next(filter(lambda config: config['name'] == "inputFileName", matchedConfigs)).text)
        else:
            super().__init__(inputFilePathConfig.text, next(filter(lambda config: config['name'] == "inputFileName", matchedConfigs)).text)
