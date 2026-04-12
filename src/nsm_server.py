# THIS WILL HOUSE A WEB SERVER THAT WILL SHOW LIVE CORDINATES OF DEVICES <-- MIGHT BRANCH OFF OF THIS PROGRAM IDK LOL


# UI IMPORTS
from rich.console import Console
console = Console()


# ETC IMPORTS
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json, os; from pathlib import Path


# NSM IMPORTS
from nsm_vars import Variables



class HTTP_Handler(SimpleHTTPRequestHandler):
    """This class will handle/server http traffic"""



    def log_message(self, fmt, *args):
        """Silence HTTP server logs"""
        pass

    def do_GET(self) -> None:
        """This will handle basic web server requests"""


        live_map  = Variables.live_map
        war_drive = Variables.war_drive


        if self.path == "/api/devices":

            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", '*')
            self.end_headers()
            
            self.wfile.write(json.dumps(live_map).encode())

        elif self.path == "/api/wardriving":

            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", '*')
            self.end_headers()

            self.wfile.write(json.dumps(war_drive).encode())

        else: super().do_GET()




class Web_Server():
    """This class will launch the web server"""



    @staticmethod
    def start(CONSOLE, address:str="0.0.0.0", port:int=8000) -> None:
        """This method will start the web server"""

        gui_path = str(Path(__file__).parent.parent / "gui" )
        os.chdir(gui_path)

        server = HTTPServer(server_address=(address,port), RequestHandlerClass=HTTP_Handler) 
        
        CONSOLE.print(f"[bold green][+] Successfully Launched web server")
        CONSOLE.print(f"[bold green][+] Starting Web_Server on:[bold yellow] http://localhost:{port}")
        server.serve_forever(poll_interval=2)
    

