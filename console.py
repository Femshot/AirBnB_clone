#!/usr/bin/python3
"""
Defines AirBnB console
"""
import cmd
import models
from models.user import User
BaseModel = models.base_model.BaseModel


class HBNBCommand(cmd.Cmd, BaseModel):
    """
    Defines ALX AirBnB command interpreter
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when there is an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel,

        Saves it (to the JSON file) and prints out the id
        """
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            var = BaseModel()
            var.save()
            print(var.id)

    def do_show(self, arg):
        """Prints the string representation of an instance

        Based on the class name and id supplied
        """
        if not arg:
            print("** class name missing **")
        else:
            words = arg.split()
            if words[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(words) == 1:
                print("** instance id missing **")
            else:
                models.storage.reload()
                all_obj = models.storage.all()
                found = False
                for key, value in all_obj.items():
                    if key == words[0] + "." + words[1]:
                        found = value
                if found:
                    print(found)
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id

        Save the change into the JSON file after
        """
        if not arg:
            print("** class name missing **")
        else:
            words = arg.split()
            if words[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(words) == 1:
                print("** instance id missing **")
            else:
                models.storage.reload()
                all_obj = models.storage.all()
                found = False
                for key, value in all_obj.items():
                    if key == words[0] + "." + words[1]:
                        found = key
                if found:
                    del all_obj[found]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances

        based or not on the class name, i.e Ex: $ all BaseModel or $ all.
        """
        if arg and arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_list = []
            models.storage.reload()
            all_obj = models.storage.all()
            for obj in all_obj:
                new_list.append(str(all_obj[obj]))
            print(new_list)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
