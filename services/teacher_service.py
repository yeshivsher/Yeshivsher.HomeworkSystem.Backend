#!/usr/bin/env python
from models.teacher import Teacher
from config import db
from werkzeug.exceptions import NotFound
import json
from helper.AlchemyEncoder import AlchemyEncoder


def get():
    '''
    Get all entities
    :returns: all entity
    '''
    return Teacher.query.all()

def getById(id):
    return Teacher.query.filter_by(id=id).first()

def post(body):
    '''
    Create entity with body
    :param body: request body
    :returns: the created entity
    '''
    teacher = Teacher(**body)
    db.session.add(teacher)
    db.session.commit()
    return teacher


def login(mail, password):
    with db.engine.connect() as con:
        rs = con.execute("SELECT * FROM homework_system.teacher WHERE Mail='" +
                         str(mail)+"' and Password='"+str(password)+"'")
        for cols in rs:
            return {"data": cols, "isAuthenticated": True}

    raise NotFound('authenticated faild for: ' + str(mail))


def put(body):
    '''
    Update entity by id
    :param body: request body
    :returns: the updated entity
    '''
    teacher = Teacher.query.get(body['id'])
    if teacher:
        teacher = Teacher(**body)
        db.session.merge(teacher)
        db.session.flush()
        db.session.commit()
        return teacher
    raise NotFound('no such entity found with id=' + str(body['id']))


def checkNameAndMail(name, mail):
    with db.engine.connect() as con:
        rs = con.execute("SELECT * FROM homework_system.teacher WHERE Mail='" +
                         str(mail)+"' and Name='"+str(name)+"'")
        for cols in rs:
            return {"data": cols, "isAuthenticated": True}

    raise NotFound('authenticated faild for: ' + str(mail))


def resetPasswordByMail(password, mail):
    teacherObj = Teacher.query.filter_by(mail=mail).first()
    tempTeacher = json.dumps(
        teacherObj, ensure_ascii=False, cls=AlchemyEncoder)
    teacher = json.loads(tempTeacher)

    body = {
        "classIds": teacher["classIds"],
        "id": teacher["id"],
        "lastName": teacher["lastName"],
        "name": teacher["name"],
        "mail": teacher["mail"],
        "password": password,
    }

    if teacher:
        teacher = Teacher(**body)
        db.session.merge(teacher)
        db.session.flush()
        db.session.commit()
        return teacher
    raise NotFound('resetPasswordByMail faild for: ' + str(mail))


def updateTeacherByNewClassIdAndTeacherId(teacherId, classId):
    teacherObj = Teacher.query.filter_by(id=int(teacherId)).first()
    tempTeacher = json.dumps(
        teacherObj, ensure_ascii=False, cls=AlchemyEncoder)
    teacher = json.loads(tempTeacher)
    
    teacherClassesList = json.loads(teacher["classIds"])
    teacherClassesList.append(classId)
    
    body = {
        "classIds": str(teacherClassesList),
        "id": teacher["id"],
        "lastName": teacher["lastName"],
        "name": teacher["name"],
        "mail": teacher["mail"],
        "password": teacher["password"],
    }

    if teacher:
        teacher = Teacher(**body)
        db.session.merge(teacher)
        db.session.flush()
        db.session.commit()
        return teacher
    raise NotFound('updateTeacherByNewClassId faild for: ' + str(teacherId))


def delete(id):
    '''
    Delete entity by id
    :param id: the entity id
    :returns: the response
    '''
    teacher = Teacher.query.get(id)
    if teacher:
        db.session.delete(teacher)
        db.session.commit()
        return {'success': True}
    raise NotFound('no such entity found with id=' + str(id))
