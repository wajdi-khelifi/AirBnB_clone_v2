#!/usr/bin/python3
"""module containing do_deploy function for web_static
"""

from fabric.api import *
env.hosts = ['54.234.154.44', '35.175.189.164']


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
        run('ln -sfn {} /data/web_static/current'.format(dirname))
        return True
    except Exception:
        return False
