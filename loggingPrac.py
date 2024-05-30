import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is for the Information")
logging.critical("This is for the Critical")

handler = logging.FileHandler('MyLogs.log')
handler.setLevel(logging.DEBUG)
logger = logging.getLogger("Don2")
logger.addHandler(handler)

logger.warning("I warn you")
logger.error("Ab tu dekh. Ab tu gya beta.")
