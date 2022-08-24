import time
from datetime import datetime
import keyboard

import sys
import subprocess as sp

LOGFILE = 'tegralog.txt'
METHOD = 'w'

device_name = 'jetson-' + input('jetson-')

def read_tegrastats(interval=1):
    pts = sp.Popen(['tegrastats', '--interval', str(interval)], stdout=sp.PIPE)
    with open(LOGFILE, METHOD) as f:
        try:
            while True:
                print(datetime.now(), time.time())
                if pts.poll() is not None:
                    continue
                out = pts.stdout
                if out is not None:
                    line = out.readline()
                    tegrastats_data = line.decode("utf-8")
                    if device_name == 'jetson-nano':
                        f.write(f"{datetime.now().strftime('%m-%d-%Y %H:%M:%S')} {tegrastats_data}")
                    elif device_name == 'jetson-agx':
                        f.write(f"{tegrastats_data}")
                    else:
                        assert False, f"Invalid device name: {device_name}.\nChoose from list ['jetson-agx, jetson-nano']"
        finally:
            pts.kill()


read_tegrastats()

