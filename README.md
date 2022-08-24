# tegraWATTS
**tegraWATTS** is a tegrastats parser that help provide layer by layer energy consumption in model inferences.

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
1. To run customized `tegrastats`, run `spinningclock.py`
2. Store starting/finishing timestamps in `inferlog.csv`
3. To get Energy Consumption, run `tegrawatts.py`. See `energylog.csv` for results.
