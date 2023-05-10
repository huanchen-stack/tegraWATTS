# tegraWATTS
**tegraWATTS** is a tegrastats parser that help provide layer by layer energy consumption in model inferences.
(The current tegraWATTS are tested only on single layer inferences. The code only takes care of jetson-nano and jetson-agx families.)

## Formats ##
### Input Formats ###
#### tegralog.txt ####
```
datetime tegrastats_log...WATTS
```
#### inferlog.csv ####
```
layername,ts_start,ts_finish
```
### Output Format ###
#### energylog.csv ####
```
layername,duration,energy_consumption
```
## How to Use ##
1. To run customized `tegrastats` (with auto datetime insertion (for ***jetson-nano***)), run `spinningclock.py`
2. Run model inference in another terminal window; store the starting/finishing timestamps in `inferlog.csv`
4. To get Energy Consumption, run `tegrawatts.py`; see `energylog.csv` for results.
