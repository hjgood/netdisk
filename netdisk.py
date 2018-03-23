# _*_ codeing:utf-8 _*_
import socket, fcntl, struct, os, platform
from flask import Flask
from flask import render_template
from flask import request
def get_ip(ifname): # 获取本机IP地址
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])
def show_system_os(): # 获取本机操作系统
    system_os = platform.system()
    return system_os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	netdisk_ip = get_ip(b'ens160')
	app.run(host=netdisk_ip, port=8088, debug=True, threaded=True) # 测试模式 多线程
