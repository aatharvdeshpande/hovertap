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
    find_document = collection.find({"name":user_name,"password":user_password})     
    for item in find_document:
        if item['name'] == None and item['password'] == None:
            return result
        else :    
            db_user_name = item["name"]
            db_user_password = item["password"]
            
            result['success']=True
            result['message']=True
            result['user']=item
            collection.update_one({"name":user_name},{"$set":{"status":True}})
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