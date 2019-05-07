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
TEMPLATE OF MONGO DB
"""
def backupCommand ():
    print('Processing the command')
    dbhost = sys.argv[1:]
    dbport = sys.argv[2:]
    dbname = sys.argv[3:]
    tools.dumpMongoDB(dbhost, dbport, dbname)
    print('Success processing the command')