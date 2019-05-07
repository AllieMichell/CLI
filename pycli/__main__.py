#!/opt/python3.7/bin/python

import sys
# import temp.mysql
# import temp.mongo
# from .classmodule import MyClass
# from .funcmodule import my_function 

def main():
    print('In main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    
    # my_function('hello world')
    # my_object = MyClass('AxtelLabs')
    # my_object.say_name()

if __name__ == '__main__':
    main()
    # temp.mysql.backupCommand()