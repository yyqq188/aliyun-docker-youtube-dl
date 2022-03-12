from fabric import Connection
import time
import os

# envs = os.environ
# host = envs["host"]  #'209.250.232.55'
# password = envs["password"] # 'J{y8USsMXuG3)Ph{'
# remote_video_path = envs["remote_video_path"] # "/root/new-yhl/youtube/youtube/"
# local_video_path_base = envs["local_video_path_base"] # "/Users/yanghualei/Downloads/movie_edit/"  todo 这里修改下

import config_self
host = config_self.config["host"]  #'209.250.232.55'
password = config_self.config["password"] # 'J{y8USsMXuG3)Ph{'
remote_video_path = config_self.config["remote_video_path"] # "/root/new-yhl/youtube/youtube/"
local_video_path_base = config_self.config["local_video_path_base"] # "/Users/yanghualei/Downloads/movie_edit/"  todo 这里修改下


target_path = os.path.join(local_video_path_base,time.strftime('%Y_%m_%d')) + "/"
#先创建目标日期目录
if not os.path.exists(target_path):
    os.makedirs(target_path)
connect = Connection(host=host, port=22, user='root', connect_kwargs={'password': password})
with connect as c:
    result = c.run("ls "+remote_video_path,hide=True)
    line = result.stdout.split('\n')
    for filename in line:
        try:
            c.get(remote_video_path + filename, target_path)
            print(filename + "    文件本地下载成功!")
        except:
            pass

    print('+++++++++++++++++++++++本地视频全部下载完成!!!+++++++++++++++++++++++')
    c.run("rm -rf  "+remote_video_path + " && mkdir " + remote_video_path,hide=True)
    print('+++++++++++++++++++++++远程服务器视频全部删除完成!!!+++++++++++++++++++++++')

