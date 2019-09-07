import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.99.1",username="manik",password="Rmani123")
stdin,stdout,stderr=ssh.exec_command("ipconfig",get_pty=True)
#print(stdout.readlines())
print(''.join(stdout.readlines()))

#print(stdout.channel.recv_exit_status())
#for line in stdout:
	#print(line)