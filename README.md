# File Copy Detection Monitor

## Overview

The **File Copy Detection Monitor** is a Python-based security monitoring tool that tracks file activities within a specific directory. It detects when files are created, copied, moved, or modified and records these events with timestamps.

This project demonstrates how file monitoring can be used in **cybersecurity environments to detect unauthorized data copying or insider threats**.

## Features

* Monitors a specific folder in real time
* Detects file creation, movement, and copy actions
* Logs activity with timestamps
* Generates alerts when suspicious file activity occurs
* Lightweight and easy to run

## Technologies Used

* Python
* Watchdog Library
* Logging Module
* Visual Studio Code
* Git & GitHub

## Project Structure

FileCopyDetectionMonitor
│
├── monitor.py
├── monitored_folder
├── screenshots
│     └── output.png
├── file_monitor.log
└── README.md

## Installation

Install the required library:

pip install watchdog

## How to Run

Run the monitoring script using:

python monitor.py

The script will start monitoring the configured folder and log all file activities.

## Output

The program records file events such as:

CREATED – when a new file appears
MOVED/COPIED – when files are copied or moved
MODIFIED – when file contents are changed

![Program Output](screenshots/output.png)

## Use Case in Cybersecurity

This tool demonstrates how security teams can monitor file systems to detect **unauthorized file copying, insider threats, and suspicious activity**. It can be extended to trigger alerts or send notifications when sensitive files are accessed.

## Future Improvements

* Email or alert notification when files are copied
* Integration with SIEM tools
* Real-time dashboard for monitoring activity
* Detection of suspicious file patterns







