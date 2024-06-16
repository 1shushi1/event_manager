from pymongo import MongoClient
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

"""

Database client

"""

database = MongoClient(os.environ['MONGODB']).event_management

"""

Collections

"""
users = database.users
events = database.events
