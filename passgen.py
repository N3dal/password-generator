#!/usr/bin/python3
# -----------------------------------------------------------------
# simple password generator.
# this is one of my 50 python project challenge for 2021.
# simple CLI password manager.
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
from sys import argv, exit
from random import (randint, choice)
from os import name as OS_NAME
from os import system
from os import getcwd
import json

# TODO: store the password in json file.

# set the defaults.
DEFAULT_VALUES = {
    "len": 8,  # password default length.
    "upper": False,  # use upper case letters.
    "lower": True,  # use lower case letters.
    "symbols": False,  # include symbols.
    "numbers": False  # include numbers.
}

PROGRAM_OPTIONS = (
    "clear", "cls"  # same command.
    "generate", "get",  # same command.
    "use", "set",  # same command.
    "options",
    "help",
    "exit", "quit"  # same command.
    "show"
)


def clear():
    """wipe terminal screen."""

    if OS_NAME == "posix":
        # for *nix machines.
        system("clear")

    else:
        # for windows machines.
        system("cls")


clear()


def get_user_args():
    """return all the command passed arguments except the file name,
    and convert them into lower case."""

    return [arg.lower() for arg in argv[1:]]


def get_user_input(msg: str = ">>> "):
    """get input from the user and return it,
    after stript it and lower it.
    """

    return input(msg).strip().lower()


def _help():
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

    return None


def main_loop():
    """the main loop for our REPL program."""

    while True:
        usr_input = get_user_input()

        if usr_input in ("exit", "quit"):
            # end the program .
            _exit()

        elif usr_input in ("clear", "cls"):
            clear()

        elif usr_input == "help":
            pass

        elif usr_input in ("generate", "get"):
            pass

        elif usr_input in ("set", "use"):
            pass

        elif usr_input == "options":
            pass

        elif usr_input == "show":
            pass

        else:
            # show the option or the help,
            # msg if the user give us a wrong,
            # command or wrong option format.
            print(usr_input)


def arguments_parse():
    """parse the user arguments and remove or raise an error,
    if there are any wrong argument.

    see the help function for more info about option/keywords.

    """

    OPTIONS = (
        "--length",
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

    # create the option list that we will return,
    # simply-out the parsed option list.
    parsed_option_list = []

    # guard conditions.
    if not user_options:

        # if we get an empty collection,
        # simply-out command without args,
        # then do the default procedure.
        # the default procedure when we get an empty commands,
        # simply-out when we get the passgen command without args,
        # then we will call this function, and active the default options.
        # 'passgen' == 'password --length 8 --lower --numbers'.

        DEFAULT_OPTIONS = (
            "--length", 8,
            "--lower",
            "--numbers"
        )

        parsed_option_list.extend(DEFAULT_OPTIONS)

    if not all((option in OPTIONS) for option in user_options):
        # if we get any option does not exist in our options.
        print("Invalid option.")
        print("Try 'passgen --help' for more information.")

        return None

    if "--lower" in user_options and "--no-lower" in user_options:
        # if both --lower and --no-lower exist then we will apply,
        # --no-lower.
        parsed_option_list.append("--no-lower")

    if "--numbers" in user_options and "--no-numbers" in user_options:
        # if both --numbers and --no-numbers exist then we will apply,
        # --no-numbers.
        parsed_option_list.append("--no-numbers")

    return parsed_option_list


def main():
    val = arguments_parse()

    print(val)


if __name__ == "__main__":
    main()
