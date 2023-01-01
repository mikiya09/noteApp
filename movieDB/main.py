#
# from dotenv import load_dotenv, find_dotenv
# import os
# import pprint 
# from pymongo import MongoClient 
# load_dotenv(find_dotenv())
#
#
# # connection setup
# password = os.environ.get("MONGODB_PWD")
# connection_string = f"mongodb+srv://mikiya:{password}@test01.ydhguxj.mongodb.net/?retryWrites=true&w=majority"
#
# client = MongoClient(connection_string)
#
#
# dbs = client.list_database_names()
# print(dbs)


import movieClass as mc

movieObject = mc.Movie()
movieObject.prompt()
