import requests, json
from bson.objectid import ObjectId
import os

auth = requests.auth.HTTPBasicAuth(os.environ.get("api_user"), os.environ.get("api_pass"))

URL= os.environ.get("url")
BASE_URL = f"{URL}/students/"


# get all students
def get_all_students_from_api():
    all_students_api_link = BASE_URL
    response = requests.get(all_students_api_link, auth=auth)
    students = json.loads(response.text)
    return students

# get one student
def get_one_student_from_api(id):
    _id = id[10:34]
    all_students_api_link = f"{BASE_URL}{_id}"
    response = requests.get(all_students_api_link, auth=auth)
    student = json.loads(response.text)
    return student

# delete one student
def delete_student_from_api(id):
    _id = id[10:34]
    url = BASE_URL
    payload = {"id":_id}
    requests.delete(url, json=payload, auth=auth)

# put one student
def edited_student_admin_api_request(id,student_id, status, first_name, last_name, email, gender, professor_name, year_of_graduation, degree, projectId, programming_language):
    _id = id[10:34]
    url = BASE_URL
    payload = {
        "id": _id,
        "student_id":student_id,
        "status" : status,
        "first_name" : first_name,
        "last_name" : last_name,
        "email" : email,
        "gender" :  gender,
        "professor_name" : professor_name,
        "year_of_graduation" : year_of_graduation,
        "degree" : degree,
        "projectId" : projectId,
        "programming_language" : programming_language
    }
    requests.put(url, json=payload, auth=auth)
    #add student 
def add_student_to_list(student_Id,first_name,last_name,email,gender, professor_name, year_of_graduation, degree, projectId, programming_language,resume,status="active"):
        url = BASE_URL
        payload = {
        "student_id":student_Id,
        "status":status,
        "first_name":first_name,
        "last_name":last_name,
        "email":email, 
        "gender":gender,
        "professor_name":professor_name, 
        "year_of_graduation": year_of_graduation, 
        "degree":degree,
        "projectId":projectId,
        "programming_language":programming_language,
        "resume":resume
        }
        requests.post(url, json=payload, auth=auth)
