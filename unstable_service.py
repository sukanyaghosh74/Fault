import random

def unstable_call():
    if random.randint(1, 3) == 1:
        raise Exception("Random failure occurred")
    return {"value": "Successful response"}
