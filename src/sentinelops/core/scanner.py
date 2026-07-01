import requests
from sentinelops.models.scan_results import ScanResult
from datetime import datetime

def run_scan(target):
    try:
        r = requests.get(f"https://{target}")
        
        result = ScanResult(
            target=target,
            response=r.status_code,
            server=r.headers['server'],
            content_type=r.headers['content-type'],
            last_mod=r.headers['last-modified'],
            scan_time=datetime.now()
        )

        return result
    except:
        return "Invalid Response"
