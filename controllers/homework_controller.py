#!/usr/bin/env python
from flask import Blueprint, jsonify
import services.homework_service as homework_service
from models.homework import Homework
from werkzeug.exceptions import HTTPException
import json
from helper.AlchemyEncoder import AlchemyEncoder, AlchemyEncoderForDatetime
from io import BytesIO
from flask import Flask, render_template, request, send_file

homeworkApi = Blueprint('homework', 'homework')


@homeworkApi.route('/homework', methods=['GET'])
def api_get():
    homeworks = homework_service.get()

    return jsonify({'homeworks': json.dumps(homeworks, ensure_ascii=False, cls=AlchemyEncoderForDatetime)})


@homeworkApi.route('/homework/byStudnetId', methods=['GET'])
def getAllByStudentId():
    studentId = request.args.get('studentId')

    homeworks = homework_service.getAllByStudentId(studentId)

    return jsonify({'homeworks': json.dumps(homeworks, ensure_ascii=False, cls=AlchemyEncoderForDatetime)})


@homeworkApi.route('/homework/getFileByHomeworkId', methods=['GET'])
def download():
    homeworkId = request.args.get('homeworkId')

    file = homework_service.getFileByHomeworkId(homeworkId)

    return jsonify({'fileData': file.fileData.decode('UTF-8')})


@homeworkApi.route('/homework', methods=['POST'])
def api_post():
    file = request.files['fileData']
    name = request.form['name']
    classId = request.form['classId']
    status = request.form['status']
    studentId = request.form['studentId']
    isFileExist = request.form['isFileExist']

    homework = homework_service.post(
        file, name, classId, status, studentId, isFileExist)

    if file.filename != '':
        file.save(file.filename)

    return jsonify({"success": True})


@homeworkApi.route('/homework/<string:id>', methods=['PUT'])
def api_put(id):
    ''' Update entity by id'''
    file = request.files['fileData']
    name = request.form['name']
    classId = request.form['classId']
    status = request.form['status']
    grade = request.form['grade']
    studentId = request.form['studentId']
    isFileExist = request.form['isFileExist']
    print(grade)

    homework = homework_service.put(
        id, file, name, classId, status, grade, studentId, isFileExist)

    if file.filename != '':
        file.save(file.filename)

    return jsonify({"success": True})


@homeworkApi.route('/homework/updateWithoutFile/<string:id>', methods=['PUT'])
def api_putWithoutFile(id):
    ''' Update entity by id'''
    name = request.form['name']
    classId = request.form['classId']
    status = request.form['status']
    grade = request.form['grade']
    studentId = request.form['studentId']

    homework = homework_service.putWithoutFile(
        id,  name, classId, status, grade, studentId)

    return jsonify({"success": True})

# @ api.route('/homework/<string:id>', methods=['DELETE'])
# def api_delete(id):
#     ''' Delete entity by id'''
#     res = homework_service.delete(id)
#     return jsonify(res)


@homeworkApi.errorhandler(HTTPException)
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
