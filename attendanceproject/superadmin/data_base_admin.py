import pymongo

client = pymongo.MongoClient("mongodb+srv://harsh:harsh@attendanceproject.rrlaxic.mongodb.net/?retryWrites=true&w=majority")
db = client['AttendanceProject'] 

def school_table():
    #making school table
    db = client['AttendanceProject']
    collection = db['school_table']
    