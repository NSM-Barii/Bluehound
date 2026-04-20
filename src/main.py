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
    parser.add_argument("-sniffer", action="store_true", help="Sniffer Mode: Scan and log nearby BLE devices (wardriving / reconnaissance)")
    parser.add_argument("-monitor", action="store_true", help="Monitor Mode: Analyze BLE environment for anomalies (unstable devices, signal drops, interference)")
    parser.add_argument("-save", action="store_true", help="BLE Wardriivng with command output")
    parser.add_argument("-s", help="Server IP for led lights")



    args = parser.parse_args()
    Variables.sniffer = args.sniffer
    Variables.monitor = args.monitor
    Variables.server_ip = args.s
    Variables.file_saving = args.save


    #console.print(f"[*] Mode: BLE Wardriving  -  Server IP: {Variables.server_ip}")
    
    
    BLE_Sniffer.main()
    Monitor_Bluetooth.main()



        






