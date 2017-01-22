

import requests
import os

def get_exam_info(ip_addr, username, password):
    r = requests.get('http://' + ip_addr, auth=(username, password))
    print(r)
    j = r.json()
    return j

def set_session(ip_addr, login_user, token):
    with open(os.path.expanduser('~/.testsession'), mode='w') as session:
        session.writelines([ip_addr, '\n', login_user, '\n', token, '\n', time.time()])

#[ip_addr, login_user, token, time]
def get_session():
    with open(os.path.expanduser('~/.testsession')) as session:
        result = list(map(lambda x:x.rstrip(), session.readlines()))
    return result

def get_time():
    [ip_addr, login_user, token] = get_session()
    r = requests.get('http://' + ip_addr + '/time')
    return r.text

def start_compile():
    [ip_addr, login_user, token] = get_session()
    r = requests.get('http://' + ip_addr + '/compile')
    return int(r.text)

def try_get_result():
    [ip_addr, login_user, token] = get_session()
    r = requests.get('http://' + ip_addr + '/compile')
    if r.status_code == 200:
        return r.json()
    elif r.status_code == 302:
        return None
    else:
        raise hell


