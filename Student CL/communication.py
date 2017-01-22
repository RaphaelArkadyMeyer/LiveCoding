
import requests

def get_exam_info(ip_addr_, username_, password_):
    global ip_addr, login_user, login_pass
    ip_addr  = ip_addr_
    username = username_
    password = password_
    r = requests.get('http://' + ip_addr, auth=(username, password))
    j = r.json()
    print(j)
    return j

def get_time():
    global ip_addr, login_user, login_pass
    # TODO query dæmon instead
    r = requests.get('http://' + 'localhost:5000' + '/time')
    return r.text
