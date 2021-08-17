#!/usr/bin/env python
from models.student import Student
from config import db
from werkzeug.exceptions import NotFound
import json
from helper.AlchemyEncoder import AlchemyEncoder


def get():
    '''
    Get all entities
    :returns: all entity
    '''
    getStudentsListByClassId(1)
    return Student.query.all()


def post(body):
    '''
    Create entity with body
    :param body: request body
    :returns: the created entity
    '''
    student = Student(**body)
    db.session.add(student)
    db.session.commit()
    return student


def login(mail, password):
    with db.engine.connect() as con:
        rs = con.execute("SELECT * FROM homework_system.student WHERE Mail='" +
                         str(mail)+"' and Password='"+str(password)+"'")
        for cols in rs:
            return {"data": cols, "isAuthenticated": True}

    raise NotFound('authenticated faild for: ' + str(mail))


def checkNameAndMail(name, mail):
    with db.engine.connect() as con:
        rs = con.execute("SELECT * FROM homework_system.student WHERE Mail='" +
                         str(mail)+"' and Name='"+str(name)+"'")
        for cols in rs:
            return {"data": cols, "isAuthenticated": True}

    raise NotFound('authenticated faild for: ' + str(mail))


def resetPasswordByMail(password, mail):
    studentObj = Student.query.filter_by(mail=mail).first()
    tempStudent = json.dumps(
        studentObj, ensure_ascii=False, cls=AlchemyEncoder)
    student = json.loads(tempStudent)

    body = {
        "classIds": student["classIds"],
        "id": student["id"],
        "lastName": student["lastName"],
        "name": student["name"],
        "mail": student["mail"],
        "password": password,
    }

    if student:
        student = Student(**body)
        db.session.merge(student)
        db.session.flush()
        db.session.commit()
        return student
    raise NotFound('resetPasswordByMail faild for: ' + str(mail))


def put(body):
    '''
    Update entity by id
    :param body: request body
    :returns: the updated entity
    '''
    student = Student.query.get(body['id'])
    if student:
        student = Student(**body)
        db.session.merge(student)
        db.session.flush()
        db.session.commit()
        return student
    raise NotFound('no such entity found with id=' + str(body['id']))


def delete(id):
    '''
    Delete entity by id
    :param id: the entity id
    :returns: the response
    '''
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return {'success': True}
    raise NotFound('no such entity found with id=' + str(id))

#########################
# helper functoins
def getStudentsListByClassId(classId):
    classIdToNumber = int(classId)
    allStudents = Student.query.all()
    studentsList = []

    for s in allStudents:
        classIdsJson = json.loads(s.classIds)
        if classIdToNumber in classIdsJson:
            studentsList.append(s.id)
            
    return studentsList