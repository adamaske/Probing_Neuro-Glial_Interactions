import logging

logger = logging.getLogger("app")

def main():
    
    
    
    logging.basicConfig(level="DEBUG")
    logger.debug("deubug message")
    logger.info("info message")
    logger.warning("warning mesage")
    logger.critical("critical message")
    try:
        1/0
    except ZeroDivisionError:
        logger.exception("execepction mesage")
    
if __name__ == "__main__":
    main()