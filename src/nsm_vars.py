# THIS WILL HOLD MODULE WIDE VARS


# UI IMPORTS
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.console import Console


# ETC IMPORTS
import threading


class Variables():
    """This will house variables"""


    # MODES
    sniffer = False
    monitor = False

    # LAUNCH LIVE WEB DASHBOARD
    web = False

    # SCAN TIMING
    scan_window   = 5   # HOW LONG EACH SCAN LISTENS
    scan_interval = 0   # HOW LONG TO WAIT BETWEEN SCANS (0 = CONTINUOUS)

    # CONSTANTS
    console = Console()
    LOCK    = threading.RLock()


    server_ip   = False
    file_saving = False

    live_map  = {}
    war_drive = {}

    # HISTORICAL TRACKING
    history = []
    max_history = 500
    min_count = None
    max_count = None
    threat_log = []
    start_time = None