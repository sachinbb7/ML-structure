import logging
import os
from datetime import datetime

log_file = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'
log_path = os.path.join(os.getcwd(), "logs", log_file)

os.makedirs(os.path.dirname(log_path), exist_ok=True)

logs_file_path = log_path

logging.basicConfig(
    filename=logs_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



