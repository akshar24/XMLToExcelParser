from Configuration.ConfigurationOptions import ConfigurationOptions
from XMLRepresentations.BaseNode import Node
class Reader:
    def __init__(self, options: ConfigurationOptions) -> None:
        self.options = options
    def read(self, *args, **kwargs) -> Node:
        pass