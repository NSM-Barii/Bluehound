# THIS WILL HOUSE A WEB SERVER THAT WILL SHOW LIVE CORDINATES OF DEVICES <-- MIGHT BRANCH OFF OF THIS PROGRAM IDK LOL


# UI IMPORTS
from rich.console import Console
console = Console()


# ETC IMPORTS
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json, os; from pathlib import Path


# NSM IMPORTS
from nsm_vars import Variables
from nsm_database import Extensions



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

            self.wfile.write(json.dumps(live_map).encode())

        elif self.path == "/api/status":

            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", '*')
            self.end_headers()

            status = Extensions.get_status()
            self.wfile.write(json.dumps(status).encode())

        elif self.path == "/api/history":

            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", '*')
            self.end_headers()

            self.wfile.write(json.dumps(Variables.history).encode())

        elif self.path == "/api/stats":

            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", '*')
            self.end_headers()

            import time
            stats = {
                "min_count": Variables.min_count or 0,
                "max_count": Variables.max_count or 0,
                "current_avg": round(Extensions.avg, 2) if Extensions.avg is not None else 0,
                "uptime": round(time.time() - Variables.start_time, 1) if Variables.start_time else 0
            }
            self.wfile.write(json.dumps(stats).encode())

        elif self.path == "/api/threats":

            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", '*')
            self.end_headers()

            self.wfile.write(json.dumps(Variables.threat_log).encode())

        else: super().do_GET()

    def do_POST(self) -> None:
        """Handle POST requests"""

        if self.path == "/api/baseline/reset":

            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", '*')
            self.end_headers()

            Extensions.avg = None
            Extensions.last_count = 0
            Extensions.last_color = "green"
            Variables.history.clear()
            Variables.threat_log.clear()
            Variables.min_count = None
            Variables.max_count = None

            import time
            Variables.start_time = time.time()

            self.wfile.write(json.dumps({"status": "success", "message": "Baseline reset"}).encode())

        else:
            self.send_response(404)
            self.end_headers()




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
    

