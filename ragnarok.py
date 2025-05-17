import nmap

def scan_hosts(network_range):
    scanner = nmap.PortScanner()

    print(f"[+] Scanning network: {network_range} with -sn")
    scanner.scan(hosts=network_range, arguments='-sn')

    print("\n[+] Live Hosts Found:")
    for host in scanner.all_hosts():
        print(f"    - {host} is UP")

if _name_ == "_main_":
    print("Basic Nmap Host Discovery Tool")
    target = input("Enter IP address or subnet (e.g. 192.168.1.0/24): ")
    scan_hosts(target)
