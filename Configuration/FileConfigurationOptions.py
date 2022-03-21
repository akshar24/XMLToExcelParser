from .ConfigurationOptions import ConfigurationOptions
import os
class FileConfigurationOptions(ConfigurationOptions):
    def __init__(self, inputFilePath: str, inputFileName: str) -> None:
        super().__init__()
        self.inputFilePath = inputFilePath
        self.inputFileName = inputFileName
        self.path = os.path.join(self.inputFilePath, self.inputFileName)
