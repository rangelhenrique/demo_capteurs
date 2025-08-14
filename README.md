# Sensor Data Logger – Documentation

## Overview
This program simulates readings from multiple types of sensors (battery level, temperature, and two-dimensional position) and stores them in a CSV file while optionally displaying logs in the terminal.

It is designed for testing, logging, and continuous improvement workflows (CI).

## Features
- Generates random sensor data:
  - Battery level (12% to 100%)
  - Temperature (30.0°C to 60.0°C)
  - Position X/Y (0.0 to 60.0)
- Saves data in CSV format with a predefined header.
- Configurable logging (silent, INFO, DEBUG).
- Keeps the CSV file open during the loop to reduce I/O overhead.
- Command-line interface (CLI) to control log verbosity.

## Requirements
- Python >= 3.9
- Standard libraries only:
  - `csv`
  - `random`
  - `time`
  - `datetime`
  - `logging`
  - `argparse`

## File Structure
```
robot_data_logger_cli.py   # Main program with CLI
donnees.csv                # Output CSV file
```

## Usage
Run the script from the terminal:

**Default mode (silent):**
```bash
python robot_data_logger_cli.py
```

**Log INFO level:**
```bash
python robot_data_logger_cli.py --info
```

**Log DEBUG level:**
```bash
python robot_data_logger_cli.py --debug
```

## CSV Output Example
```csv
heure,batterie(%),temperature(degrees),position_X,position_Y
12:00:01 14-08-2025,98,35.6,12.4,45.7
12:00:06 14-08-2025,54,41.2,33.8,21.9
```

## Function Reference

### `gen_donnees()`
Generates a list containing:
1. **heure**: current time in `HH:MM:SS DD-MM-YYYY` format.
2. **batterie**: random integer between 12 and 100.
3. **temperature**: random float between 30.0 and 60.0 (1 decimal place).
4. **position_X**: random float between 0.0 and 60.0 (1 decimal place).
5. **position_Y**: random float between 0.0 and 60.0 (1 decimal place).

## Logging
- **INFO** level displays measurement lines.
- **DEBUG** level also shows generated raw data and extra version messages.
- By default, logging is **silent** (WARNING level).

## Version History
- **2.1.1**: Initial GitHub test version.
- **2.1.2**: Added CLI logging controls and kept file open for performance.
