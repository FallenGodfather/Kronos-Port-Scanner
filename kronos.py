import socket
import sys
from datetime import datetime

# TODO: Maybe add threading later for faster scans?

def show_banner():
    """
    Displays the tool banner
    """
    # I spent way too much time making this look cool lol
    print("=" * 70)
    print("                    Kronos (Port Scanner)")
    print("                    Port Scanner v1.0")
    print("                   Created by Hassan Ali")
    print("                   github.com/FallenGodfather")
    print("=" * 70)
    print()


def check_port(ip, port):
    """
    Check if a specific port is open
    Returns True if open, False if closed
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    
    # Try to connect
    result = s.connect_ex((ip, port))
    s.close()
    return result == 0


def get_service_name(port):
    """
    Try to get the common service name for a port
    Just added the most common ones I know
    """
    common_ports = {
        21: "FTP",
        22: "SSH", 
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        445: "SMB",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        5900: "VNC",
        8080: "HTTP-Proxy",
        8443: "HTTPS-Alt"
    }
    
    return common_ports.get(port, "Unknown")


def scan_target(target, port_range):
    """
    Main scanning function
    """
    start_port, end_port = port_range
    
    print(f"[*] Starting scan on {target}")
    print(f"[*] Port range: {start_port}-{end_port}")
    print(f"[*] Time: {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 70)
    
    # Resolve hostname to IP
    try:
        target_ip = socket.gethostbyname(target)
        if target != target_ip:
            print(f"[+] Resolved {target} to {target_ip}")
            print()
    except socket.gaierror:
        print(f"[!] Error: Could not resolve hostname '{target}'")
        print("[!] Please check the address and try again")
        return
    
    open_ports = []
    
    try:
        # Scan each port
        for port in range(start_port, end_port + 1):
            try:
                if check_port(target_ip, port):
                    service = get_service_name(port)
                    print(f"[+] Port {port:5d} - OPEN  ({service})")
                    open_ports.append(port)
            except KeyboardInterrupt:
                print("\n[!] Scan cancelled by user")
                sys.exit(0)
            except socket.error:
                pass  # Port is closed or filtered
                
    except Exception as e:
        print(f"[!] Error during scan: {e}")
        return
    
    # Show results
    print()
    print("-" * 70)
    print(f"[*] Scan complete at {datetime.now().strftime('%H:%M:%S')}")
    print(f"[*] Found {len(open_ports)} open port(s)")
    
    if open_ports:
        print(f"[*] Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("[*] No open ports found in this range")
    print()


def main():
    """
    Main program logic
    """
    show_banner()
    
    # Get user input
    print("[?] Enter target IP or hostname")
    target = input(">>> ").strip()
    
    # Use localhost if nothing entered
    if not target:
        target = "127.0.0.1"
        print(f"[*] Using default target: {target}")
    
    print()
    print("[?] Enter starting port (default: 1)")
    start_input = input(">>> ").strip()
    start = int(start_input) if start_input else 1
    
    print("[?] Enter ending port (default: 1000)")
    end_input = input(">>> ").strip()
    end = int(end_input) if end_input else 1000
    
    # Quick validation
    if start < 1 or end > 65535 or start > end:
        print("[!] Invalid port range! Ports must be between 1-65535")
        print("[!] Start port must be less than end port")
        return
    
    print()
    
    # Run the scan
    scan_target(target, (start, end))
    
    print("[*] Thanks for using Kronos!")
    print("[*] Remember: Only scan systems you have permission to test")


if __name__ == "__main__":
    # Entry point
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user. Exiting...")
        sys.exit(0)