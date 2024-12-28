import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

logs_directory = os.path.join(os.getcwd(), "logs")

# Pehle logs directory banaye
os.makedirs(logs_directory, exist_ok=True)

# Phir log file ka path banaye
logs_path = os.path.join(logs_directory, LOG_FILE)

logging.basicConfig(
    filename=logs_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)