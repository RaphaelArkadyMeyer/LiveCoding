
import requests

def get_exam_info(ip_addr, username, password):
    r = requests.get(ip_addr, auth=(username, password))
    return r.json()
