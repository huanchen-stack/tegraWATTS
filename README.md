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
1. start running tegrastats under the directory of this folder in one terminal
```
tegrastats --interval 1 --tegralog.txt
```
2. start running model inference under the directory of another folder in another terminal
```
python3 detect.py --inferlog inferlog.csv
```
3. parse tegralog.txt and align with inferlog.csv
```
python3 tegraWATTS.py
```
