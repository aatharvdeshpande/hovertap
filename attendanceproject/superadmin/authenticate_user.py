import pymongo
from django.shortcuts import redirect
from attendanceproject.settings import MEDIA_URL
import csv
# class user_authentication: 
client = pymongo.MongoClient("mongodb+srv://harsh:harsh@attendanceproject.rrlaxic.mongodb.net/?retryWrites=true&w=majority")
db = client['AttendanceProject']

    # def __init__(self,client,db):
    #     server_url = self.client
    #     database_name = self.db

def get_out(name):
    collection = db['superadmin_adminaccount']
    if name is not None:
        print(name+"helo")
        collection.update_one({"adminName":name},{"$set":{"loginStatus":False}})

def auth_user(user_name, user_password):
    final_output = False
    collection = db['superadmin_adminaccount']
    find_document = collection.find({"adminName":user_name})
    user_detail_in_database = []
    for item in find_document:
        db_user_name = item["adminName"]
        user_detail_in_database.append(db_user_name)
        db_user_password = item["adminPassword"]
        user_detail_in_database.append(db_user_password)
        
    if user_detail_in_database[0] == user_name and user_detail_in_database[1] == user_password:
        collection.update_one({"adminName":user_name},{"$set":{"loginStatus":True}})
        final_output = True

    return final_output
    
def check_if_allowed(user_name):
    permission_allowed = False
    collection = db['superadmin_adminaccount']
    find_document = collection.find({"adminName":user_name})
    for item in find_document:
        account_status = item["loginStatus"]
        permission_allowed = account_status

    return permission_allowed

def entry_check(get_response):

    def middleware(request):
        if not request.session.get('user'):
            return redirect('Login')
        else:
            pass
        response = get_response(request)
        return response

    return middleware

def add_course(course_id, course_name):
        db = client['AttendanceProject']
        collection = db['course_table']
        pass

def add_classroom(sql):
    db = client['AttendanceProject']
    collection = db['superadmin_classroom']
    collection.insert_one(sql)

def update_classroom(classroom_id,course_name,course_year,course_division,course_subject):
    db = client['AttendanceProject']
    collection = db['superadmin_classroom']
    collection.update_one({"ClassRoom_id":int(classroom_id)},{"$set":{"course_name":course_name, "course_year":course_year,"course_division":course_division,"course_subject":course_subject}}) 

def student_details(student_csv_file):
    data = []
    base = 'media/'
    FileWithLocation = base+str(student_csv_file)
    with open(FileWithLocation) as f:
            reader = csv.reader(f)
            for i in reader:
                    dict1 = {'student_prn':i[0],'student_email':i[1]}
                    data.append(dict1)
    return data

def teacher_details(teacher_csv_file):
    data = []
    base = 'media/'
    FileWithLocation = base+str(teacher_csv_file)
    with open(FileWithLocation) as f:
            reader = csv.reader(f)
            for i in reader:
                    dict1 = {'teacher_prn':i[0], 'teacher_email':i[1], 'teacher_subject':i[2]}
                    data.append(dict1)
    return data

def update_s_t(where,s_list,t_list):
    db = client['AttendanceProject']
    collection = db['superadmin_classroom']
    collection.update_one(where,{"$set":{'students':s_list,'teachers':t_list}}) 