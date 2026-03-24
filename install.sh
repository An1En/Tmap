#!/bin/bash
# Tmap Global Installer by An1En

echo -e "\e[1;34m[*] Starting Tmap Installation...\e[0m"

# 1. Install system requirements (Nmap and Python pip)
echo -e "\e[1;33m[*] Installing dependencies (Nmap, Python3-pip)...\e[0m"
sudo apt-get update -y
sudo apt-get install nmap python3 python3-pip -y

# 2. Install Python dependencies
echo -e "\e[1;33m[*] Installing python-nmap...\e[0m"
pip3 install python-nmap --break-system-packages 2>/dev/null || pip3 install python-nmap

# 3. Make Tmap executable and move it to the system binaries
echo -e "\e[1;33m[*] Configuring system paths...\e[0m"
chmod +x Tmap.py
sudo cp Tmap.py /usr/local/bin/tmap-scan
sudo chmod +x /usr/local/bin/tmap-scan

echo -e "\e[1;32m[+] Tmap installed successfully!\e[0m"
echo -e "\e[1;32m[+] You can now run it from anywhere by typing: tmap\e[0m"
