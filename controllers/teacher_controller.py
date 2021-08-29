#!/usr/bin/env python
from flask import Blueprint, jsonify, request
from werkzeug.wrappers import response
import services.teacher_service as teacher_service
from models.teacher import Teacher
from werkzeug.exceptions import HTTPException
import json
from helper.AlchemyEncoder import AlchemyEncoder

teacherApi = Blueprint('teacher', 'teacher')

teacherToken = "teacher"


@teacherApi.route('/teacher', methods=['GET'])
def api_get():
    teachers = teacher_service.get()
    teachersToList = []

    for t in teachers:
        teachersToList.append(json.dumps(
            t, ensure_ascii=False, cls=AlchemyEncoder))

    return jsonify({'teachers': teachersToList})


@teacherApi.route('/teacher/<string:id>', methods=['GET'])
def api_getById(id):
    teacherObj = teacher_service.getById(id)

    teacher = json.dumps(teacherObj, ensure_ascii=False, cls=AlchemyEncoder)

    return jsonify({'teacher': teacher})


@teacherApi.route('/teacher', methods=['POST'])
def api_post():
    ''' Create entity'''
    teacher = teacher_service.post(request.json)
    teacherWithoutPassword = {
        "id": teacher.id,
        "name": teacher.name,
        "lastName": teacher.lastName,
        "classIds": teacher.classIds,
        "mail": teacher.mail,
        "token": teacherToken
    }
    return jsonify({"success": True, "data": json.dumps(teacherWithoutPassword, ensure_ascii=False, cls=AlchemyEncoder)})


@teacherApi.route('/teacher/login', methods=['GET'])
def login():
    mail = request.args.get('mail')
    password = request.args.get('password')

    re = teacher_service.login(mail, password)
    print(re)
    teacherWithoutPassword = {
        "id": re["data"][0],
        "name": re["data"][1],
        "lastName": re["data"][2],
        "classIds": re["data"][5],
        "mail": re["data"][4],
        "token": teacherToken
    }
    response = jsonify(
        {"isAuthenticated": re["isAuthenticated"], "token": teacherToken, "data": teacherWithoutPassword})

    return response


@teacherApi.route('/teacher/checknameandmail', methods=['GET'])
def checkNameAndMail():
    name = request.args.get('name')
    mail = request.args.get('mail')

    re = teacher_service.checkNameAndMail(name, mail)
    teacherWithoutPassword = {
        "id": re["data"][0],
        "name": re["data"][1],
        "lastName": re["data"][2],
        "classIds": re["data"][5],
        "mail": re["data"][4]
    }
    return jsonify({"isAuthenticated": re["isAuthenticated"], "token": teacherToken, "data": teacherWithoutPassword})


@teacherApi.route('/teacher/resetpasswordbymail', methods=['put'])
def resetPasswordByMail():
    password = request.args.get('password')
    mail = request.args.get('mail')

    re = teacher_service.resetPasswordByMail(password, mail)
    tempTeacher = json.dumps(re, ensure_ascii=False, cls=AlchemyEncoder)
    teacher = json.loads(tempTeacher)

    teacherWithoutPassword = {
        "id": teacher["id"],
        "name": teacher["name"],
        "lastName": teacher["lastName"],
        "classIds": teacher["classIds"],
        "mail": teacher["mail"]
    }
    return jsonify({"isAuthenticated": True, "token": teacherToken, "data": teacherWithoutPassword})


# @ api.route('/teacher/<string:id>', methods=['PUT'])
# def api_put(id):
#     ''' Update entity by id'''
#     body = request.json
#     body['id'] = id
#     res = teacher_service.put(body)
#     return jsonify(res.as_dict()) if isinstance(res, Teacher) else jsonify(res)


# @ api.route('/teacher/<string:id>', methods=['DELETE'])
# def api_delete(id):
#     ''' Delete entity by id'''
#     res = teacher_service.delete(id)
#     return jsonify(res)


@teacherApi.errorhandler(HTTPException)
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
