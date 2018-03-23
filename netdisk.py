# _*_ codeing:utf-8 _*_
import socket, struct, os, platform #, fcntl
from flask import Flask
from flask import render_template
from flask import request
def get_linux_ip(ifname): # 获取本机IP地址
    import fcntl
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])
def get_win_ip():
    s = socket.gethostbyname(socket.gethostname())
    return s
def show_system_os(): # 获取本机操作系统
    system_os = platform.system()
    return system_os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', system_os=show_system_os())

if __name__ == '__main__':
    if show_system_os() == 'Windows':
        netdisk_ip = get_win_ip()
        app.run(host=netdisk_ip, port=8088, debug=True, threaded=True) # 测试模式 多线程
    if show_system_os() == 'Linux':
        netdisk_ip = get_linux_ip(b'ens160')
        app.run(host=netdisk_ip, port=8088, debug=True, threaded=True) # 测试模式 多线程
