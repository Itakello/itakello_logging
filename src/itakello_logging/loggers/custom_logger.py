import logging


class CustomLogger(logging.Logger):
    CONFIRMATION_LEVEL = 25
    INSTRUCTION_LEVEL = 24

    def __init__(self, name: str, level: int = logging.NOTSET) -> None:
        super().__init__(name, level)
        logging.addLevelName(self.CONFIRMATION_LEVEL, "CONFIRMATION")
        logging.addLevelName(self.INSTRUCTION_LEVEL, "INSTRUCTION")

    def confirmation(self, message: str, *args, **kwargs) -> None:
        if self.isEnabledFor(self.CONFIRMATION_LEVEL):
            self._log(self.CONFIRMATION_LEVEL, message, args, **kwargs)

    def instruction(self, instructions: list[str], *args, **kwargs) -> None:

        message = "\n".join(
            [
                f"{index + 1}. {instruction}"
                for index, instruction in enumerate(instructions)
            ]
        )

        if self.isEnabledFor(self.INSTRUCTION_LEVEL):
            self._log(self.INSTRUCTION_LEVEL, message, args, **kwargs)
