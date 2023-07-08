import logging
import time
from datetime import datetime, timedelta
# from battery_logs import execute_battery_logs

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('run_daily.log'),  # Specify the log file path
        logging.StreamHandler()
    ]
)

# Set up a scheduled task to execute battery_logs.py at specific times
schedule_times = ['09:00:00', '12:00:00', '15:00:00', '18:00:00', '21:00:00', '00:00:00', '02:00:00']

while True:
    current_time = datetime.now().strftime('%H:%M:%S')

    if current_time in schedule_times:
        logging.info('Executing battery_logs.py...')
        # execute_battery_logs()  # Call the function to execute battery_logs.py

    # Sleep for 1 minute before checking the time again
    time.sleep(60)