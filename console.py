#!/usr/bin/python3
"""
Defines AirBnB console
"""
import cmd
import models
from models.user import User
from models.state import State
"""from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review"""
BaseModel = models.base_model.BaseModel


class HBNBCommand(cmd.Cmd, BaseModel):
    """
    Defines ALX AirBnB command interpreter
    """
    cls_list = ["BaseModel", "User", "State", "City", "Place", "Amenity",
               "Review"]
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
        elif arg not in HBNBCommand.cls_list:
            print("** class doesn't exist **")
        else:
            var = eval(arg + "()")
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
            if words[0] not in HBNBCommand.cls_list:
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
            if words[0] not in HBNBCommand.cls_list:
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
        if arg and arg not in HBNBCommand.cls_list:
            print("** class doesn't exist **")
        else:
            new_list = []
            models.storage.reload()
            all_obj = models.storage.all()
            for obj in all_obj:
                if arg:
                    if obj.startswith(arg):
                        new_list.append(str(all_obj[obj]))
                else:
                    new_list.append(str(all_obj[obj]))
            print(new_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id

        Attributes can be added or updated then saved to Json File
        """
        if not arg:
            print("** class name missing **")
        else:
            words = arg.split()
            if words[0] not in HBNBCommand.cls_list:
                print("** class doesn't exist **")
            elif len(words) == 1:
                print("** instance id missing **")
            elif len(words) == 2:
                print("** attribute name missing **")
            elif len(words) == 3:
                print("** value missing **")
            else:
                models.storage.reload()
                all_obj = models.storage.all()
                found = False
                for key, value in all_obj.items():
                    if key == words[0] + "." + words[1]:
                        found = value
                if not found:
                    print("** instance id missing **")
                else:
                    value = (words[3] + ".del")
                    try:
                        value_2 = eval(words[3])
                        print("No Space Error on", value_2)
                        """found.__setattr__(words[2], words[3])"""
                    except SyntaxError:
                        print("Space Error on", value[:-4])
                        """found.__setattr__(words[2], value)"""
                    found.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
