import pyfiglet
import sys
import socket

def port_check():
    def get_target_ip():
        while True:
            ip = input("Enter the target IP address: ")
            try:
                socket.inet_aton(ip)
                return ip
            except socket.error:
                print("Invalid IP address format. Please enter a valid IP address.")
      
    banner = pyfiglet.figlet_format("port scanner")

    print("-"*80)
    print(banner)
    print("-"*80)

    # Get the target IP address from user input
    target = get_target_ip()

    print("Scanning IP:", target)

    try:
        for port in range(1, 65536):
            i = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = i.connect_ex((target, port))
            
            if result == 0:
                print("Port", port, "is open")
            else:
                print("Port", port, "is closed")
                  
            i.close()

    except KeyboardInterrupt:
        print("Keyboard Interrupted")
        sys.exit()

    except socket.gaierror:
        print("Cannot connect to hostname")
        sys.exit()

    except socket.error:
        print("Cannot connect")
        sys.exit()

# Call the function to execute the port scanning

