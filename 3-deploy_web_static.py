#!/usr/bin/python3
"""module containing deploy function for web_static
"""

from fabric.api import *
from datetime import datetime

env.hosts = ['54.234.154.44', '35.175.189.164']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """create a .tgz archive of web_static
    """

    local('mkdir -p versions')
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_" + now + ".tgz"

    try:
        local('tar -cvzf {} web_static'.format(filename))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """pushes web_static .tgz archive file to webserver,
    uncompresses files to production folder
    updates symlink and deletes archive file
    """

    filename = archive_path.partition('versions/')[2].split(".tgz")[0]
    dirname = '/data/web_static/releases/' + filename + '/'

    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(dirname))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(filename, dirname))
        run('rm /tmp/{}.tgz'.format(filename))
        run('mv {}web_static/* {}'.format(dirname, dirname))
        run('rm -rf {}web_static'.format(dirname))
        run('ln -sfn {} /data/web_static/current'.format(dirname))
        return True
    except Exception:
        return False


def deploy():
    """calls do_pack and do_deploy in one place for deployment
    """
    archive_path = do_pack()
    if not archive_path:
        return None
    return do_deploy(archive_path)
