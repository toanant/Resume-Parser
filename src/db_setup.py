""" MongoDB is used as database to save the result """
from pymongo import MongoClient
connection = MongoClient()

"""
Create MongoDB database Named 'Resume' and save parsed details into
Collections of named to PDF files.
"""
dummy = connection.<dbname> # please enter here the database name
#dummy.create_collection('Resume')
resume = dummy.<collection name> # Please enter here the collection name
