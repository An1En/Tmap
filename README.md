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
git clone [https://github.com/YOUR_USERNAME/Tmap.git](https://github.com/YOUR_USERNAME/Tmap.git)

# 2. Navigate to the directory
cd Tmap

# 3. Execute the global installer
sudo ./install.sh
💻 Usage
Once installed, you can launch the interactive framework from anywhere in your terminal:

Bash
tmap-scan
CLI Arguments
If you prefer to skip the interactive menu, you can pass targets directly:

Bash
tmap-scan -t 192.168.1.1
tmap-scan --target scanme.nmap.org
👨‍💻 Author
An1En * GitHub: @YourUsername

<p align="center"><i>"Automate the boring stuff. Hack the rest."</i></p>


-----

### **3 Secrets to GitHub Aesthetics**

If you want to customize that template further, here are the three tricks used to make it look pro:

**1. HTML Centering (`<p align="center">`)**
Standard Markdown forces everything to the left side of the screen. By wrapping your titles, badges, and sub-menus in HTML center tags, you create a balanced, modern website look.

**2. Dynamic Badges (Shields.io)**
Those `img.shields.io` links at the top of the template automatically generate the clean little colored tags that say "Python" or "Linux". They instantly signal to other developers that the project is well-maintained.

**3. The Collapsible Section (For long logs)**
If you ever want to show a massive wall of code (like a full Tmap scan output) without cluttering the README, wrap it in a `details` tag. It creates a neat little dropdown arrow\!

````html
<details>
  <summary>Click to view full Deep Scan output</summary>
  
  ```text
  [+] Host: 192.168.1.1
  [*] Detailed Port Analysis:
  ...
</details>


Would you like me to show you how to record a GIF of your terminal running Tmap so yo
