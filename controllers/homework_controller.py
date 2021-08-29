#!/usr/bin/env python
from flask import Blueprint, jsonify
import services.homework_service as homework_service
from models.homework import Homework
from werkzeug.exceptions import HTTPException
import json
from helper.AlchemyEncoder import AlchemyEncoder, AlchemyEncoderForDatetime
from io import BytesIO
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
import sys

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

@homeworkApi.route('/homework/getExamQuestionByHomeworkId', methods=['GET'])
def getExamQuestionByHomeworkId():
    homeworkId = request.args.get('homeworkId')

    homework = homework_service.getFileByHomeworkId(homeworkId)

    return jsonify({'fileData': homework.examQuestion.decode('UTF-8')})


@homeworkApi.route('/homework', methods=['POST'])
def api_post():
    name = request.form['name']
    classId = request.form['classId']
    studentId = request.form['studentId']
    date = request.form['date']
    print('------------------------------\n\n\n')

    homework = homework_service.post(
        name, classId, studentId, date)

    return jsonify({"success": True})


@homeworkApi.route('/homework/addExam', methods=['POST'])
def api_postNewExam():
    name = request.form['name']
    classId = request.form['classId']
    isExam = request.form['isExam']
    studentId = -1
    examQuestion = request.files['examQuestion']
    examSolution = request.files['examSolution']
    date = request.form['date']
    argsType = request.form['argsType']
    
    homeworkId = homework_service.postNewExam(
        name, classId, isExam, studentId, examQuestion, examSolution, date, argsType)
    
    return jsonify({"success": True, "addId": homeworkId})


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
    argsType = request.form['argsType']
    isExam = request.form['isExam']
    examId = request.form['examId']
    
    homework = homework_service.put(
        id, file, name, classId, status, grade, studentId, isFileExist, argsType, isExam, examId)

    return jsonify({"success": True})


@homeworkApi.route('/homework/updateWithoutFile/<string:id>', methods=['PUT'])
def api_putWithoutFile(id):
    print(id)
    
    ''' Update entity by id'''
    name = request.form['name']
    classId = request.form['classId']
    status = request.form['status']
    grade = request.form['grade']
    studentId = request.form['studentId']
    argsType = request.form['argsType']
    isExam = request.form['isExam']
    examId = request.form['examId']

    homework = homework_service.putWithoutFile(
        id,  name, classId, status, grade, studentId, argsType, isExam, examId)

    return jsonify({"success": True})
 

@homeworkApi.route('/homework/pythonCodeCheckerByHomeworkId', methods=['GET'])
def api_PythonCodeCheckerByHomeworkId():
    homeworkId = request.args.get('homeworkId')

    data = homework_service.pythonCodeCheckerByHomeworkId(homeworkId)

    return jsonify({'data': data})


@homeworkApi.route('/homework/pythonCodeChecker', methods=['POST'])
def api_PythonCodeChecker():
    file = request.files['file']

    grade = homework_service.PostPythonCodeChecker(file)

    return jsonify({'grade': grade})



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
