#!/usr/bin/python3
# -----------------------------------------------------------------
# simple password generator cli.
# this is one of my 50 python project challenge for 2021.
#
#
#
# Author:N84.
#
# Create Date:Fri Apr 15 16:45:25 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------

import string
from sys import argv
import random
from os import name as OS_NAME
from os import system
from os import getcwd
import json


def clear():
    """wipe terminal screen."""

    if OS_NAME == "posix":
        # *nix machines.
        system("clear")

    else:
        # windows machines.
        system("cls")


clear()


def get_user_args():
    """return all the command passed arguments except the file name."""

    return argv[1:]
