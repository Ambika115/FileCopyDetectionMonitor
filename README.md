# File Copy Detection Monitor

A Python-based security monitoring tool that detects file copy, move, and access activity in a monitored directory.

## Features
- Detects file copy activity
- Logs file access events
- Records timestamp and file name
- Useful for detecting insider threats

## Technologies Used
- Python
- Watchdog library
- Logging module

## How to Run

1. Install dependencies
pip install watchdog

2. Run the script
python monitor.py

## Output
All activity is logged in:
file_activity.log
