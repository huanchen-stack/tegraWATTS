import time
from datetime import datetime

with open("tegralog.txt", 'a') as f:
    for i in range(10):
        time.sleep(1)
        f.write(f"{datetime.now()}\n")
