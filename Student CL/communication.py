
import requests

def get_exam_info(ip_addr, username, password):
    r = requests.get('http://' + ip_addr, auth=(username, password))
    j = r.json()
    print(j)
    return j

