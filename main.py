import threading
import sys
from scapy.all import *


## Banner
print('''
.__          ___.  ___.          .___            __         ____ 
|  |__ _____ \_ |__\_ |__   ____ |   | ____     |__| ___  _/_   |
|  |  \\__  \ | __ \| __ \ /  _ \|   |/    \    |  | \  \/ /|   |
|   Y  \/ __ \| \_\ \ \_\ (  <_> )   |   |  \   |  |  \   / |   |
|___|  (____  /___  /___  /\____/|___|___|  /\__|  |   \_/  |___|
     \/     \/    \/    \/                \/\______|             
>--------------------------------------------->
Version 1.0
                              C0d3d by 303/g0d
┌─────────────────────────────────────────────┐
│        Tos: Only for Habbo origins !    │
├─────────────────────────────────────────────┤
│                 New stuff:                  │
│          [+] Added Packet Handler      │
│          [+] Packet Edition           │
│          [+] Windows Executable         │
├─────────────────────────────────────────────┤
│ twitter: twitter.com/g0dkorp │
└─────────────────────────────────────────────┘''')

def handle_packet(packet):
    print(packet.summary())
    save_packet_log(packet)

def packet_sniffer():
    print("[+] Connecting to the hotel...")
    sniff(prn=handle_packet, iface='en0', filter='tcp')

def start_sniffer():
    print("[+] Starting Sniffer. Please connect to the hotel...")
    sniff(prn=handle_packet, iface='en0', filter='tcp')

def stop_sniffer():
    print("[+] Stopping Sniffer.")
    sys.exit(0)

def save_packet_log(packet):
    with open("packet_logs.txt", "a") as log_file:
        log_file.write(f"{packet.summary()}\n")

def threading_logger():
    threading.Thread(target=stop_sniffer).start()
    threading.Thread(target=save_packet_log, args=(packet,)).start()
    threading.Thread(target=start_sniffer).start()

# Call the functions
threading_logger()
print("[+] Threads started !")
