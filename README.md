# Forensic Analysis Tool

This repository contains tools for performing **digital forensics** and **network forensics**.

## Features
### Digital Forensics (`digital_forensics.py`)
- Extract file metadata (size, creation date, modification date).
- Generate file hashes (MD5, SHA-256, etc.) to verify file integrity.

### Network Forensics (`network_forensics.py`)
- Analyze PCAP files to provide basic statistics.
- Display protocol distribution in captured network traffic.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/forensic-analysis.git
    cd forensic-analysis
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Requirements
- Python 3.x
- `scapy` for network analysis (`network_forensics.py`)

