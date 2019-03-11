import os
import paramiko




client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.load_system_host_keys()
client.connect(machine_ip, port=port, username=user_name, password=password)


process_name = 'sav-protect'

rel = os.popen("cat /etc/*-release").read()

if '6.9' in rel:
    os_version = '6.9'
else:
    os_version = '7.4'

print(os_version)

if os_version == '6.9':
    dmn = os.popen("/etc/init.d/sav-protect status").read()
else:
    dmn = os.popen("systemctl status sav-protect").read()

if 'inactive' in dmn:
    print('sophos is inactive')
    exit(0)
else:
    print('sophos is active')
    exit(1)
