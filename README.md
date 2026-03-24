<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-red.svg" alt="Version">
  <img src="https://img.shields.io/badge/Language-Python_3-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Linux-lightgrey.svg" alt="Linux">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

<h1 align="center">
  <br>
  T M A P
  <br>
</h1>

<h4 align="center">A professional, automated reconnaissance and port-scanning framework.</h4>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#author">Author</a>
</p>

---

> **Note:** Tmap is built for authorized penetration testing and security research only. Do not scan networks you do not own or have explicit permission to test.

## 🎯 Overview
Tmap streamlines the network discovery phase by casting a wide, high-speed net for open ports, and automatically piping those targets into an aggressive deep-enumeration engine. It replaces tedious manual typing with a sleek, interactive terminal interface.

<br>

## ✨ Features
* **Interactive UI:** Navigate modules effortlessly without memorizing complex Nmap flags.
* **Smart Parsing:** Automatically isolates open ports for targeted deep scans.
* **Deep Enumeration:** Extracts OS guesses, vulnerability scripts (NSE), and SSH keys.
* **Zero Dependencies:** Runs natively via a single bash installer.

<br>

## 🚀 Installation

Tmap is designed for global deployment on Debian/Ubuntu/Kali systems. 

```bash
# 1. Clone the repository
git clone https://github.com/An1En/Tmap.git

# 2. Navigate to the directory
cd Tmap

# 3. Execute the global installer
chmod +x install.sh
sudo ./install.sh
```
## 💻 Usage

Tmap is designed to be frictionless. You do not need to memorize complex Nmap flags or syntax. Simply launch the framework from anywhere in your terminal and let the interactive menu guide your reconnaissance.

```bash
# Launch the interactive framework
tmap
```
## ⚙️ CLI Arguments

For advanced users and automated pipelines, Tmap supports direct command-line arguments to completely bypass the interactive menus.

| Argument | Short Flag | Description | Example |
| :--- | :--- | :--- | :--- |
| `--target` | `-t` | Locks onto the target IP or hostname. | `-t 192.168.1.1` |
| `--scan`   | `-s` | Skips the menu and runs the specified scan (`quick`, `stealth`, `service`, `aggressive`). | `-s aggressive` |

**Example Automation Workflow:**
```bash
# Instantly launch an aggressive scan against a target without any prompts
tmap-scan -t 10.10.10.5 -s aggressive
```
## 👨‍💻 Author

**An1En** * 🛡️ **Focus:** Cybersecurity, Penetration Testing, and Automation
* 🐙 **GitHub:** [@An1En](https://github.com/An1En)

> *"Automate the reconnaissance. Weaponize the data."*

