import requests

def run_scan(target):
    try:
        response = requests.get(f"https://{target}")
        response_result = response.status_code, response.headers
        return response_result
    except:
        return "Invalid Response"
