from XMLRepresentations.XMLDataNode import XMLDataNode
from .XMLFileBasedConfigurationOptions import XMLFileBasedConfigurationOptions
from .ConfigurationOptions import ConfigurationOptions
from Utilities.Utils import Utils
from DataStructures.AttributesCollection import AttributesCollection

class TableConfigurationEntry: 
    def __init__(self, xmlPath: str = "", tableName: str = "") -> None:
        self.xmlPath = xmlPath
        self.tableName = tableName
    def __str__(self) -> str:  
        return "XmlPath: " + self.xmlPath + ", TableName: " + self.tableName

class XMLToExcelParserOutputOptions(ConfigurationOptions):
    def __init__(self, options: XMLFileBasedConfigurationOptions) -> None:
        super().__init__()
        self.options = options
        section = self.options.first(Utils.findName('parserOutputConfig'))
        self.tableConfigs = AttributesCollection()
        for tableConfiguration in section.filter(Utils.findName('table')):
            tableConfigEntry = TableConfigurationEntry()
            for subConfig in tableConfiguration.filter(lambda node: node['name'] in ['path', 'tablename']):
                if subConfig['name'] == 'path':
                    tableConfigEntry.xmlPath = subConfig.text
                elif subConfig['name'] == 'tablename':
                    tableConfigEntry.tableName = subConfig.text
            self.tableConfigs.add(tableConfigEntry.tableName, tableConfigEntry)




        

