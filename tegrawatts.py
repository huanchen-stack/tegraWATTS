import re
import time
import csv
from datetime import datetime

WATT_RE = re.compile(r'\b(\w+) ([0-9.]+)(\w?)W?\/([0-9.]+)(\w?)W?\b')

##################################################
################## FILE FORMATS ##################
##################################################

##################################################
# TEGRALOG.TXT                                   #
# DATETIME TEGRASTATS_LOG...WATTS                #
##################################################

##################################################
# INFERLOG.CSV                                   #
# LAYERNAME TS_START TS_FINISH                   #
##################################################

##################################################
# ENERGYLOG.CSV                                  #
# LAYERNAME DURATION ENERGY_CONSUMPTION          #
##################################################

class TegraWATTS(object):

    def __init__(self, 
            fn_tegralog="tegralog.txt", 
            fn_inferlog="inferlog.csv",
            fn_energylog="energylog.csv"
        ):
        super().__init__()
        
        self.fn_tegralog = fn_tegralog
        self.fn_inferlog = fn_inferlog
        self.fn_energylog = fn_energylog
        
        self.powerlog = {}

    def parse(self, filename="tegralog.txt"):
        f_log = open(filename, 'r')

        for log in f_log:
            time = datetime.strptime(log[:19], "%m-%d-%Y %H:%M:%S")
            if time not in self.powerlog:
                self.powerlog[time] = {}
            
            watts = {
                str(name): {
                    'cur': int(cur), 
                    'avg': int(avg)
                } for name, cur, _, avg, _ in re.findall(WATT_RE, log)
            }
            cur_agg = 0
            for _, wattsdict in watts.items():
                cur_agg += wattsdict['cur']
            watts['cur_agg'] = cur_agg

            self.powerlog[time][len(self.powerlog[time])] = watts

        f_log.close()

        dt_list = list(self.powerlog.keys())
        dt_list.sort()

        self.powerlog.pop(dt_list[0])
        self.powerlog.pop(dt_list[-1])
    
    def print_powerlog(self, head=True):
        i = 0
        for dt, wattsdictdict in self.powerlog.items():
            print(dt)
            for itr, wattsdict in wattsdictdict.items():
                if i == 5 and head:
                    return
                print(f"\t{itr}")
                for name, watts in wattsdict.items():
                    print(f"\t\t{name:6} | {watts}")
                i += 1

    def get_cur_agg(self, ts):
        dt = datetime.fromtimestamp(ts // 1)

        assert dt in self.powerlog, f"Inference timestamp {dt} not profiled by tegrastats."
        entry = ts % 1 * len(self.powerlog[dt]) // 1
        return self.powerlog[dt][entry]['cur_agg']


    def align(self):

        f_inferlog = open(self.fn_inferlog, 'r')
        f_energylog = open(self.fn_energylog, 'w')

        reader = csv.reader(f_inferlog)
        for layername, ts_start, ts_finish in reader:
            ts_start = float(ts_start)
            ts_finish = float(ts_finish)
            cur_agg_start = self.get_cur_agg(ts_start)
            cur_agg_finish = self.get_cur_agg(ts_finish)
            power_avg = (cur_agg_start + cur_agg_finish) / 2
            energy = power_avg * (ts_finish - ts_start)
            f_energylog.write(f"{layername},{ts_finish-ts_start:.6f},{energy:.4f}\n")
        
        f_inferlog.close()
        f_energylog.close()

    def get_WATTS(self, verbose=False):
        self.parse()
        if verbose:
            self.print_powerlog()
            for dt, wattsdictdict in tegraWATTS.powerlog.items():
                print(f"{dt} ({dt.timestamp()}) | {len(wattsdictdict)}")
        self.align()



tegraWATTS = TegraWATTS()
tegraWATTS.get_WATTS()