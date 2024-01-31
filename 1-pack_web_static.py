#!/usr/bin/python3
"""create .tgz archive of web_static folder using Fabric
"""

from fabric.api import local
from datetime import datetime


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
