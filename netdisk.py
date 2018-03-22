# _*_ codeing:utf-8 _*_
import socket, fcntl, struct
from flask import Flask
def get_ip(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

app = Flask(__name__)

if __name__ == '__main__':
	netdisk_ip = get_ip(b'ens160')
	app.run(host=netdisk_ip, port=8088, debug=True, threaded=True)
