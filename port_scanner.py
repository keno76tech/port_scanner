import socket, sys
from datetime import datetime
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor

symbol_true = colored(str('+'), 'green')
sybmol_false = colored(str('-'), 'red')
symbol_command = colored(str('<>'), 'magenta')
symbol_help = colored(str('?'), 'yellow')

if len(sys.argv) >= 4:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
else:
    print(f'[{sybmol_false}] Invalid number of arguments. Please provide 3 arguments \n[{symbol_help}] (1. IP address [str], 2. starting port [int], 3. ending port [int])\n')
    sys.exit()

def scan_port(host, port):

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.10)  # Ustawienie timeoutu dla próby połączenia
            result = s.connect_ex((host, port))
            if result == 0:
                symbol_true = colored(str('+'), 'green')
                port = colored(str(port), 'green')
                host = colored(str(host), 'green')
                time = colored(str(datetime.now()), 'green')

                print(f"[{symbol_true}] Port {port} on host {host} is open. [{time}]")
    except:
        pass

def port_scanner(host, start_port, end_port, max_threads=10):

    ascii = r'''______               _     _____                                        
| ___ \             | |   /  ___|                                       
| |_/ /  ___   _ __ | |_  \ `--.   ___   __ _  _ __   _ __    ___  _ __ 
|  __/  / _ \ | '__|| __|  `--. \ / __| / _` || '_ \ | '_ \  / _ \| '__|
| |    | (_) || |   | |_  /\__/ /| (__ | (_| || | | || | | ||  __/| |   
\_|     \___/ |_|    \__| \____/  \___| \__,_||_| |_||_| |_| \___||_| '''

    ascii = colored(str(ascii), 'magenta')
    print(f'\n{ascii}')

    print(f"\n[{symbol_command}] Initiating scanning of host {host} within the port range from {start_port} to {end_port}: ")

    with ThreadPoolExecutor(max_threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, host, port)

if __name__ == "__main__":
    target_host = arg1  # Możesz zmienić ten adres IP na dowolny host, który chcesz zeskanować
    try:
        start_port = int(arg2)
        end_port = int(arg3)  # Możesz zmienić zakres portów w zależności od potrzeb
    except:
        print(f'[{sybmol_false}] Argument 2 and 3 must be numbers.\n')
        sys.exit()
        
    port_scanner(target_host, start_port, end_port)