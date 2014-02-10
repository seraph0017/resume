#encoding:utf-8
"""
author:tianyu0915@gmail.com
version:1.4
datetime:2013-11-23

"""
import time
import os
from cuisine import *
from fabric.api import *
#from cuisine import *
from fabric.contrib.project import rsync_project, upload_project
from fabric.operations import get
from fabric.contrib.files import  exists
today = time.strftime("%Y-%m-%d-%H%M", time.localtime())

env.name            = 'resume'
env.hosts           = ['repo.t-y.me']
env.user            = 'ubuntu'
env.path            = '/srv/{}'.format(env.name)
env.nginx_conf      = '/usr/local/nginx/conf/vhost/{}'.format(env.name)
env.repositories    = 'https://github.com/tianyu0915/{}.git'.format(env.name)

def sync(branch_name='master'):
    with mode_sudo():
        with cd(env.path):
            run('sudo git checkout -- .')
            run('sudo git checkout {0}'.format(branch_name))
            for f in ['html','pdf']:
                run('cp readme.{} /srv/t-y/resume4{}.{}'.format(f,branch_name,f))


