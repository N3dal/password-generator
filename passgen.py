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
    """return all the command passed arguments except the file name,
    and convert them into lower case."""

    return [arg.lower() for arg in argv[1:]]


def help_message():
    """print a help message.
    in simple words print the program documentation"""

    PASSGEN_DOCUMENTATION = """parse the user arguments and remove or raise an error,
    if there are any wrong argument.

        passgen --length
        select the password length by default this option is enabled,
        and its value is 8.

        passgen --lower
        add lower case letters to your password by default this option,
        is enabled.

        passgen --upper
        add upper case letters to your password by default this option,
        is disabled.

        passgen --numbers
        add number (0 through 9) to your password by default this option,
        is disabled.

        passgen --special
        add special ascii characters to your password by default this option,
        is disabled.

        passgen --no-lower
        remove lower case letters from your password.

        passgen --no--numbers
        remove numbers from your password.

        passgen -h or passgen --help
        show this help message.

    """

    print(DOC)


def default():
    """the default procedure when we get an empty commands,
    simply out when we get the passgen command without args,
    then we will call this function, and active the default options.
    'passgen' == 'password --length 8 --lower --numbers' 

    """

    pass


def arguments_parse():
    """parse the user arguments and remove or raise an error,
    if there are any wrong argument.

    see the help function for more info about option/keywords.

    """

    OPTIONS = (
        "--lower",
        "--upper",
        "--numbers",
        "--special",
        "--no-lower",
        "--no-numbers",
        "-h", "--help"
    )

    # get the user option aka command arguments.
    user_options = get_user_args()
    # print(user_options)

    # guard conditions.
    if not user_options:
        # if we get an empty collection,
        # simply out command without args,
        # then do the default procedure.
        default()

    if not all((option in OPTIONS) for option in user_options):
        # if we get any option does not exist in our options.
        print("Invalid option.")
        print("Try 'passgen --help' for more information.")

    if "--lower" in user_options and "--no-lower" in user_options:
        # if both --lower and --no-lower exist then we will apply,
        # --no-lower.
        pass

    if "--numbers" in user_options and "--no-numbers" in user_options:
        # if both --numbers and --no-numbers exist then we will apply,
        # --no-numbers.
        pass


def main():
    arguments_parse()


if __name__ == "__main__":
    main()
