#!/usr/bin/python3
"""
Defines AirBnB console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Defines ALX AirBnB command interpreter
    """

    prompt = "(hbnb)"

    def emptyline(self):
        """Do nothing when there is an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print()
        pass



if __name__ == "__main__":
     HBNBCommand().cmdloop()
