import sys
import paramiko
pwd=str(sys.argv[1])
hosts=str(sys.argv[2])
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for host in hosts.split(","):
    print("conecting to",host)
    ssh.connect(hostname=host,username="mani",password=pwd)
    stdin,stdout,stderr=ssh.exec_command("whoami;time",get_pty=True)
    print(''.join(stdout.readlines()))
    #35.154.62.146