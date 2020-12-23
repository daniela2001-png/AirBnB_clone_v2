#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz
archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""
import os.path
from datetime import datetime
from fabric.api import local
import time
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

# give the ips of my both servers :3
env.hosts = ["34.75.79.213", "35.243.180.246"]


def do_pack():
    """Create a tar file inside a dir"""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If file doesn't exist archive_path or an error occurs - False.
        else: True.
    """

    if os.path.isfile(archive_path) is False:
        return False
    # archive_path =versions/web_static_20170315003959.tgz
    file = archive_path.split("/")[-1]
    name = file.replace('.tgz', '')

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
            format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
            format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
            format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name)).failed is True:
        return False
    return True


def deploy():
    """Deploys all"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
