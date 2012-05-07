# -*- coding: utf-8 -*-
 
import urllib2
import json
import subprocess
 
#通过git log命令获得最新的sha
run1 = subprocess.Popen(['git', 'log', '-1'],  stdout=subprocess.PIPE)
run2 = subprocess.Popen(["grep", "commit"], stdin=run1.stdout, stdout = subprocess.PIPE)
commit, error = run2.communicate()
local_sha = str(commit).rstrip('\n').split(' ')[-1]
 
#通过github的api获得当前github上最新的sha
response = urllib2.urlopen('https://api.github.com/repos/github用户名/github仓库名/commits').read()
json_data = json.loads(response)
remote_sha = json_data[0]['sha']
 
#如果不相等，用git pull命令更新代码
if not local_sha == remote_sha:
    subprocess.Popen(['git', 'pull'])    
else:
    print 'Already the latest'

