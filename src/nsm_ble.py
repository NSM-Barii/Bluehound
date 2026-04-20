# TEST MODULE WILL BE STARTING BLE FRAMEWORK FROM HERE
 

# UI IMPORTS
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.console import Console


# HACKING IMPORTS
from bleak import BleakClient, BleakScanner


# ETC IMPORTS
import asyncio, os, time, random, threading, requests


# Yoda
from pathlib import Path
from gtts import gTTS
import subprocess


# NSM IMPORTS
from nsm_vars import Variables
from nsm_server import Web_Server
from nsm_database import DataBase, Extensions


console = Console()
LOCK = threading.Lock()


class BLE_Sniffer(): 
    """This will be a ble hacking framework"""



    @classmethod
    async def _ble_discover(cls):
        """This will sniff traffic"""


        devices = await BleakScanner.discover(timeout=60, return_adv=True)

        return devices
    
    

    @classmethod
    def _get_manuf(cls, manuf):
        """This will parse and get manuf"""


    
        if not manuf: return False

        for key, value in manuf.items():
            id = key; hex = value.hex()
        


        company = DataBase.get_manufacturer(id=id, data=hex)


        return company



    @classmethod
    async def _ble_printer(cls, server_ip=False) -> None:
        """Lets enumerate"""


        c1 = "bold red"
        c2 = "bold yellow"
        c3 = "bold green"
        c4 = "bold red"
        c5 = "bold blue"
        table = ""
        timeout = 10

        table = Table(title="BLE Driving", title_style="bold red", border_style="bold purple", style="bold purple", header_style="bold red")
        table.add_column("#"); table.add_column("RSSI", style=c2); table.add_column("Mac", style=c3); table.add_column("Manufacturer", style=c5); table.add_column("Local_name"); table.add_column("UUID", style=c3)


        try:

            scanner = BleakScanner()

            while 0 < timeout:

                await scanner.start()
                await asyncio.sleep(5)
                await scanner.stop()
                devices = scanner.discovered_devices_and_advertisement_data


                #current_time = time.time()
                #stale_macs = [mac for mac, data in cls.live_map.items() if current_time - data["up_time"] > 30]
                #for mac in stale_macs: del cls.live_map[mac]

                if devices: 
                
                    
                    for mac, (device, adv) in devices.items():

                        name  = adv.local_name or False
                        rssi  = adv.rssi
                        uuid  = adv.service_uuids or False
                        manuf = cls._get_manuf(manuf=adv.manufacturer_data) 
                        vendor = DataBase.get_vendor_main(mac=mac, verbose=False) 
                        up_time = time.time()
                                        

                        data = {
                            "rssi": rssi,
                            "addr": mac,
                            "manuf": manuf,
                            "vendor": vendor,
                            "name": name,
                            "uuid": uuid,
                            "up_time": up_time
                        }


                        cls.live_map[mac] = data

                        if mac not in cls.devices:
                            
                            cls.devices.append(mac)
                            cls.war_drive[len(cls.devices)] = data
            
                            console.print(f"{len(cls.devices)}", rssi, mac, manuf, vendor, name, uuid)
        


                DataBase.push_results(devices=cls.war_drive, verbose=False)
                count = len(devices)
                Extensions.Controller(current_count=count, server_ip=server_ip)


                        

            console.print(f"\n[bold green][+] Found a total of:[bold yellow] {len(cls.devices)} devices")


        except KeyboardInterrupt:  return KeyboardInterrupt
        except Exception as e:     return Exception


        
    @classmethod
    def main(cls):
        """Run from here"""


        if not Variables.sniffer: return False
        

        cls.devices = []
        cls.num = 0

        server_ip   = Variables.server_ip
        cls.live_map    = Variables.live_map
        cls.war_drive   = Variables.war_drive


        try:

            console.print("[yellow][+] Bluetooth Sniffer Activated")
            threading.Thread(target=Web_Server.start, args=(console, ), daemon=True).start(); time.sleep(1)
            asyncio.run(BLE_Sniffer._ble_printer(server_ip=server_ip))
    
        
        except KeyboardInterrupt: console.print("\n[bold red]Stopping....")
        except Exception as e: console.print(f"[bold red]Sniffer Exception Error:[bold yellow] {e}")




