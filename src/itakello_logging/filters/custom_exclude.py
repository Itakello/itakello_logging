import logging


class CustomExcludeFilter(logging.Filter):

    def __init__(self, modules: list[str]):
        super().__init__()
        self.modules = modules

    def filter(self, record: logging.LogRecord) -> bool:
        return record.name not in self.modules
