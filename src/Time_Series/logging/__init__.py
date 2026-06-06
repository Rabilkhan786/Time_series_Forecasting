import os
import sys
import logging

log_dir = "Logs"
os.makedirs(log_dir, exist_ok=True)

log_filepath = os.path.join(log_dir, "continous_logs.log")

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]",
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("TimeSeriesLogger")