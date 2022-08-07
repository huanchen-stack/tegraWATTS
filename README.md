# tegraWATTS
**tegraWATTS** is a tegrastats parser that help provide layer by layer energy consumption in model inferences.

## Input Formats ##
### tegralog.txt ###
```
datetime tegrastats_log ... WATTS
```
### inferlog.csv ###
```
layername ts_start ts_finish
```
## Output Format ##
### energylog.csv ###
```
layername duration energy_consumption
```
