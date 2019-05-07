#!/opt/python3.7/bin/python
import os
import sys
import time
import json
import tools
import pymongo
import paramiko
import urllib.request
from datetime import datetime
from pymongo import MongoClient

"""
TEMPLATE OF MYSQL
"""
def backupCommand ():
    print('Processing the command')
    dbuser = sys.argv[1:]
    dbpassword = sys.argv[2:]
    dbhost = sys.argv[3:]
    dbname = sys.argv[4:]
    tools.dumpMySQL(dbuser, dbpassword, dbhost, dbname)
    print('Success processing the command')