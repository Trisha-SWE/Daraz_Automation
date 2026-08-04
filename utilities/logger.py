import logging
import os


class LogGen:
    """
    Logger Utility Class
    Creates and returns a reusable logger instance.
    """

    LOG_FOLDER = "logs"
    LOG_FILE = "automation.log"

    @staticmethod
    def loggen():

        # Create logs folder if it doesn't exist
        if not os.path.exists(LogGen.LOG_FOLDER):
            os.makedirs(LogGen.LOG_FOLDER)

        log_path = os.path.join(
            LogGen.LOG_FOLDER,
            LogGen.LOG_FILE
        )

        logging.basicConfig(
            filename=log_path,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%d-%m-%Y %I:%M:%S %p",
            force=True
        )

        return logging.getLogger(__name__)