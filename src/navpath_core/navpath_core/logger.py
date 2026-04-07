from loguru import logger
import sys

def init_logging():
    logger.remove()
    logger.add(sys.stdout, format="<green>{time}</green> | <level>{level}</level> | {message}")
    logger.add("logs/system.log", rotation="1 day")
