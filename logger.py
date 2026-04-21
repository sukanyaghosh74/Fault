from datetime import datetime

LOG_FILE = "api.log"

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")
    print(message)
