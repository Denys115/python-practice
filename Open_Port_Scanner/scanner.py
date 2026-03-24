import socket
import sys
from datetime import datetime

def check(host:str, port:int):
    IPV4:int = socket.AF_INET
    TCP:int = socket.SOCK_STREAM
    Address:tuple[str, int] = (host, port)
    
    with socket.socket(IPV4, TCP) as s:
        s.settimeout(1)
        result:int = s.connect_ex(Address)
        if result == 0:
            return f"Port {port} is OPEN"
        return None

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 scanner.py <host> <start_port> <end_port>")
        sys.exit(1)

    host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    print("-" * 50)
    print(f"Scanning Target: {host}")
    print(f"Scanning started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    try:
        print(f"Cautam porturi deschise...\n")
        for port in range(start_port, end_port + 1):
            sys.stdout.write(f"\r[#] Verificam portul: {port}...")
            sys.stdout.flush()

            status = check(host, port)
            if status:
                print(f"\n[+] {status} !!!") 
            
    except KeyboardInterrupt:
        print("\n[!] Scanare oprita de utilizator.")
        sys.exit()
    except socket.gaierror:
        print("\n[!] Hostname-ul nu a putut fi rezolvat.")
        sys.exit()
    except socket.error:
        print("\n[!] Nu s-a putut stabili conexiunea cu serverul.")
        sys.exit()

    print(f"\n" + "-" * 50) # \n adauga un rand liber la final
    print(f"Scan completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
