





# UI IMPORTS
from rich.table import Table
from rich.live import Live
from rich.panel import Panel


# NETWORK IMPORTS
from bleak import BleakClient, BleakScanner


# ETC IMPORTS
import asyncio, time, time, statistics
from datetime import datetime


# NSM IMPORTS
from nsm_vars import Variables
from nsm_database import DataBase, Extensions


# CONSTANTS
console = Variables.console
LOCK    = Variables.LOCK
#DataBase = DataBase.Bluetooth





# REMASTERED <-- Bluehound
class Monitor_Bluetooth(): 
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
        cycle = 0
        unstable_devices = set()
        panel = Panel(renderable="Developed by nsm_barii", style="bold red", border_style="bold purple", expand=False)

        table = Table(title="BLE Driving", title_style="bold red", border_style="bold purple", style="bold purple", header_style="bold red")
        table.add_column("#"); table.add_column("RSSI", style=c2); table.add_column("Mac", style=c3); table.add_column("Manufacturer", style=c5); table.add_column("Local_name"); table.add_column("UUID", style=c3)


        try:

            scanner = BleakScanner()
            
            with Live(panel, console=console, refresh_per_second=4):

                while True:


                    await scanner.start()
                    await asyncio.sleep(5)
                    await scanner.stop()
                    devices = scanner.discovered_devices_and_advertisement_data
                    now     = time.time()
                    cycle   += 1



                    if devices: 
                    
                        
                        for mac, (device, adv) in devices.items():
                            
                            name  = adv.local_name or False
                            rssi  = adv.rssi
                            uuid  = adv.service_uuids or False
                            manuf = cls._get_manuf(manuf=adv.manufacturer_data) 
                            vendor = DataBase.get_vendor_main(mac=mac, verbose=False) 
                                            

                            data = {
                                "rssi": rssi,
                                "addr": mac,
                                "manuf": manuf,
                                "vendor": vendor,
                                "name": name,
                                "uuid": uuid,
                            }
    
                            

                            if (mac not in cls.live_map):
                                
                
                                cls.live_map[mac] = {
                                    "status": "stable",
                                    "data": data,
                                    "rssi_list": [],
                                    "unstable_hits": 0,
                                    "seen_cycles": 1,
                                    "first_seen": now,
                                    "last_seen": now
                                }

                                cls.devices += 1
                                console.print(f"{cls.devices}", rssi, mac, manuf, vendor, name, uuid)
                        
                            


                            cls.live_map[mac]["rssi_list"].append(rssi)
                            cls.live_map[mac]["seen_cycles"] += 1
                            cls.live_map[mac]["last_seen"]   = now
                            cls.live_map[mac]["cycle"]       = cycle

                    for mac, dev in list(cls.live_map.items()):
                            
                        use = f"[dim][>] {mac} ->"
                        weight       = 0
                        rssi_list    = dev["rssi_list"]
                        time_missing = now - dev["last_seen"]


                        
                        # // C++ IS SUPERIOR
                        if len(rssi_list) >= 3 and max(rssi_list) - min(rssi_list) > 30: 
                            weight += 1
                            console.print(f"{use}[yellow] rssi spike")

                        if (time_missing > 5): 
                            weight += 1
                            #console.print(f"{use}[yellow] short time gap")

                        if (time_missing > 10): 
                            weight += 2
                            console.print(f"{use}[yellow] long time gap")


                        if (weight >= 2): dev["unstable_hits"] += 1
                        else:           
                            if dev["unstable_hits"] > 0:
                                dev["unstable_hits"] -= 1


                        if (dev["unstable_hits"] >= 2):
                            if dev["status"] != "unstable":
                                console.print(f"[bold red][!] Unstable Device:[yellow] {mac}")
                                unstable_devices.add(mac)
                                dev["status"] = "unstable"
                                dev["stable_count"] = 0

                        else: 
                            if (dev["status"] == "unstable"):
                                dev["stable_count"] += 1

                                if (dev["stable_count"] >= 2): 
                                    dev["status"] = "stable"
                                    dev["stable_count"] = 0
                                    unstable_devices.discard(mac)
                                    console.print(f"[bold green][+] Device now stable:[yellow] {mac}")



                        """
                        Proverbs 27:17 As iron sharpens iron, so a friend sharpens another.
                        """



                        if time_missing > 30:
                            console.print(f"[bold yellow][-] Removing stale device:[/bold yellow] {mac}")
                            unstable_devices.discard(mac)
                            del cls.live_map[mac]


            

                    

                    # WILL MAKE A GLOBALIZED SAVE FOR ALL INFO FROM ALL MONITOR METHODS
                    # DataBase.push_results(devices=cls.war_drive, verbose=False)

                                        
                    count = len(devices) if devices else 0
                    Extensions.Controller(current_count=count, server_ip=server_ip)

                    avg       = Extensions.avg or 1
                    total     = len(cls.live_map) or 1
                    unstables = len({mac for mac in unstable_devices if mac in cls.live_map})

                    unstable_ratio = unstables / total
                    drop_score     = (avg - count) / avg if avg else 0

                    unstable_pct = round(unstable_ratio * 100, 2)
                    drop_pct     = round(drop_score * 100, 2)

                    c1 = "bold yellow"
                    panel.renderable = (
                        f"Session Devices:[{c1}] {total}[/{c1}]  -  "
                        f"Unstable Devices:[{c1}] {unstables}[/{c1}]  -  "
                        f"Unstable Ratio:[{c1}] {unstable_pct}%[/{c1}]  -  "
                        f"Drop Score:[{c1}] {drop_pct}%[/{c1}]"
                    )



        except KeyboardInterrupt as e:  console.print(f"[bold red][!] BLE Keyboard Exception Error:[bold yellow] {e}")
        except Exception as e:     console.print(f"[bold red][!] BLE Exception Error:[bold yellow] {e}")


        
    @classmethod
    def main(cls):
        """Run from here"""


        if not Variables.monitor: return False
        

        cls.devices = 0
        cls.num = 0

        server_ip    = Variables.server_ip
        cls.live_map = Variables.live_map


        try: 
            
            console.print("[yellow][+] Bluetooth/BLE Monitoring Activated")
            asyncio.run(cls._ble_printer(server_ip=server_ip))
    
        except KeyboardInterrupt: console.print("\n[bold red]Stopping....")
        except Exception as e: console.print(f"[bold red]Sniffer Exception Error:[bold yellow] {e}")






if __name__ == "__main__":
    Monitor_Bluetooth.main()