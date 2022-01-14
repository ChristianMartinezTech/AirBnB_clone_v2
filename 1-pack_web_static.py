#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of
the web_static folder, using the function do_pack """

from os import path
from fabric.api import local
from datetime import datetime


def do_pack():
    """ must return the archive path if the archive has been
    correctly generated """

    # datetime variable with format
    var_time = datetime.now().strftime("%Y%m%d%H%M%S")

    # Check if the folder versions exists
    if not path.isdir("./versions/"):
        local("mkdir versions")

    # Name crafting
    file_name = "versions/web_static_" + var_time + ".tbz"

    # File compression
    local("tar -cvjf {} web_static".format(file_name))

    # Check if the compression was succesfull
    if path.isfile(file_name):
        return file_name
