#!/usr/bin/python3
"""
fucntion do_deploy take one arg
take the path tthe pfile to deploy

Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy:

Prototype: def do_deploy(archive_path):
Returns False if the file at the path archive_path doesn’t exist
The script should take the following steps:

Upload the archive to the /tmp/ directory of the web server

Uncompress the archive to the folder
/data/web_static/releases/<archive filename without extension>
on the web server

Delete the archive from the web server

Delete the symbolic link /data/web_static/current from the web server

Create a new the symbolic link /data/web_static/current on the web server
linked to the new version of your code
(/data/web_static/releases/<archive filename without extension>)

All remote commands must be executed on your both web servers
(using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)

Returns True if all operations have been done correctly,
otherwise returns False

You must use this script to deploy it on your servers: xx-web-01 and xx-web-02

In the following example, the SSH key and the
username used for accessing
to the server are passed in the command line
Of course, you could define them as Fabric environment variables
(ex: env.user =...)
Disclaimer: commands execute by Fabric displayed
below are linked to the way
we implemented the archive function do_pack - like the mv command
depending of your implementation of it, you may don’t need it
"""
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

# give the ips of my both servers :3
env.hosts = ["34.75.79.213", "35.243.180.246"]


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
