# -*- coding: utf-8 -*-
VERSION = "0.0.2"
__author__ = "Munis Isazade"
__email__ = "munisisazade@gmail.com"

import re, sys

COMMANDS = (
    "createapp",
    "version",
    "author",
    "help"
)


def help():
    print("")
    print("Type 'pyquick help <subcommand>' for help on a specific subcommand.")
    print("")
    print("Available subcommands:")
    print("")
    print("\033[31m[pyquick]\033[0m")
    for command in COMMANDS:
        print("\t" + command)


class Command(object):
    def __init__(self, command):
        self.command_name = command
        self.version = VERSION

    def run(self):
        if self.command_name == "createapp":
            self.createapp()
        elif self.command_name == "version":
            self.createapp()
        elif self.command_name == "author":
            self.createapp()
        else:
            self.unknowncommand()

    def createapp(self):
        pass

    def unknowncommand(self):
        print("Unknown command: '%s'" % self.command_name)
        print("Type 'pyquick help' for usage.")


if __name__ == '__main__':
    # if sys.argv[0] == "pyquick":
    if len(sys.argv) == 1:
        help()

    if len(sys.argv) > 1:
        if sys.argv[1] == "help":
            help()
        else:
            command = Command(sys.argv[1])
            command.run()
