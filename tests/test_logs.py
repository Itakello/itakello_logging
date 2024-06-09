import unittest

from itakello_logging.core import ItakelloLogging

logger = ItakelloLogging().get_logger(__name__)


class TestLogging(unittest.TestCase):
    def test_func_with_args(self) -> None:
        logger.debug("Test debug message from test.py")
        logger.info("Test info message from test.py")
        logger.instruction(
            [
                "Test instruction 1 message from test.py",
                "Test instruction 2 message from test.py",
                "Test instruction 3 message from test.py",
            ]
        )
        logger.confirmation("Test confirmation message from test.py")
        logger.warning("Test warning message from test.py")
        logger.error("Test error message from test.py")
        logger.critical("Test critical message from test.py")

    def test_func_with_exception(self) -> None:
        try:
            raise ValueError("This is a test error")
        except ValueError as e:
            logger.error(str(e))

    def test_func_with_critical_exception(self) -> None:
        try:
            raise Exception("This is a test critical error")
        except Exception as e:
            logger.critical(str(e))


if __name__ == "__main__":
    unittest.main()
