# wattsuppro_logger
WattsupPro logger, [based on work by Isaac Lino](https://github.com/isaaclino/wattsup).

# Introduction

This is a basic logging utility for wattsupPro, this is simplified and updated from [Wattsup](https://github.com/isaaclino/wattsup), to run with python3 and without a GUI for extended durations. 

Most of the documentation has been taken offline, the resources I managed to find are included in the resources folder as well as resources I created.
The main usecase of this repository will be for conducting experiments with the greenlab machines for the [S2 group](https://github.com/S2-group).

# Usage

To run the program in default configuration

```
python3 WattsupPro.py -l
```

## Parameters
To run with a custom timeout(default 10s)
```
python3 WattsupPro.py -l -t 500
```
To run with a custom output file(default log.out)
```
python3 WattsupPro.py -l -o sample.log
```

To specify port(default /dev/ttyUSB0)
```
python3 WattsupPro.py -l -p /dev/ttyUSB0  
```

To specify sample interval(default 1s)
```
python3 WattsupPro.py -l -s 10 
```

*note, these commands may need to be run with sudo privileges 

## Notes
In the case of green lab, be sure which serial port you will be logging from as it may affect the experiments being run by other users, refer [this diagram](https://github.com/GioDoesntKnowCode/wattsuppro_logger/blob/main/Diagram.png) for an overview.

Logged output will come in the format: Timestamp index, Watts, Voltage, Amps

#### Serial ports(Green lab):

| Machine       | Serial port   |
| ------------- | ------------- |
| GL2           | /dev/ttyUSB0  |
| GL3           | /dev/ttyUSB2  |
| GL4           | /dev/ttyUSB1  |

