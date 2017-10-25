
import os

def copy():
    password = 'abc#123'
    window_path='D:\\test'
    username='root'
    Linux_ip='192.168.29.198'
    Linux_path='/root'
    print("begin -------")
    cmd = 'E:\chromeDownlod\PSCP\pscp.exe -r -pw {password} {window_path} {username}@{Linux_ip}:{Linux_path}'.format(
        password=password, window_path=window_path, username=username, Linux_ip=Linux_ip, Linux_path=Linux_path)
    os.system(cmd)

copy()