import subprocess, re, ipaddress, requests, json

def get_ips_from_ipsum() -> set:
    # Thank you stamparm
    url = 'https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt'
    content = requests.get(url).content
    return set(re.findall(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}', str(content)))

"""
add platform module (platform.system())
Linux: Linux
Mac: Darwin
Windows: Windows
"""

def netstat_list() -> set:
    result = set()
    net_conn = subprocess.check_output("netstat -n".split(), universal_newlines=True).splitlines()
    nets = re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(net_conn))
    for net in nets:
        if not ipaddress.IPv4Address(net).is_private:
            result.add((net).rstrip('\n'))
    return result

def powershell_file():
    with open('test.json', 'r') as f:
        data = f.read()
    #obj = json.loads(data)
    bad_ips = get_ips_from_ipsum()
    res = set(data['remoteaddress'].values())

powershell_file()

def bad_stuff():
    bad_ips = get_ips_from_ipsum() & netstat_list()
    if not len(bad_ips) == 0:
        for ip in bad_ips:
            print(f'Bad IP connected to you: {ip}')
    else:
        print(f'Network is clear of malicious IPs')
        

if __name__ == '__main__':
    bad_stuff()
