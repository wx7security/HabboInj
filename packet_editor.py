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


## variables
packet_edit1 = input("[+] ENTER the packet to edit: ")
packet_edit2 = input("[+] edit the packet: ")

def edit_packet(packet):
    packet[packet_edit1] = packet_edit2
    return packet

## Threading

def thread_packet(packet):
    threading.Thread(target=handle_packet, args=(packet,)).start()
    threading.Thread(target=edit_packet, args=(packet,)).start()
    threading.Thread(target=save_packet_log, args=(packet,)).start()
    threading.main_thread(50).start()

def handle_packet(packet):
    print(packet.summary())
