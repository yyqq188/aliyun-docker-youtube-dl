from fabric import Connection

# import os
# envs = os.environ
# host = envs["host"]  #'209.250.232.55'
# password = envs["password"] # 'J{y8USsMXuG3)Ph{'
# local_list_path = envs["local_list_path"] # './list.txt'  todo 这里修改下
# remote_list_path = envs["remote_list_path"] # '/root/new-yhl/youtube'
# remote_start_sh_path = envs["remote_start_sh_path"] # /root/new-yhl/youtube/start.sh

import config_self
host = config_self.config["host"]  #'209.250.232.55'
password = config_self.config["password"] # 'J{y8USsMXuG3)Ph{'
local_list_path = config_self.config["local_list_path"] # './list.txt'  todo 这里修改下
remote_list_path = config_self.config["remote_list_path"] # '/root/new-yhl/youtube'
remote_start_sh_path = config_self.config["remote_start_sh_path"] # /root/new-yhl/youtube/start.sh

connect = Connection(host=host, port=22, user='root', connect_kwargs={'password':password})
with connect as c:
    c.put(local_list_path, remote_list_path)
    print("+++++++++++++++++++++++上传url文件到远程服务器完成!!!+++++++++++++++++++++++")
    c.run("bash " + remote_start_sh_path ,hide=True)
    print('+++++++++++++++++++++++远程服务器视频下载完成!!!+++++++++++++++++++++++')
    print('---------------------')



