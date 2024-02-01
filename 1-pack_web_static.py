#!/usr/bin/python3
"""Fabric script that generates a .tgz"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """.tgz archive"""
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")

        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)

        local("tar -cvzf {} web_static".format(archive_path))

        print("web_static packed: {} -> {}Bytes".format(archive_path, size))

        return archive_path
    except Exception as e:
        return None
