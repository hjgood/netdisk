# _*_ codeing:utf-8 _*_

import socket

import os

import platform

from flask import Flask

from flask import render_template

from flask import request



def get_ip():  

    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()

    return ip



app = Flask(__name__)



def show_system_os():

    system_os = platform.system()

    return system_os



@app.route('/')

def index():

    files_name = os.listdir('static/')

    return render_template('index.html',system_os = show_system_os(),files_name = files_name)



@app.route('/upload', methods=['GET', 'POST'])

def upload():

    file = request.files.get('file')

    if not file:
 
        return u"请先选择文件再上传,<a href='http://%s:8088  '>返回</a>" % (netdisk_ip)

    file.save('static/%s' % file.filename)

    return "此次上传文件为：<a href='http://%s:8088/static/%s'>http://%s:8088/static/%s</a>   <a href='http://%s:8088'>返回</a>" % (netdisk_ip,file.filename,netdisk_ip,file.filename,netdisk_ip)



if __name__ == '__main__':

    netdisk_ip = get_ip()
    app.run(host = netdisk_ip, port=8088, debug=True, threaded=True) # 测试模式 多线程
