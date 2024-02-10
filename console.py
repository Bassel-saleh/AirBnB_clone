#!/usr/bin/python3
''' console main operation file '''
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    '''subclass for cmd class'''

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file), and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of
        all instances based or not on the class name"""
        args = arg.split()
        if not arg:
            objs = storage.all().values()
        elif args[0] in storage.classes:
            objs = [v for k, v in storage.all().items() if args[0] in k]
        else:
            print("** class doesn't exist **")
            return
        print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        try:
            attr_value = eval(attr_value)
        except NameError:
            pass
        setattr(storage.all()[key], attr_name, attr_value)
        storage.save()

    def emptyline(self):
        """does nothing only for pressing enter on empty line"""
        pass

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        return True

    def do_quit(self, args):
        """Quits the interpreter"""
        raise SystemExit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
