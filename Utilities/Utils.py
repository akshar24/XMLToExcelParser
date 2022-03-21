class Utils:
    @staticmethod
    def findName(value: str):
        return lambda node: node['name'] == value