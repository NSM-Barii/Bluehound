# UNIVERSAL CODE STEMS FROM HERE



# UI IMPORTS
from rich.console import Console
console = Console()


# ETC IMPORTS
import argparse


# NSM MODULES
from nsm_mesh_finder import BLE_Sniffer
from nsm_database import DataBase




class Main_Menu():
    """This class will gatekeep program wide logic"""


    parser = argparse.ArgumentParser(
        description="IOT Framework for Wireless Recon, Fuzzing & Hacking"
    )


   # parser.add_argument("-h", help="Display help, usage info, and project banner")
    parser.add_argument("-w", action="store_true", help="BLE Wardriving along with automatic data saving")
    parser.add_argument("-wv", action="store_true", help="BLE Wardriivng with command output")

    parser.add_argument("-s", help="Server IP for led lights")



    args = parser.parse_args()
    

    # WAR DRIVING
    war       = args.w
    war_v     = args.wv
    server_ip = args.s


    if  war or war_v: 
        BLE_Sniffer.main(war_drive=war, print=war_v, server_ip=server_ip); exit()




        






