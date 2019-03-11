import os
import paramiko

required_args = [('-H', 'hostname', 'Specify Vertica Server Address')]
optional_args = []

usage = "-H hostname"
params = parseUtility.parseArgs(usage, required_args, optimal_args)

machine = '10.128.38.49'
port = 22
username = 'root'
password = 'nicecti1!'



client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.load_system_host_keys()
client.connect(machine, port=port, username=username, password=password)
_, stdout, _ = client.exec_command("[ -d /opt/sophos-av ]; echo $?")
print(int(stdout.read().rstrip()))





# """
# if os.path.exists("/opt/sophos-av/"):
#     print("path exists")
# else:
#     print("path does not exists")
#
# if [-d "/opt/sophos-av/"]
#     echo 'exist'
#
# """