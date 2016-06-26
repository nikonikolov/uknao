import paramiko
from scp import SCPClient

def createSSHClient(server, port, user, password):
	ssh = paramiko.SSHClient()
	ssh.load_system_host_keys()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server, port, user, password)
	# SCPCLient takes a paramiko transport as its only argument
	scp = SCPClient(ssh.get_transport())

	scp.put('str.txt')
#	scp.get('test2.txt')

	scp.close()


server = "172.20.10.4"
username = "nao"
password = "nao"
port=22

createSSHClient(server, port, username, password)

