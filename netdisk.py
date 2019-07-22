# _*_ codeing:utf-8 _*_
import socket, fcntl, struct
import os
import platform
from flask import Flask
from flask import render_template
from flask import request

def get_ip(ifname):  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24]) 

app = Flask(__name__)

def show_system_os():
    system_os = platform.system()
    return system_os

@app.route('/')
def index():
    files_name = os.listdir('static/')
    return render_template('index.html', files_name=files_name, netdisk_ip=netdisk_ip, ico='favicon.ico', system_os=show_system_os())


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return u'请先选择文件再上传'
    file.save('static/%s' % file.filename)

    return "此次上传文件为：<a href='http://%s/static/%s'>http://%s/static/%s</a>   <a href='http://%s'>返回</a>" % \
           (netdisk_ip, file.filename, netdisk_ip, file.filename, netdisk_ip)

if __name__ == '__main__':
    if show_system_os() == 'Windows':
        netdisk_ip = get_win_ip()
        app.run(host=netdisk_ip, port=8088, debug=True, threaded=True) # 测试模式 多线程
    if show_system_os() == 'Linux':
        netdisk_ip = get_linux_ip(b'ens160')
        app.run(host=netdisk_ip, port=8088, debug=True, threaded=True) # 测试模式 多线程

