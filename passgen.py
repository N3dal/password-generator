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

from string import (ascii_lowercase, ascii_uppercase, punctuation, digits)
from sys import argv, exit
from random import (randint, choice)
from os import name as OS_NAME
from os import system
from pyperclip import copy as copy2clipboard

# TODO: store the password in json file.
# TODO: send any generated password to the clipboard. # DONE.
# TODO: add option to show the password map=> default-values dict to the user with fancy look, not in the dict form.


# set the defaults.
DEFAULT_VALUES = {
    "len": 8,  # password default length.
    "upper": False,  # use upper case letters.
    "lower": True,  # use lower case letters.
    "symbols": False,  # include symbols.
    "numbers": False  # include numbers.
}

PROGRAM_OPTIONS_REPL = (
    "clear", "cls",  # same command.
    "generate", "gen",  # same command.
    "set",
    "options",
    "help",
    "exit", "quit",  # same command.
    "show",
    "map"
)

ARGUMENTS = (
    "--length",
    "--lower",
    "--upper",
    "--numbers",
    "--special",
    "--no-lower",
    "--no-numbers",
    "-h", "--help"
)

# var to store the last password that have been generated.
last_password = ""


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


def _help(doc_type: int = 0):
    """print a help message.
    in simple words print the program documentation.
    notice that if we pass 0 then the doc that will been,
    shown is for program arguments.
    and if we pass 1 then the doc that will been shown,
    is for program repl commands.
    other numbers will consider as 0"""

    # guard conditions.
    if doc_type not in (0, 1):
        doc_type = 0

    # note there are two different help msgs,
    # one for the program arguments and the,
    # another to the repl commands.

    PASSWORD_GENERATOR_DOCUMENTATION_ARGUMENTS = """parse the user arguments and remove or raise an error,
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

    PASSWORD_GENERATOR_DOCUMENTATION_REPL_COMMANDS = """
    clear = cls
        clear the REPL screen.

    generate = gen
        generate random password with values in the password map,
        and send it to the clipboard directly.

    set
        change password map value to generate random patterns for your passwords.

    options
        show all available options with brief description.

    help
        show help msg simply out this msg.

    exit = quit
        ending the REPL session.

    show
        show last password had been generated, and send it to the clipboard again.

    map
        show the password generated pattern, simply-out password map values.
    """

    if doc_type == 0:
        # print arguments doc.
        print(PASSWORD_GENERATOR_DOCUMENTATION_ARGUMENTS)

    elif doc_type == 1:
        # print repl commands doc.
        print(PASSWORD_GENERATOR_DOCUMENTATION_REPL_COMMANDS)

    else:
        # print("Error")
        raise("Error in help msg.")

    return None


def _exit():
    """when the user enter exit command,
    for end the program execution."""

    exit()


def _generate():
    """generate new password depending on,
    the password_default option dictionary."""

    global last_password

    string = ""

    if DEFAULT_VALUES["lower"]:
        # if the lower option enabled.
        string += ascii_lowercase

    if DEFAULT_VALUES["upper"]:
        # if the upper option enabled.
        string += ascii_uppercase

    if DEFAULT_VALUES["symbols"]:
        # if the symbols option enabled.
        string += punctuation

    if DEFAULT_VALUES["numbers"]:
        # if the numbers options enabled.
        string += digits

    password_length = DEFAULT_VALUES["len"]

    generated_password = "".join(choice(string)
                                 for _ in range(password_length))

    print(generated_password)

    # then send the generated password to clipboard.
    copy2clipboard(generated_password)

    # now tell the user that the password in clipboard.
    print("\nthe password in the clipboard you can paste it directly.")

    # now add the generated password to last password had been generated.
    last_password = generated_password

    return generated_password


def _show():
    """show last password had been generated."""

    # first checkout if their pass word or not.
    # guard condition.
    if not last_password:
        # if the last_password string is empty.
        print("No password Had been generated, generate one using 'generate' command.")

        return None

    print(last_password)

    # then send the generated password to clipboard.
    copy2clipboard(last_password)

    # now tell the user that the password in clipboard.
    print("\nthe password in the clipboard you can paste it directly.")

    return last_password


def _set(key: str, value: object):
    """set new value for password default dictionary"""

    global DEFAULT_VALUES

    DEFAULT_VALUES[key] = value


def _options():
    """show all repl options"""

    for index, option in enumerate(PROGRAM_OPTIONS_REPL, 1):
        print(f"[{str(index).zfill(2)}] '{option}'")

    return None


def _map():
    """show the default password dictionary in simple way for the users."""
    pass


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
            _help(1)

        elif usr_input in ("generate", "gen"):
            _generate()

        elif usr_input in "set":
            _set()

        elif usr_input == "options":
            _options()

        elif usr_input == "show":
            _show()

        elif usr_input == "map":
            _map()

        else:

            # first print wrong msg then print commands list.
            print(f"There's no command called '{usr_input}'\n")

            _options()


def arguments_parse():
    """parse the user arguments and remove or raise an error,
    if there are any wrong argument.

    see the help function for more info about option/keywords.

    arguments parse.

    """

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

    if not all((option in ARGUMENTS) for option in user_options):
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

    main_loop()


if __name__ == "__main__":
    main()
