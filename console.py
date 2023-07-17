#!/usr/bin/python3
"""
Defines AirBnB console
"""
import cmd
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
BaseModel = models.base_model.BaseModel


class HBNBCommand(cmd.Cmd, BaseModel):
    """
    Defines ALX AirBnB command console interpreter
    """
    cls_list = ["BaseModel", "User", "State", "City", "Place", "Amenity",
                "Review"]
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when there is an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program. usage: 'quit'"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program usage: 'EOF'"""
        return True

    def default(self, line):
        """Handles '<class name>.command()' and Unknown commands"""
        if line.endswith(".all()"):
            line = line.rsplit(".")
            self.do_all(line[0])
        elif line.endswith(".count()"):
            line = line.rsplit('.')
            HBNBCommand.count(line[0])
        else:
            line = line.split(".", maxsplit=1)
            if line[0] in HBNBCommand.cls_list:
                if line[1].startswith("show"):
                    var = line[1].strip('\"show()\"')
                    var = f"{line[0]} {var}"
                    self.do_show(var)
                elif line[1].startswith("destroy"):
                    var = line[1].strip('\"destroy()\"')
                    var = f"{line[0]} {var}"
                    self.do_destroy(var)
                elif line[1].startswith("update"):
                    var = line[1].strip("update()")
                    var = var.split(", ")
                    cls_id = var[0].strip("\"")
                    cls_atr = var[1].strip("\"")
                    var = f"{line[0]} {cls_id} {cls_atr} {var[2]}"
                    self.do_update(var)

    def do_create(self, arg):
        """Creates a new instance of BaseModel,

        Saves it (to the JSON file) and prints out the id
        usage: 'create <class name>'
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
        usage: 'show <class name> <id>'or <class name>.show("<id>")
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
        usage: 'destroy <class name> <id>' or <class name>.destroy("<id>")
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

        based or not on the class name.
        usage: 'all <class name>' or 'all' or '<class name>.all()'
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
            words = arg.split(" ", maxsplit=3)
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
                    print("** no instance found **")
                else:
                    if len(words[3].split()) == 1:
                        var = words[3]
                        if var.startswith("\"") and var.endswith("\""):
                            found.__setattr__(words[2], eval(var))
                        else:
                            found.__setattr__(words[2], words[3])
                    else:
                        words[3] = words[3].split()
                        value = []
                        for word in words[3]:
                            if word.startswith("\"") or word.endswith("\""):
                                value.append(word)
                        value = f"{value[0]} {value[1]}"
                        found.__setattr__(words[2], value)
                    found.save()

    @staticmethod
    def count(arg):
        """Counts the number of objects in storage for a particular class

        usage: <class name>.count()
        """
        if arg not in HBNBCommand.cls_list:
            print("** class doesn't exist **")
        else:
            new_list = []
            models.storage.reload()
            all_obj = models.storage.all()
            for obj in all_obj:
                if obj.startswith(arg):
                    new_list.append(all_obj[obj])
            print(len(new_list))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
