
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

def copyScms2():
    password = 'yxTEST#22126'
    window_path='S:\workspace2017_IJ\scms2\scms2.static\webapp\scms2\embed/1901\index.vm'
    username='root'
    Linux_ip='192.168.22.126'
    Linux_path='/data/www/ROOT/static/scms2/embed/1901'
    print("begin -------")
    cmd = 'E:\chromeDownlod\PSCP\pscp.exe -r -scp -pw {password} {window_path} {username}@{Linux_ip}:{Linux_path}'.format(
        password=password, window_path=window_path, username=username, Linux_ip=Linux_ip, Linux_path=Linux_path)
    os.system(cmd)
    print("end-------")
# copy()


copyScms2()