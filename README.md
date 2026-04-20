# Bluehound

A Bluetooth Low Energy (BLE) reconnaissance and anomaly detection framework with real-time visualization.

Originally built for BLE wardriving, now extended into a **dual-mode system for device discovery and environment analysis**.

---

## Features

### Sniffer Mode (Wardriving)

- Discovers nearby BLE devices in real-time  
- Persistent JSON database across sessions  
- RSSI-based distance estimation  
- Web-based radar visualization  
- Fast continuous scanning  

---

### Monitor Mode (Anomaly Detection Engine)

Analyzes BLE activity in real-time to detect abnormal behavior across both devices and the environment.

#### Device-Level Detection

- RSSI spike detection (signal instability)
- Missed scan cycles (intermittent presence)
- Time-based disappearance tracking

Devices are dynamically classified:
- `stable`
- `unstable`

---

#### Environment-Level Detection

- Unstable device ratio  
- Device count drop score  
- Real-time session analysis  

Detects conditions such as:
- BLE flooding  
- RF interference  
- Sudden signal disruption  
- Suspicious device behavior  

---

## Installation

### Install BlueZ (Linux Bluetooth Stack)

**Debian / Ubuntu**
```bash
sudo apt-get update && sudo apt-get install -y bluez
```

**Arch Linux**
```bash
sudo pacman -S bluez bluez-utils
sudo systemctl enable --now bluetooth
```

---

### Install Bluehound

```bash
git clone https://github.com/nsm-barii/bluehound.git
cd bluehound/src

python3 -m venv venv
source venv/bin/activate

pip install -r ../requirements.txt
```

---

## Usage

### Sniffer Mode
```bash
sudo venv/bin/python main.py -sniffer
```

### Monitor Mode
```bash
sudo venv/bin/python main.py -monitor
```

---

### Optional Flags

```bash
-save        # Save scan results
-s <IP>      # Send data to external server (ESP32 / LED system)
```

---

## How It Works

### Sniffer Mode

- Scans BLE advertisement packets  
- Extracts device metadata (MAC, vendor, RSSI, UUIDs)  
- Stores results persistently  
- Displays devices in a real-time web UI  

---

### Monitor Mode

- Tracks devices across scan cycles  
- Builds a live model of BLE activity  
- Uses weighted anomaly detection:

```text
RSSI instability + missed cycles + signal loss → unstable device
```

---

### Real-Time Metrics

- Total devices  
- Unstable devices  
- Unstable ratio (%)  
- Drop score  

Example:
```
Session Devices: 42
Unstable Devices: 8
Unstable Ratio: 19.04%
Drop Score: 0.27
```

---

## Project Structure

```bash
src/
├── main.py
├── scanner/
│   └── BLE_Sniffer.py
├── monitor/
│   └── Monitor_Bluetooth.py
├── web/
├── database/
│   └── database.json
```

---

## Use Cases

- BLE wardriving and mapping  
- IoT device discovery  
- RF environment monitoring  
- BLE anomaly detection  
- Early-stage BLE intrusion detection research  

---

## Roadmap

- BLE jamming detection  
- Device fingerprinting (behavior + vendor)  
- Multi-adapter support  
- ESP32 real-time alert integration  
- Data export / analytics pipeline  

---

## Requirements

- Linux (BlueZ required)  
- Python 3.7+  
- BLE-compatible adapter  

---

## Disclaimer

This tool is intended for **authorized security research and educational use only**.  
Do not scan or analyze devices without permission.

---

## Author

Built by  
https://github.com/nsm-barii
