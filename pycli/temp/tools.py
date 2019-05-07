#!/opt/python3.7/bin/python
import os
import sys
import time
import pipes
import pymongo
import pymysql
import paramiko
import subprocess
from datetime import datetime
from pymongo import MongoClient

"""
FILE MODULE OF ALL THE FUNCTIONS THAT USE TO 
EXECUTE DUMP COMMANDS OF MySQL or MongoDB 
DATABASES
"""

def message (name:str) -> str:
    print('The name is :: {0}'.format(name))

def renameFileMYSQL(filename:str) -> str:
    """
    This function is used to rename the file when the file was 
    created only when the databse is MySQL 
    Params
    ------
        filename: Name of database to need rename
    Returns
    -------
        renamefile: New name of database when they was created
    """
    try:
        file_name = '{0}'.format(filename)
        mod_time = os.stat(file_name).st_mtime
        create = datetime.fromtimestamp(mod_time)
        create_str = str(create)
        separate_date = create_str.split('-')
        separate_time = create_str.split(':')
        date = separate_date[0]+separate_date[1]+separate_date[2]
        time = separate_time[0]+separate_time[1]+separate_time[2]
        lastdate = date[0:8]+"_"+time[11:17]
        renamefile = os.rename(file_name, lastdate+'.sql')
        return renamefile
    except OSError as e: 
        print(e)

def renameFileMONGO (filename:str) -> str: 
    """
    This function is used to rename the file when the file was 
    created only when the database is MongoDB
    Params
    ------
        filename: Name of the database to need rename
    Returns 
    -------
        renamefile: New name of database when they was creaded
    """
    try:
        file_name = '{0}'.format(filename)
        mod_time = os.stat(file_name).st_mtime
        create = datetime.fromtimestamp(mod_time)
        create_str = str(create)
        separate_date = create_str.split('-')
        separate_time = create_str.split(':')
        date = separate_date[0]+separate_date[1]+separate_date[2]
        time = separate_time[0]+separate_time[1]+separate_time[2]
        lastdate = date[0:8]+"_"+time[11:17]
        renamefile = os.rename(file_name, lastdate)
        return renamefile
    except OSError as e: 
        print(e)

def renameFileJENKINS (filename:str) -> str:
    """
    This function is used to rename the file of configurations of Jenkins
    when the file was creaded 
    Params
    ------
        filename: Name of the file of configurations of Jenkins 
    Returns
    ------
        renamefile: New name of configuration file when they was crated
    """
    try:
        file_name = '{0}'.format(filename)
        mod_time = os.stat(file_name).st_mtime
        create = datetime.fromtimestamp(mod_time)
        create_str = str(create)
        separate_date = create_str.split('-')
        separate_time = create_str.split(':')
        date = separate_date[0]+separate_date[1]+separate_date[2]
        time = separate_time[0]+separate_time[1]+separate_time[2]
        lastdate = date[0:8]+"_"+time[11:17]
        renamefile = os.rename(file_name, lastdate)
        return renamefile
    except OSError as e: 
        print(e)

def dumpMySQL (dbuser:str, dbpassword:str, dbhost:str, dbname:str) -> str: 
    """
    This function is used to created the dump command to execute the mysqldump and get the
    local backup of this database
    Params
    ------
        dbuser: User of the database
        dbpassword: Password of the database
        dbhost: IP of the database 
        dbname: Name of the database
    Returns
    -------
        command: Return the command to do in this case mysqldump
    """
    try:
        if dbuser=='' or dbpassword=='' or dbhost=='' or dbname=='':
            print('Invalid Dump, the command has an alone variable')
        else:
            print('Processing the Dump command')
            command = 'mysqldump -- databases --create-options --add-drop-database --routines=true --triggers -h{2} -u{0} -p{1} {3} > latest.sql'.format(dbuser, dbpassword, dbhost, dbname)
            os.system(command)
            return command
    except OSError as e:
        print(e)

def dumpMongoDB (dbhost:str, dbport:str, dbname:str) -> str:
    """
    This function is used ti create the dump command to execute the mongodump and get
    the local backup of this database
    Params
    ------
        dbhost: IP of the database
        dbport: Port of the database
        dbname: Name of the database
    Returns
        command: Return the command to do in this case mongodump
    """
    try: 
        if dbhost=='' or dbport=='' or dbname=='':
            print('Invalid Dump, the command has an alone variable')
        else: 
            print('Processing the Dump command')
            command = 'mongodump --host {0} --port {1} --db {2} --out latest'.format(dbhost, dbport, dbname)
            os.system(command)
            return command
    except OSError as e: 
        print(e)