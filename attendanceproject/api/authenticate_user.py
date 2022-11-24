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