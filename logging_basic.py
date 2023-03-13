import logging

# Set the configuration attributes
logging.basicConfig(
    filename='./files/logger.log',
    format=('[%(levelname)s] %(asctime)s: %(message)s'),
    datefmt='%Y/%m/%d %H:%M:%S',  # same format as for time.strftime
    level=logging.DEBUG)  # log all messages up to DEBUG level

logging.info("---- Start logging ----")
user = "Kevin"
logging.debug("This is a Debug message")
logging.info("This is Info")
logging.warning("This is a Warning!")
logging.error("This is an Error!")
logging.info(f"This log is created by {user}")
