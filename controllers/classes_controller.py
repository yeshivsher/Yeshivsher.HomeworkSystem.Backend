#!/usr/bin/env python
from flask import Blueprint, jsonify, request
import services.classes_service as classes_service
from models.classes import Classes
from werkzeug.exceptions import HTTPException
import json
from helper.AlchemyEncoder import AlchemyEncoder
import services.teacher_service as teacher_service

classesApi = Blueprint('classes', 'classes')


@classesApi.route('/classes', methods=['GET'])
def api_get():
    classess = classes_service.get()
    classessToList = []

    for t in classess:
        classessToList.append(json.dumps(
            t, ensure_ascii=False, cls=AlchemyEncoder))

    return jsonify({'classes': classessToList})


@classesApi.route('/classes', methods=['POST'])
def api_post():
    ''' Create entity'''
    # print('5555555555555555555555555')
    # print(request.json["className"])
    # print(request.json) 
    # return
    classObj = classes_service.post(
        {"className": request.json["className"], "credits": int(request.json["credits"])})

    classObjFormated = json.dumps(
        classObj, ensure_ascii=False, cls=AlchemyEncoder)

    classObjFormated = json.loads(classObjFormated)

    teacher_service.updateTeacherByNewClassIdAndTeacherId(
        request.json["teacherId"], classObjFormated["id"])

    return jsonify({"success": True, "data": json.dumps(classObj, ensure_ascii=False, cls=AlchemyEncoder)})


# @ api.route('/classes/<string:id>', methods=['PUT'])
# def api_put(id):
#     ''' Update entity by id'''
#     body = request.json
#     body['id'] = id
#     res = classes_service.put(body)
#     return jsonify(res.as_dict()) if isinstance(res, classes) else jsonify(res)


# @ api.route('/classes/<string:id>', methods=['DELETE'])
# def api_delete(id):
#     ''' Delete entity by id'''
#     res = classes_service.delete(id)
#     return jsonify(res)


@ classesApi.errorhandler(HTTPException)
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
