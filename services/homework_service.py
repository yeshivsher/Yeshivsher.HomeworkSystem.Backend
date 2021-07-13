#!/usr/bin/env python
from models.homework import Homework
from config import db
from werkzeug.exceptions import NotFound
from flask_sqlalchemy import SQLAlchemy
from helper.StrToBool import Str2bool
from helper.NullStrToNull import NullStrToNull


def get():
    '''
    Get all entities
    :returns: all entity
    '''
    with db.engine.connect() as con:
        rs = con.execute("SELECT * FROM homework_system.homework")
        d, a = {}, []
        for r in rs:
            for column, value in r.items():
                # build up the dictionary
                d = {**d, **{column: value}}
            a.append(d)
        return a

    raise NotFound('authenticated faild for: ' + str(id))


def getAllByStudentId(id):
    with db.engine.connect() as con:
        rs = con.execute("SELECT * FROM homework_system.homework WHERE StudentId=" +
                         str(id))
        d, a = {}, []
        for r in rs:
            for column, value in r.items():
                # build up the dictionary
                d = {**d, **{column: value}}
            a.append(d)
        return a

    raise NotFound('authenticated faild for: ' + str(id))


def getFileByHomeworkId(id):
    return Homework.query.filter_by(id=id).first()


def post(file, name, classId, status, studentId, isFileExist):
    '''
    Create entity with body
    :param body: request body
    :returns: the created entity
    '''
    body = {
        "fileData": file.read(),
        "name": name,
        "classId": classId,
        "status": status,
        "studentId": studentId,
        "isFileExist": Str2bool.default(isFileExist)
    }
    homework = Homework(**body)
    db.session.add(homework)
    db.session.commit()
    return homework


def put(id, file, name, classId, status, grade, studentId, isFileExist):
    '''
    Update entity by id
    :param body: request body
    :returns: the updated entity
    '''
    body = {
        "id": id,
        "fileData": file.read(),
        "name": name,
        "classId": classId,
        "status": status,
        "grade": NullStrToNull.default(grade),
        "studentId": studentId,
        "isFileExist": Str2bool.default(isFileExist)
    }
    homework = Homework.query.get(id)
    if homework:
        homework = Homework(**body)
        db.session.merge(homework)
        db.session.flush()
        db.session.commit()
        return homework
    raise NotFound('no such entity found with id=' + str(id))


def putWithoutFile(id,  name, classId, status, grade, studentId):
    '''
    Update entity by id
    :param body: request body
    :returns: the updated entity
    '''
    body = {
        "id": id,
        "name": name,
        "classId": classId,
        "status": status,
        "grade": grade,
        "studentId": studentId
    }
    homework = Homework.query.get(id)
    if homework:
        homework = Homework(**body)
        db.session.merge(homework)
        db.session.flush()
        db.session.commit()
        return homework
    raise NotFound('no such entity found with id=' + str(body['id']))


def delete(id):
    '''
    Delete entity by id
    :param id: the entity id
    :returns: the response
    '''
    homework = Homework.query.get(id)
    if homework:
        db.session.delete(homework)
        db.session.commit()
        return {'success': True}
    raise NotFound('no such entity found with id=' + str(id))
