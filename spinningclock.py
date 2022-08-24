import time
from datetime import datetime
import keyboard

import sys
import subprocess as sp

LOGFILE = 'tegralog.txt'
METHOD = 'w'


def read_tegrastats(interval=1):
    pts = sp.Popen(['tegrastats', '--interval', str(interval)], stdout=sp.PIPE)
    with open(LOGFILE, METHOD) as f:
        try:
            while True:
                print(datetime.now())
                if pts.poll() is not None:
                    continue
                out = pts.stdout
                if out is not None:
                    line = out.readline()
                    tegrastats_data = line.decode("utf-8")
                    f.write(f"{datetime.now().replace(microsecond=0)} {tegrastats_data}")
        finally:
            pts.kill()


read_tegrastats()

