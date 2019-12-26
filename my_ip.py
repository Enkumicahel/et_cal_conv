import socket
import fcntl
import struct


def get_ip_address(ifname):
	'''Required the interface and then gets the ip address
	
	using no external package
	
	Arguments:
		ifname {[str]} -- [e.g. eth0, wlp2s0, enp3s0]
	
	Returns:
		[type] -- [description]
	'''
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# print(struct.pack(b'256s', ifname[:15]))
	return socket.inet_ntoa(fcntl.ioctl(
	    s.fileno(),
	    0x8915,
	    struct.pack('256s', bytes(ifname[:15], 'utf-8')))[20:24])

# print(get_ip_address('wlp2s0'))