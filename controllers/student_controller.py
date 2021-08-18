#!/usr/bin/env python
from os import name
from flask import Blueprint, jsonify, request
import services.student_service as student_service
from models.student import Student
from werkzeug.exceptions import HTTPException
import json
from helper.AlchemyEncoder import AlchemyEncoder

studentApi = Blueprint('student', 'student')

studentToken = "student"


@studentApi.route('/student', methods=['GET'])
def api_get():
    students = student_service.get()
    studentsToList = []

    for t in students:
        jsonString = json.dumps(
            t, ensure_ascii=False, cls=AlchemyEncoder)
        
        tempStudent = json.loads(jsonString)
        studentWithoutPassword = {
            "id": tempStudent["id"],
            "name": tempStudent["name"],
            "lastName": tempStudent["lastName"],
            "classIds": tempStudent["classIds"],
            "mail": tempStudent["mail"]
        }
        studentsToList.append(studentWithoutPassword)

    return jsonify({'students': studentsToList})


@studentApi.route('/student', methods=['POST'])
def api_post():
    ''' Create entity'''
    student = student_service.post(request.json)
    studentWithoutPassword = {
        "id": student.id,
        "name": student.name,
        "lastName": student.lastName,
        "classIds": student.classIds,
        "mail": student.mail,
        "token": studentToken
    }
    
    return jsonify({"success": True, "data": json.dumps(studentWithoutPassword, ensure_ascii=False, cls=AlchemyEncoder)})


@studentApi.route('/student/login', methods=['GET'])
def login():
    mail = request.args.get('mail')
    password = request.args.get('password')

    re = student_service.login(mail, password)
    studentWithoutPassword = {
        "id": re["data"][0],
        "name": re["data"][1],
        "lastName": re["data"][2],
        "classIds": re["data"][5],
        "mail": re["data"][4],
        "token": studentToken
    }
    return jsonify({"isAuthenticated": re["isAuthenticated"], "token": studentToken, "data": studentWithoutPassword})

@studentApi.route('/student/checknameandmail', methods=['GET'])
def checkNameAndMail():
    name = request.args.get('name')
    mail = request.args.get('mail')

    re = student_service.checkNameAndMail(name, mail)
    studentWithoutPassword = {
        "id": re["data"][0],
        "name": re["data"][1],
        "lastName": re["data"][2],
        "classIds": re["data"][5],
        "mail": re["data"][4]
    }
    return jsonify({"isAuthenticated": re["isAuthenticated"], "token": studentToken, "data": studentWithoutPassword})

@studentApi.route('/student/resetpasswordbymail', methods=['put'])
def resetPasswordByMail():
    password = request.args.get('password')
    mail = request.args.get('mail')

    re = student_service.resetPasswordByMail(password, mail)
    tempStudent = json.dumps(re, ensure_ascii=False, cls=AlchemyEncoder)
    student = json.loads(tempStudent)

    studentWithoutPassword = {
        "id": student["id"],
        "name": student["name"],
        "lastName": student["lastName"],
        "classIds": student["classIds"],
        "mail": student["mail"]
    }
    return jsonify({"isAuthenticated": True,"token": studentToken, "data": studentWithoutPassword})


# @studentApi.route('/student/<string:id>', methods=['PUT'])
# def api_put(id):
#     ''' Update entity by id'''
#     body = request.json
#     body['id'] = id
#     res = student_service.put(body)
#     return jsonify(res.as_dict()) if isinstance(res, Student) else jsonify(res)


# @studentApi.route('/student/<string:id>', methods=['DELETE'])
# def api_delete(id):
#     ''' Delete entity by id'''
#     res = student_service.delete(id)
#     return jsonify(res)


@studentApi.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON format for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        'success': False,
        "message": e.description
    })
    response.content_type = "application/json"
    return response
