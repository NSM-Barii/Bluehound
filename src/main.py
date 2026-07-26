# UNIVERSAL CODE STEMS FROM HERE



# UI IMPORTS
from rich.console import Console
console = Console()


# ETC IMPORTS
import argparse


# NSM MODULES
from nsm_vars import Variables
from nsm_ble import BLE_Sniffer
from nsm_monitor import Monitor_Bluetooth
from nsm_database import DataBase




class Main_Menu():
    """This class will gatekeep program wide logic"""


    parser = argparse.ArgumentParser(
        description="BLE Sniffing Framework"
    )


   # parser.add_argument("-h", help="Display help, usage info, and project banner")
    #parser.add_argument("--mode", choices=["sniffer", "monitor"], help="This will be used to choose the mode option")
    parser.add_argument("--sniffer", action="store_true", help="Sniffer Mode: Scan and log nearby BLE devices (wardriving / reconnaissance)")
    parser.add_argument("--monitor", action="store_true", help="Monitor Mode: Analyze BLE environment for anomalies (unstable devices, signal drops, interference)")
    parser.add_argument("--save", action="store_true", help="BLE Wardriivng with command output")
    parser.add_argument("-s", help="Server IP for led lights")
    parser.add_argument("--web", action="store_true", help="Launch live web dashboard (http://localhost:8000) showing active BLE devices")
    parser.add_argument("--window", type=float, default=5, help="Scan window in seconds: how long each scan listens for BLE advertisements")
    parser.add_argument("--interval", type=float, default=0, help="Seconds to wait between scans (0 = scan continuously)")



    args = parser.parse_args()
    Variables.sniffer = args.sniffer
    Variables.monitor = args.monitor
    Variables.server_ip = args.s
    Variables.file_saving = args.save
    Variables.web = args.web
    Variables.scan_window   = args.window
    Variables.scan_interval = args.interval


    #console.print(f"[*] Mode: BLE Wardriving  -  Server IP: {Variables.server_ip}")
    
    
    BLE_Sniffer.main()
    Monitor_Bluetooth.main()



        






