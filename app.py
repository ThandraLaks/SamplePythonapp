import logging

logging.basicConfig(filename="app.log", level=logging.INFO)
logging.info("Application started")
logging.error("Database connection failed")
logging.warning("Low memory warning")
logging.info("Application stopped")
