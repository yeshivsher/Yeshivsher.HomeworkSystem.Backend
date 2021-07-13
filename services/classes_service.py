#!/usr/bin/env python
from models.classes import Classes
from config import db
from werkzeug.exceptions import NotFound

def get():
    '''
    Get all entities
    :returns: all entity
    '''
    return Classes.query.all()

def post(body):
    '''
    Create entity with body
    :param body: request body
    :returns: the created entity
    '''
    classes = Classes(**body)
    db.session.add(classes)
    db.session.commit()
    return classes

def put(body):
    '''
    Update entity by id
    :param body: request body
    :returns: the updated entity
    '''
    classes = Classes.query.get(body['id'])
    if classes:
        classes = Classes(**body)
        db.session.merge(classes)
        db.session.flush()
        db.session.commit()
        return classes
    raise NotFound('no such entity found with id=' + str(body['id']))

def delete(id):
    '''
    Delete entity by id
    :param id: the entity id
    :returns: the response
    '''
    classes = Classes.query.get(id)
    if classes:
        db.session.delete(classes)
        db.session.commit()
        return {'success': True}
    raise NotFound('no such entity found with id=' + str(id))


