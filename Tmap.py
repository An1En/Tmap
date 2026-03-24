#!/usr/bin/env python3
"""
Project: Tmap
Author: An1En
Description: A professional Python CLI wrapper for Nmap reconnaissance.
"""

import nmap
import argparse
import sys

def banner():
    print("""
  _____                     
 |_   _| __ ___   __ _ _ __ 
   | || '_ ` _ \ / _` | '_ \ 
   | || | | | | | (_| | |_) |
   |_||_| |_| |_|\__,_| .__/ 
                      |_|    
    Author: An1En
    """)

def print_results(nm):
    """Parses initial Nmap scan results cleanly and returns open ports."""
    open_ports = []
    
    for host in nm.all_hosts():
        print(f"\n[+] Host: {host} ({nm[host].hostname()})")
        print(f"[+] State: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(f"\n[*] Protocol: {proto.upper()}")
            ports = nm[host][proto].keys()
            
            print(f"{'PORT':<10} {'STATE':<10} {'SERVICE':<15} {'VERSION INFO'}")
            print("-" * 65)
            
            for port in sorted(ports):
                state = nm[host][proto][port]['state']
                
                if state == 'open':
                    open_ports.append(port)
                    
                service = nm[host][proto][port].get('name', '')
                product = nm[host][proto][port].get('product', '')
                version = nm[host][proto][port].get('version', '')
                
                service_version = f"{product} {version}".strip()
                print(f"{port:<10} {state:<10} {service:<15} {service_version}")

    return open_ports

def print_deep_results(nm):
    """Parses and displays the extensive data from a Deep/Aggressive scan."""
    for host in nm.all_hosts():
        print(f"\n" + "="*50)
        print(f"[+] DEEP ENUMERATION REPORT: {host} ({nm[host].hostname()})")
        print("="*50)
        
        # 1. Display Operating System Detection
        if 'osmatch' in nm[host] and len(nm[host]['osmatch']) > 0:
            print("\n[*] Operating System Guesses:")
            for os in nm[host]['osmatch']:
                print(f"    |__ {os['name']} (Confidence: {os['accuracy']}%)")
        
        # 2. Display Detailed Port and Script Info
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            print(f"\n[*] Detailed Port Analysis ({proto.upper()}):")
            
            for port in sorted(ports):
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port].get('name', '')
                product = nm[host][proto][port].get('product', '')
                version = nm[host][proto][port].get('version', '')
                extrainfo = nm[host][proto][port].get('extrainfo', '')
                
                print(f"\n    >> [Port {port}] - {state.upper()} - {service} {product} {version} {extrainfo}".strip())
                
                # Unleash the full Nmap Scripting Engine (NSE) output
                if 'script' in nm[host][proto][port]:
                    print("        |__ [Vulnerability/Enumeration Scripts]:")
                    for script_name, script_out in nm[host][proto][port]['script'].items():
                        print(f"            --> {script_name}:")
                        # Print every line of the script output nicely indented
                        for line in script_out.split('\n'):
                            if line.strip():
                                print(f"                {line.strip()}")
        
        # 3. Display Host-Level Scripts (e.g., general SMB or DNS discoveries)
        if 'hostscript' in nm[host]:
            print("\n[*] Host-Level Script Discoveries:")
            for script in nm[host]['hostscript']:
                print(f"    |__ {script['id']}:")
                for line in script['output'].split('\n'):
                    if line.strip():
                        print(f"        {line.strip()}")

def run_deep_scan(target, ports):
    """Runs an intensive scan specifically targeted at identified open ports."""
    nm = nmap.PortScanner()
    port_string = ','.join(map(str, ports))
    
    print(f"\n[*] INITIATING DEEP ENUMERATION ON PORTS: {port_string}")
    print(f"[*] This may take a minute. Firing heavily weaponized probes...")
    
    try:
        nm.scan(hosts=target, ports=port_string, arguments='-A -sC -sV -T4')
        # Use our new dedicated deep parsing engine!
        print_deep_results(nm)
    except Exception as e:
        print(f"\n[-] Deep Scan Error: {e}")

def run_scan(target, scan_type):
    nm = nmap.PortScanner()
    print(f"\n[*] Target locked: {target}")
    print(f"[*] Initiating {scan_type.upper()} scan...")

    if scan_type == 'quick':
        args = '-F -T4'
    elif scan_type == 'stealth':
        args = '-sS -T3'
    elif scan_type == 'service':
        args = '-sV -T4'
    elif scan_type == 'aggressive':
        args = '-A -T4'
    else:
        return

    try:
        nm.scan(hosts=target, arguments=args)
        open_ports = print_results(nm)
        
        if open_ports:
            print(f"\n[*] Discovered {len(open_ports)} open ports.")
            choice = input("[?] Would you like to run a Deep Scan on these specific ports? (y/n): ").strip().lower()
            if choice == 'y':
                run_deep_scan(target, open_ports)
            else:
                print("[*] Skipping deep enumeration.")
        else:
            print("\n[-] No open ports discovered to deep scan.")

    except nmap.PortScannerError as e:
        print(f"\n[-] Nmap Error: {e}")
        print("    Note: SYN ('stealth') and certain Aggressive scans require sudo privileges.")
    except Exception as e:
        print(f"\n[-] An unexpected error occurred: {e}")

def interactive_menu(target):
    while True:
        print("\n" + "="*30)
        print("      TMAP SCAN MODULES      ")
        print("="*30)
        print("1. Quick Scan        (-F -T4)")
        print("2. Stealth Scan      (-sS -T3) *requires sudo")
        print("3. Service Scan      (-sV -T4)")
        print("4. Aggressive Scan   (-A -T4)  *requires sudo")
        print("5. Exit Framework")
        print("="*30)
        
        choice = input("\n[?] Select a module (1-5): ").strip()
        
        if choice == '1':
            run_scan(target, 'quick')
        elif choice == '2':
            run_scan(target, 'stealth')
        elif choice == '3':
            run_scan(target, 'service')
        elif choice == '4':
            run_scan(target, 'aggressive')
        elif choice == '5':
            print("\n[*] Shutting down Tmap. Goodbye, An1En.\n")
            sys.exit(0)
        else:
            print("\n[-] Invalid selection.")

def main():
    banner()
    parser = argparse.ArgumentParser(description="Tmap - Python Nmap Wrapper by An1En")
    parser.add_argument("-t", "--target", help="Target IP or hostname")
    
    args = parser.parse_args()
    
    target = args.target
    if not target:
        target = input("[?] Enter target IP or hostname: ").strip()
        if not target:
            sys.exit(1)
            
    interactive_menu(target)

if __name__ == "__main__":
    main()
