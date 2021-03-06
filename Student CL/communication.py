
import time
import requests
import os

def get_exam_info(ip_addr, username, password):
    r = requests.get('http://' + ip_addr, auth=(username, password))
    print(r)
    j = r.json()
    return j

def set_session(ip_addr, login_user, token):
    with open(os.path.expanduser('~/.testsession'), mode='w') as session:
        session.writelines([ip_addr, '\n', login_user, '\n', token, '\n', str(time.time())])

#[ip_addr, login_user, token, time]
def get_session():
    with open(os.path.expanduser('~/.testsession')) as session:
        result = list(map(lambda x:x.rstrip(), session.readlines()))
    return tuple(result)

def get_time():
    ip_addr, login_user, token, time = get_session()
    r = requests.get('http://' + ip_addr + '/time')
    return r.text

def start_compile():
    ip_addr, login_user, token, time = get_session()
    r = requests.post('http://' + ip_addr + '/compile')
    return r

def try_get_result( job_id ):
    ip_addr, login_user, token, time = get_session()
    r = requests.get('http://' + ip_addr + '/queue/' + str(job_id))
    if r.status_code == 200:
        return r.json()
    elif r.status_code == 302:
        return None
    else:
        print ('Unknown error code', r.status_code)


