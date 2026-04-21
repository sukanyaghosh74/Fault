import time
from unstable_service import unstable_call
from logger import log

def retry_request(max_retries=3, delay=2):
    for attempt in range(1, max_retries + 1):
        try:
            log(f"Attempt {attempt}")
            return unstable_call()
        except Exception as e:
            log(f"Failure on attempt {attempt}: {str(e)}")
            time.sleep(delay * attempt)

    raise Exception("All retries failed")
