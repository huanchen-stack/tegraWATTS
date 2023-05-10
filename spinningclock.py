import time
from datetime import datetime

import subprocess as sp

# logfile name is HARDCODED here: make changes if needed
LOGFILE = 'tegralog.txt'
METHOD = 'w'

device_name = 'jetson-' + input('jetson-')

def read_tegrastats(interval=1):
    """
    Run tegrastats and directs its output to a standard PIPE.
    The current code only take care of jetson-agx and jetson-nano 
    """
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

                    # the current code only take care of jetson-agx and jetson-nano 
                    if device_name == 'jetson-nano':
                        f.write(f"{datetime.now().strftime('%m-%d-%Y %H:%M:%S')} {tegrastats_data}")
                    elif device_name == 'jetson-agx':
                        f.write(f"{tegrastats_data}")
                    else:
                        assert False, f"Invalid device name: {device_name}.\nChoose from list ['jetson-agx, jetson-nano']"
        
        # simply terminate the tegrastats process when the current program is killed by user
        finally:
            pts.kill()


read_tegrastats()

