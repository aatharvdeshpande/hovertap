import pymongo
from django.shortcuts import redirect
# class user_authentication:
client = pymongo.MongoClient("mongodb+srv://harsh:harsh@attendanceproject.rrlaxic.mongodb.net/?retryWrites=true&w=majority")
db = client['AttendanceProject']

    # def __init__(self,client,db):
    #     server_url = self.client
    #     database_name = self.db
    
def auth_user(user_name, user_password):
    result = {'success': False,'message':'Login Failed','user':[]}

    collection = db['api_student_table'] # collection created
    find_document = collection.find({"college_email":user_name,"password":user_password})     
    for item in find_document:
        if item['college_email'] == None and item['password'] == None:
            return result
        else :    
            data = {
                "student_prn":item["student_prn"],
                "college_email":item["college_email"],
                "password":item["password"],
                "status":item["status"],
            }
            
            result['success']=True
            result['message']="Login Successfull"
            result['user']=data
            return result                

    return result

def update_user(student_prn,fname,lname,phone_number,personal_email):
    result = {'success': False,'message':'Data Not Found','user':[]}

    collection = db['api_student_table'] # collection created
    collection.update_one({"student_prn":student_prn},{"$set":{"fname":fname, "lname": lname, "phone_number": phone_number, "personal_email": personal_email, 'status': True}});
    find_document = collection.find({"student_prn":student_prn})     
    for item in find_document:
        if item['college_email'] == None and item['password'] == None:
            return result
        else :    
            data = {
                "student_prn":item["student_prn"],
                "college_email":item["college_email"],
                "password":item["password"],
                "status":item["status"],
            }
            
            result['success']=True
            result['message']="Data Successfully Stored."
            result['user']=data
            return result                

    return result

def markAttendance(student_prn,nfcid,date,time):
    result = {'success': False,'message':'Data Not Found','user':[]}
    

    collection = db['superadmin_classroom'] # collection created
    markcollection = db['api_attendance_request'] # collection created
    find_document = collection.find({"students":{"$elemMatch":{"student_prn":student_prn}}})
    for item in find_document:
        if item['ClassRoom_id'] == None:
            result['message']="Student is not allowed to classroom."
            return result
        else : 
            classRoomId = item['ClassRoom_id']   
            tnfcid_list = nfcid.split('_')
            tnfcid = tnfcid_list[0]
            markcollection.update_one({"nfcid":{"$regex": tnfcid}, "date":date, "classroom_id": classRoomId}, {"$push":{ "student_list": { "$each":[ { "student_prn": student_prn, "nfcid":nfcid } ] } }}) 
            
            markData = markcollection.find({"nfcid": {"$regex": tnfcid}, "date":date,"classroom_id":classRoomId,"student_list":{"$elemMatch": {"student_prn":student_prn}}})
            for row in markData:
                
                result['success']=True
                result['message']="Attendance marked for "+row['subject']
                return result                
    return result

def getuserprofile(student_prn):
    result = {'success': False,'message':'Data Not Found','user':[]}
    

    collection = db['superadmin_classroom'] # collection created 
    studentcollection = db['api_student_table'] # collection created
    find_document = collection.find({"students":{"$elemMatch":{"student_prn":student_prn}}})
    for item in find_document:
        if item['ClassRoom_id'] == None:
            result['message']="Student is not allowed to classroom."
            return result
        else : 
            course_name = item['course_name']            
            markData = studentcollection.find({"student_prn": student_prn})
            for row in markData:
                data = {
                    "course_name": course_name,
                    "student_prn": row['student_prn'],
                    "fname": row['fname'],
                    "lname": row['lname'],
                    "phone_number": row['phone_number'],
                    "college_email": row['college_email'],
                    "personal_email": row['personal_email'],
                    "status": row['status'],
                }
                result['success']=True
                result['message']="Data Found Successfully"
                result['user']=data
                return result                
    return result

def update_password(student_prn,password):
    result = {'success': False,'message':'Facing some error.','user':[]}
    

    studentcollection = db['api_student_table'] # collection created
    find_document = studentcollection.find({"student_prn": student_prn})
    for item in find_document:
        if item['student_prn'] == None:
            result['message']="No User Found !!!"
            return result
        else : 
                studentcollection.update_one({"student_prn": student_prn},{"$set":{"password": password}})
                result['success']=True
                result['message']="Password updated successfully"
                return result                
    return result    

def get_user_timetable(student_prn,time,day):
    result = {'success': False,'message':'Facing some error.','user':[]}
    collection = db['api_student_timetable']
    find_document = collection.find({day: { "$elemMatch" : { "time": time } }, "students":student_prn},{day:1,"course_name": 1, "year": 1, "panel": 1})
    for item in find_document:
        if item['_id'] == None:
            result['message']="No Timetable Found !!!"
            return result
        else:
            data = {
                "course_name":item['course_name'],
                "year":item['year'],
                "panel":item['panel'],
                day:[]
            }
            for row in item[day]:
                data[day].append(row)
                
            result['success']=True
            result['message']="Data Found Successfully"
            result['user']=data
            return result
    return result        

#Teacher Function 
def auth_teacher(user_name, user_password):
    result = {'success': False,'message':'Login Failed','user':[]}

    collection = db['api_teacher_table'] # collection created
    find_document = collection.find({"college_email":user_name,"password":user_password})     
    for item in find_document:
        if item['college_email'] == None and item['password'] == None:
            return result
        else :    
            data = {
                "teacher_prn":item["teacher_prn"],
                "college_email":item["college_email"],
                "password":item["password"],
                "status":item["status"],
            }
            
            result['success']=True
            result['message']="Login Successfull"
            result['user']=data
            return result                

    return result

def update_teacher(teacher_prn,fname,lname,phone_number,personal_email):
    result = {'success': False,'message':'Data Not Found','user':[]}

    collection = db['api_teacher_table'] # collection created
    collection.update_one({"teacher_prn":teacher_prn},{"$set":{"fname":fname, "lname": lname, "phone_number": phone_number, "personal_email": personal_email, 'status': True}});
    find_document = collection.find({"teacher_prn":teacher_prn})     
    for item in find_document:
        if item['college_email'] == None and item['password'] == None:
            return result
        else :    
            data = {
                "teacher_prn":item["teacher_prn"],
                "college_email":item["college_email"],
                "password":item["password"],
                "status":item["status"],
            }
            
            result['success']=True
            result['message']="Data Successfully Stored."
            result['user']=data
            return result                

    return result

def getteacherprofiles(teacher_prn):
    result = {'success': False,'message':'Data Not Found','user':[]}
    

    collection = db['superadmin_classroom'] # collection created 
    studentcollection = db['api_teacher_table'] # collection created
    find_document = collection.find({"teachers":{"$elemMatch":{"teacher_prn":teacher_prn}}})
    for item in find_document:
        if item['ClassRoom_id'] == None:
            result['message']="Student is not allowed to classroom."
            return result
        else : 
            course_name = item['course_name']            
            markData = studentcollection.find({"teacher_prn": teacher_prn})
            for row in markData:
                data = {
                    "course_name": course_name,
                    "teacher_prn": row['teacher_prn'],
                    "fname": row['fname'],
                    "lname": row['lname'],
                    "phone_number": row['phone_number'],
                    "college_email": row['college_email'],
                    "personal_email": row['personal_email'],
                    "status": row['status'],
                }
                result['success']=True
                result['message']="Data Found Successfully"
                result['user']=data
                return result                
    return result

def update_teacher_password(teacher_prn,password):
    result = {'success': False,'message':'Facing some error.','user':[]}
    

    studentcollection = db['api_teacher_table'] # collection created
    find_document = studentcollection.find({"teacher_prn": teacher_prn})
    for item in find_document:
        if item['teacher_prn'] == None:
            result['message']="No User Found !!!"
            return result
        else : 
                studentcollection.update_one({"teacher_prn": teacher_prn},{"$set":{"password": password}})
                result['success']=True
                result['message']="Password updated successfully"
                return result                
    return result   

def get_subject(teacher_prn):
    result = {'success': False,'message':'Facing some error.','user':[]}
    

    studentcollection = db['superadmin_classroom'] # collection created
    find_document = studentcollection.find({"teachers": { "$elemMatch": { "teacher_prn": teacher_prn } }})
    for item in find_document:
        if item['ClassRoom_id'] == None:
            result['message']="No Data Found For Subject !!!"
            return result
        else : 
            subjects = ""
            for row in item['teachers']:
                if(row['teacher_prn'] == teacher_prn):
                    subjects = row['teacher_subject']

            subjectList = subjects.split(",")
            subList = []
            for sub in subjectList:
                testData = {
                    "subject":sub
                }
                subList.append(testData)

            data={
                "subjects": subList
            }
            result['success']=True
            result['message']="Data Found Successfully"
            result['user']=data
            return result                
    return result

def TmarkAttendance(teacher_prn,nfcid,subject,date,time):
    result = {'success': False,'message':'Data Not Found','user':[]}
    

    collection = db['superadmin_classroom'] # collection created
    markcollection = db['api_attendance_request'] # collection created
    find_document = collection.find({"teachers": { "$elemMatch": { "teacher_prn": teacher_prn , "teacher_subject": {"$regex": subject}} }})
    for item in find_document:
        if item['ClassRoom_id'] == None:
            result['message']="Teacher is not allowed to classroom."
            return result
        else : 
            classRoomId = item['ClassRoom_id']  
            course_name = item['course_name']
            markcollection.insert_one({"course": course_name, "classroom_id": classRoomId, "subject": subject, "nfc_id": nfcid, "teacherid": teacher_prn, "date": date, "time":time, "student_list":[]})
            markDoc = markcollection.find({"course": course_name, "classroom_id": classRoomId, "subject": subject, "nfc_id": nfcid, "teacherid": teacher_prn, "date": date, "time":time})             
            for row in markDoc:  

                result['success']=True
                result['message']="Session start for "+row['subject']
                return result                
    return result

def display_count(teacher_prn,subject,date):
    result = {'success': False,'message':'Data Not Found','user':[]}
    

    collection = db['superadmin_classroom'] # collection created
    markcollection = db['api_attendance_request'] # collection created
    find_document = collection.aggregate([
      {
        '$addFields': {
          'size': {
            '$size': '$students'
          }
        }
      }, {
        '$group': {
          '_id': None, 
          'students_count': {
            '$sum': '$size'
          }
        }
      }
    ])
    for item in find_document:
        if item['students_count'] == None:
            result['message']="No Student Found In Classroom"
            return result
        else : 
            total_students_count = item['students_count']  
            markDoc = markcollection.aggregate([{"$match": { "teacher_id": teacher_prn, "subject": subject, "date": date}},
            {
                '$addFields': {
                'size': {
                    '$size': '$student_list'
                }
                }
            }, {
                '$group': {
                '_id': None, 
                'student_count': {
                    '$sum': '$size'
                }
                }
            }
            ])         
            total_present_students_count=0    
            for row in markDoc:  
                total_present_students_count = row['student_count']

            data = {
                "total": total_students_count,
                "present": total_present_students_count,
                "absent": (total_students_count - total_present_students_count)
            }

            result['success']=True
            result['message']="Data Found Successfully"
            result['user']=data
            return result  

    return result



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